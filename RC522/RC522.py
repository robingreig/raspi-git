#!/usr/bin/env python

import time

OK                  = 0
ERR_NO_TAG          = 1
ERR_UNKNOWN         = 2
ERR_BAD_CRC         = 3
ERR_BAD_LEN         = 4
ERR_TIMEOUT_1       = 5
ERR_TIMEOUT_2       = 6
ERR_BAD_ACCESS_BITS = 7

SPI_CE0      = 0
SPI_CE1      = 1
AUX_SPI_CE0  = 2
AUX_SPI_CE1  = 3
AUX_SPI_CE2  = 4

KEY_A = 0
KEY_B = 1

DBG_OFF=0
DBG_MIN=1
DBG_MAX=2

"""
You need three hardware components

1) a Raspberry Pi
2) a PCD (Proximity Coupling Device), e.g. NXP MFRC522 card reader
3) a PICC (Proximity Integrated Circuit Card), e.g. a Mifare tag

The Pi and the PCD may communicate via SPI, I2C, or a serial link.

This impememtation uses SPI.

The card reader (PCD) and the tags (PICC) communicate using a 13.56MHz radio
link.

The protocol is defined in

ISO/IEC 14443-3 Identification cards
Contactless integrated circuit cards
Proximity cards
Part 3: Initialization and anticollision

See http://wg8.de/wg8n1496_17n3613_Ballot_FCD14443-3.pdf

If only the PICC UID is wanted, the above document has all the needed
information.

To read and write from MIFARE PICCs, the MIFARE protocol is used after
the PICC has been selected.

The MIFARE chips and protocol are described in the following datasheets

1K: http://www.mouser.com/ds/2/302/MF1S503x-89574.pdf
4K: http://datasheet.octopart.com/MF1S7035DA4,118-NXP-Semiconductors-datasheet-11046188.pdf
Mini: http://www.idcardmarket.com/download/mifare_S20_datasheet.pdf
Ultralight:   http://www.nxp.com/documents/data_sheet/MF0ICU1.pdf
Ultralight C: http://www.nxp.com/documents/short_data_sheet/MF0ICU2_SDS.pdf

1K

16 sectors * 4 blocks/sector * 16 bytes/block = 1024 bytes.
The blocks are numbered 0-63.
Block 3 in each sector is the Sector Trailer

   Bytes 0-5:   Key A
   Bytes 6-8:   Access Bits
   Bytes 9:     User data
   Bytes 10-15: Key B (or user data)

Block 0 is read-only manufacturer data, sometimes as follows,

 0 1 2 3 |4  | 5 |6   |7 8 9 A B C D E F
 UID     |BCC|SAK|ATAQ|Manufacturer data

To access a block, an authentication using a key from the block's sector must be performed first.

Example: To read from block 10, first authenticate using a key from sector 3 (blocks 8-11).

All keys are set to FFFFFFFFFFFFh at chip delivery.

WARNING: Please read section 8.7 "Memory Access".
"if the PICC detects a format violation the whole sector
is irreversibly blocked."

To use a block in "value block" mode (for Increment/Decrement operations)
you need to change the sector trailer. Use MIFARE_SetAccessBits()
to calculate the bit patterns.

4K

32 sectors * 4 blocks/sector * 16 bytes/block = 2048 bytes +
8 sectors * 16 blocks/sector * 16 bytes/block = 2048 bytes.

The blocks are numbered 0-255.

The last block in each sector is the Sector Trailer as for the 1K.

Mini

5 sectors * 4 blocks/sector * 16 bytes/block = 320 bytes.

The blocks are numbered 0-19.

The last block in each sector is the Sector Trailer as for the 1K.

Ultralight

16 pages of 4 bytes = 64 bytes.

Pages 0-1 are used for the 7-byte UID.
Page 2 contains the last check digit for the UID, one byte manufacturer internal data, and the lock bytes
Page 3 is OTP, One Time Programmable bits. Once set to 1 they cannot revert to 0.
Pages 4-15 are read/write unless blocked by the lock bytes in page 2. 

Ultralight

48 pages of 4 bytes = 192 bytes.

Pages 0-1 are used for the 7-byte UID.
Page 2 contains the last check digit for the UID, one byte manufacturer internal data, and the lock bytes
Page 3 is OTP, One Time Programmable bits. Once set to 1 they cannot revert to 0.
Pages 4-39 are read/write unless blocked by the lock bytes in page 2. 
Page 40 Lock bytes
Page 41 16 bit one way counter
Pages 42-43 Authentication configuration
Pages 44-47 Authentication key 


Access conditions for sector trailer
  KeyA  Bits  KeyB
  R  W  R  W  R  W
0 -  A  A  -  A  A
1 -  A  A  A  A  A Default
2 -  -  A  -  A  -
3 -  B  AB B  -  B
4 -  B  AB -  -  B
5 -  -  AB B  -  -
6 -  -  AB -  -  -
7 -  -  AB -  -  -

Access conditions for data blocks

    R   W   +  -X
0  AB  AB  AB  AB Data  Default
1  AB  --  --  AB Value
2  AB  --  --  -- Data
3   B   B  --  -- Data
4  AB   B  --  -- Data
5   B  --  --  -- Data
6  AB   B   B  AB Value
7  --  --  --  -- Data

"""
class PCD:
   """
   Workflow

   Call ISO_Request() to check to see if a tag is in range and if so
   get its ATQA.

   Upon success call ISO_Anticollision() which returns the UID of the
   active tag in range.

   Upon success call ISO_Select(UID) which selects the active tag in
   range by its UID and returns its SAK.

   If the card needs authentication call ISO_Authenticate(blockAddr,
   keyId, key, UID) to authenticate access to a block.

   Call ISO_StopCrypto() when you have finished talking to a card
   which requires authentication.
   """
   #_Reserved       = 0x00<<1
   _CommandReg      = 0x01<<1
   _ComlEnReg       = 0x02<<1
   _DivlEnReg       = 0x03<<1
   _CommIrqReg      = 0x04<<1
   _DivIrqReg       = 0x05<<1
   _ErrorReg        = 0x06<<1
   _Status1Reg      = 0x07<<1
   _Status2Reg      = 0x08<<1
   _FIFODataReg     = 0x09<<1
   _FIFOLevelReg    = 0x0A<<1
   _WaterLevelReg   = 0x0B<<1
   _ControlReg      = 0x0C<<1
   _BitFramingReg   = 0x0D<<1
   _CollReg         = 0x0E<<1
   #_Reserved       = 0x0F<<1

   #_Reserved       = 0x10<<1
   _ModeReg         = 0x11<<1
   _TxModeReg       = 0x12<<1
   _RxModeReg       = 0x13<<1
   _TxControlReg    = 0x14<<1
   _TxASKReg        = 0x15<<1
   _TxSelReg        = 0x16<<1
   _RxSelReg        = 0x17<<1
   _RxThresholdReg  = 0x18<<1
   _DemodReg        = 0x19<<1
   #_Reserved       = 0x1A<<1
   #_Reserved       = 0x1B<<1
   _MfTxReg         = 0x1C<<1
   _MfRxReg         = 0x1D<<1
   #Reserved       = 0x1E<<1
   _SerialSpeedReg  = 0x1F<<1

   #_Reserved       = 0x20<<1
   _CRCResultRegM   = 0x21<<1
   _CRCResultRegL   = 0x22<<1
   _Reserved21      = 0x23<<1
   _ModWidthReg     = 0x24<<1
   #_Reserved       = 0x25<<1
   _RFCfgReg        = 0x26<<1
   _GsNReg          = 0x27<<1
   _CWGsPReg        = 0x28<<1
   _ModGsPReg       = 0x29<<1
   _TModeReg        = 0x2A<<1
   _TPrescalerReg   = 0x2B<<1
   _TReloadRegH     = 0x2C<<1
   _TReloadRegL     = 0x2D<<1
   _TCounterValRegH = 0x2E<<1
   _TCounterValRegL = 0x2F<<1

   #_Reserved       = 0x30<<1
   _TestSel1Reg     = 0x31<<1
   _TestSel2Reg     = 0x32<<1
   _TestPinEnReg    = 0x33<<1
   _TestPinValueReg = 0x34<<1
   _TestBusReg      = 0x35<<1
   _AutoTestReg     = 0x36<<1
   _VersionReg      = 0x37<<1
   _AnalogTestReg   = 0x38<<1
   _TestDAC1Reg     = 0x39<<1
   _TestDAC2Reg     = 0x3A<<1
   _TestADCReg      = 0x3B<<1
   #_Reserved       = 0x3C<<1
   #_Reserved       = 0x3D<<1
   #_Reserved       = 0x3E<<1
   #_Reserved       = 0x3F<<1

   # MFRC522 commands

   _PCD_Idle             = 0x00
   _PCD_Mem              = 0x01
   _PCD_GenerateRandomID = 0x02
   _PCD_CalcCRC          = 0x03
   _PCD_Transmit         = 0x04
   _PCD_NoCmdChange      = 0x07
   _PCD_Receive          = 0x08
   _PCD_Transceive       = 0x0C
   _PCD_Authent          = 0x0E
   _PCD_SoftReset        = 0x0F

   # PICC commands

   _PICC_REQA          = 0x26
   _PICC_MF_READ       = 0x30
   _PICC_HLTA          = 0x50
   _PICC_WUPA          = 0x52
   _PICC_MF_AUTH_KEY_A = 0x60
   _PICC_MF_AUTH_KEY_B = 0x61
   _PICC_CT            = 0x88
   _PICC_SEL_CL1       = 0x93
   _PICC_SEL_CL2       = 0x95
   _PICC_SEL_CL3       = 0x97
   _PICC_MF_WRITE      = 0xA0
   _PICC_UL_WRITE      = 0xA2
   _PICC_MF_TRANSFER   = 0xB0
   _PICC_MF_DECREMENT  = 0xC0
   _PICC_MF_INCREMENT  = 0xC1
   _PICC_MF_RESTORE    = 0xC2

   _MAX_BLK = 0xFF

   _AUX_SPI=(1<<8)

   _debug = DBG_OFF

   def __init__(self, pi, channel=SPI_CE0, speed=8e6):
      """
      Instantiate with the Pi to which the card reader is connected.

      Optionally the SPI channel may be specified.  The default is
      main SPI channel 0.

      The following constants may be used to define the channel:

         RC522.SPI_CE0      - main SPI channel 0
         RC522.SPI_CE1      - main SPI channel 1
         RC522.AUX_SPI_CE0  - aux  SPI channel 0
         RC522.AUX_SPI_CE1  - aux  SPI channel 1
         RC522.AUX_SPI_CE2  - aux  SPI channel 2

      Optionally the SPI speed in bps (bits per second) may be
      specified.  The default is 8 Mbps.
      """
      assert SPI_CE0 <= channel <= AUX_SPI_CE2
      assert 32000 <= speed <= 125e6

      self.pi = pi

      if channel < AUX_SPI_CE0:
         self.h = pi.spi_open(channel, int(speed))
      else:
         self.h = pi.spi_open(
            channel - AUX_SPI_CE0, int(speed), _AUX_SPI)

      self._PCDInit()

   #_util

   def _utilUpdateCrc(self, ch, crc):
      """
      Adds a new byte to the CRC calculation.
      """
      ch = (ch^crc) & 0xFF
      ch = (ch^(ch<<4)) & 0xFF
      crc = (crc >> 8)^(ch << 8)^(ch<<3)^(ch>>4)
      return crc & 0xFFFF

   def _utilComputeCrc(self, data):
      """
      Generates the CRC for the data bytes.
      """
      wCrc = 0x6363 # ITU-V.41

      for ch in data:
         wCrc = self._utilUpdateCrc(ch, wCrc)

      return [wCrc & 0xFF, (wCrc >> 8) & 0xFF]

   # _PCD

   def _PCDWrite(self, reg, val):
      """
      Write val to PCD register reg.
      """
      self.pi.spi_write(self.h, [reg, val])

   def _PCDRead(self, reg):
      """
      Returns the byte read from PCD register reg.
      """
      (c, b) = self.pi.spi_xfer(self.h, [reg|0x80, 0])
      return b[1]

   def _PCDWriteFIFO(self, data):
      """
      Adds data to the PCD FIFO.
      """
      self.pi.spi_write(self.h, [self._FIFODataReg] + data)

   def _PCDReadFIFO(self, count):
      """
      Reads count bytes from the PCD FIFO.
      """
      (c, b) = self.pi.spi_xfer(self.h, [self._FIFODataReg|0x80]*count + [0])
      return list(b[1:])

   def _PCDSetBitMask(self, reg, mask):
      """
      Sets mask bits in PCD register reg.
      """
      tmp = self._PCDRead(reg)
      self._PCDWrite(reg, tmp | mask)

   def _PCDClearBitMask(self, reg, mask):
      """
      Clears mask bits in PCD register reg.
      """
      val = self._PCDRead(reg)
      tmp = val & (~mask)
      if tmp != val:
         self._PCDWrite(reg, tmp)

   def _PCDAntennaOn(self):
      """
      Switches the PCD antenna on.
      """
      temp = self._PCDRead(self._TxControlReg)
      if (temp & 0x03) != 0x03:
         self._PCDSetBitMask(self._TxControlReg, 0x03)

   def _PCDAntennaOff(self):
      """
      Switches the PCD antenna off.
      """
      self._PCDClearBitMask(self._TxControlReg, 0x03)

   def _PCDInit(self):
      """
      Initialises the 
      """

      self._RC522SoftReset()

      self._PCDWrite(self._TModeReg,      0x80)
      self._PCDWrite(self._TPrescalerReg, 0xA9)
      self._PCDWrite(self._TReloadRegH,   0x03)
      self._PCDWrite(self._TReloadRegL,   0xe8)

      self._PCDWrite(self._TxASKReg,      0x40)
      #self._PCDWrite(self._ModeReg,       0x3D)
      self._PCDWrite(self._ModeReg,       0x29)
      self._PCDAntennaOn()

   # _RC522

   def _RC522Idle(self):
      """
      Cancel any command in progress.
      """
      self._PCDWrite(self._CommandReg, self._PCD_Idle)

   def _RC522Mem(self, data=None):
      """
      Reads or writes 25 bytes to the PCD internal buffer.

      If data is None the PCD internal buffer is read otherwise
      data is written to the PCD internal buffer.
      """
      self._PCDSetBitMask(self._FIFOLevelReg, 0x80) # Clear FIFO.

      if data is not None:
         self._PCDWriteFIFO(data) # Fill FIFO with data to be written.
         self._PCDWrite(self._CommandReg, self._PCD_Mem)
      else:
         self._PCDWrite(self._CommandReg, self._PCD_Mem)
         return self._PCDReadFIFO(25)

   def _RC522GenerateRandomID(self):
      """
      Generates a 10 byte random ID and stores it in the PCD internal
      buffer.
      """
      self._PCDWrite(self._CommandReg, self._PCD_GenerateRandomID)

   def _RC522CalcCRC(self, data):
      """
      Generates the CRC for the data bytes using the 
      """
      self._PCDSetBitMask(self._FIFOLevelReg, 0x80) # Clear FIFO.

      self._PCDWriteFIFO(data) # Fill FIFO with data to be CRC'd .

      self._PCDClearBitMask(self._DivIrqReg, 0x04) # Clear CRC calculated bit.

      self._PCDWrite(self._CommandReg, self._PCD_CalcCRC) # Start CRC.

      timeout = time.time() + 0.1 # 100 milliseconds timeout

      while True:

         n = self._PCDRead(self._DivIrqReg) # Check to see if CRC ready.

         if n & 0x04: # Exit loop if CRC ready.
            break

         if time.time() > timeout:
            return [255, 255]

      return [self._PCDRead(self._CRCResultRegL),
              self._PCDRead(self._CRCResultRegM)]

   def _RC522Transceive(self, cmdData, CRC=True):
      """
      """
      if CRC:
         crc = self._utilComputeCrc(cmdData)
         cmdData += crc

      if self._debug >= DBG_MIN:
         print("_RC522Transceive< {}".format(cmdData))

      irqEn = 0x77
      waitIRq = 0x30

      self._RC522Idle()

      self._PCDWrite(self._ComlEnReg, irqEn|0x80)

      self._PCDWrite(self._CommIrqReg, 0x7F)

      self._PCDSetBitMask(self._FIFOLevelReg, 0x80) # Clear FIFO.

      self._PCDWriteFIFO(cmdData) # Fill FIFO with command.

      self._PCDWrite(self._CommandReg, self._PCD_Transceive) # Set command.

      # Start Tranceive command by setting StartSend bit
      self._PCDSetBitMask(self._BitFramingReg, 0x80)

      timeout = time.time() + 0.04 # 40 milliseconds hard timeout

      status = OK

      data = []
      bits = 0

      while True:

         n = self._PCDRead(self._CommIrqReg)

         if n & waitIRq:
            break

         if n & 1:
            status = ERR_TIMEOUT_1
            break

         if time.time() > timeout:
            status = ERR_TIMEOUT_2
            break

      self._PCDClearBitMask(self._BitFramingReg, 0x80)

      if status != OK:

         if self._debug >= DBG_MIN:
            print("_RC522Transceive> {} {} {}".format(status, data, bits))

         return status, data, bits

      if (self._PCDRead(self._ErrorReg) & 0x1B) == 0x00:

         if n & irqEn & 1:
            status = ERR_NO_TAG

         n = self._PCDRead(self._FIFOLevelReg)

         lastBits = self._PCDRead(self._ControlReg) & 0x07

         if lastBits != 0:
            bits = (n-1)*8 + lastBits
         else:
            bits = n*8

         data = self._PCDReadFIFO(n)

      else:
         status = ERR_UNKNOWN

      if self._debug >= DBG_MIN:
         print("_RC522Transceive> {} {} {}".format(status, data, bits))

      return status, data, bits

   def _RC522MFAuthent(self, blockAddr, cmd, key, UID):
      """
      """
      buf = [cmd, blockAddr] + key + UID[:4]

      if self._debug >= DBG_MIN:
         print("_RC522MFAuthent< {}".format(buf))

      self._RC522Idle()

      self._PCDSetBitMask(self._FIFOLevelReg, 0x80) # Clear FIFO.

      self._PCDWriteFIFO(buf) # Fill FIFO with command data.

      self._PCDWrite(self._CommandReg, self._PCD_Authent) # Start command.

      timeout = time.time() + 0.04 # 40 milliseconds hard timeout

      while True:

         n = self._PCDRead(self._Status2Reg)

         if n & 0x08:
            status = OK
            break

         n = self._PCDRead(self._CommIrqReg)

         if n & 1:
            status = ERR_TIMEOUT_1
            break

         if time.time() > timeout:
            status = ERR_TIMEOUT_2
            break

      if status != OK: # one last try.

         n = self._PCDRead(self._Status2Reg)

         if n & 0x08:
            status = OK

      if self._debug >= DBG_MIN:
         print("_RC522MFAuthent> {}".format(status))

      return status

   def _RC522SoftReset(self):
      """
      Resets the 
      """
      self._PCDWrite(self._CommandReg, self._PCD_SoftReset)
      time.sleep(0.05) # allow 50 milliseconds

   # _MF

   def _MFIncDecRes(self, command,  blockAddr, value):
      """
      A helper function for the increment, decrement, and
      restore value block commands.

      Returns a status (OK on success).
      """
      buf = [command] + [blockAddr]

      (status, data, bits) = self._RC522Transceive(buf)

      if status != OK:
         return status

      buf = [0]*4
      buf[0] =  value      & 0xff
      buf[1] = (value>>8)  & 0xff
      buf[2] = (value>>16) & 0xff
      buf[3] = (value>>24) & 0xff

      status, data, bits = self._RC522Transceive(buf)

      if (status == ERR_TIMEOUT_1) or (status == ERR_TIMEOUT_2):
         status = OK

      return status

   def _MFRead(self, blockAddr):
      """
      Reads a specified block from the card.

      Returns a status (OK on success) and the 16 bytes of the block.
      """
      buf = [self._PICC_MF_READ, blockAddr]

      status, data, bits = self._RC522Transceive(buf)

      if bits == 144: # data + CRC
         crc = self._utilComputeCrc(data)
         if crc[0] or crc[1]:
            status = ERR_BAD_CRC
      else:
         status = ERR_BAD_LEN

      return status, data[:16]

   def _MFWrite(self, blockAddr, block):
      """
      Writes 16 bytes to a specified block of the card.

      Returns a status (OK on success).
      """
      buf = [self._PICC_MF_WRITE, blockAddr]

      status, data, bits = self._RC522Transceive(buf)

      if ((status != OK) or
          (bits != 4) or
          ((data[0] & 0x0F) != 0x0A)):
         status = ERR_UNKNOWN

      if status == OK:

         buf = block[:]

         status, data, bits = self._RC522Transceive(buf)

         if ((status != OK) or
             (bits != 4) or
             ((data[0] & 0x0F) != 0x0A)):
            status = ERR_UNKNOWN

      return status

   def _MFIncrement(self, blockAddr, val):
      """
      Adds val to the value stored in a value block.

      Returns a status (OK on success).
      """
      status = self._MFIncDecRes(self._PICC_MF_INCREMENT, blockAddr, val)

      if status == OK:
         status = self._MFTransfer(blockAddr)

      return status

   def _MFDecrement(self, blockAddr, val):
      """
      Subtracts val from the value stored in a value block.

      Returns a status (OK on success).
      """
      status = self._MFIncDecRes(self._PICC_MF_DECREMENT, blockAddr, val)

      if status == OK:
         status = self._MFTransfer(blockAddr)

      return status

   def _MFRestore(self, blockAddr):
      """
      Copies a value block from the card to internal volatile memory.

      Returns a status (OK on success).
      """
      return self._MFIncDecRes(self._PICC_MF_RESTORE, blockAddr, 0)

   def _MFTransfer(self, blockAddr):
      """
      Copies a value block from internal volatile memory to the card.

      Returns a status (OK on success).
      """
      buf = [self._PICC_MF_TRANSFER, blockAddr]

      status, data, bits = self._RC522Transceive(buf)

      return status

   # Public

   def ISO_Request(self):
      """
      Checks to see if a card is in range.

      Returns a tuple of status (OK on success) and the cards ATQA.
      """
      self._PCDWrite(self._BitFramingReg, 0x07)

      status, data, bits = self._RC522Transceive([self._PICC_REQA], CRC=False)

      if status != OK:
         ATQA = 0
      else:
         if bits != 16:
            status = ERR_UNKNOWN
            ATQA = 0
         else:
            ATQA = data[0] + (data[1]<<8)

      return status, ATQA

   def ISO_Anticollision(self):
      """
      Deselects all but one card in range.

      Returns a tuple of status (OK on success) and the UID of the
      active card in range.
      """

      command = [self._PICC_SEL_CL1, 0x20]

      self._PCDWrite(self._BitFramingReg, 0x00)

      status, data, bits = self._RC522Transceive(command, CRC=False)

      if status == OK:
         i = 0
         if len(data) == 5:
            uidCheck = 0
            while i<4:
               uidCheck = uidCheck ^ data[i]
               i += 1
            if uidCheck != data[i]:
               status = ERR_UNKNOWN
         else:
            status = ERR_UNKNOWN

      return status, data

   def ISO_Select(self, UID):
      """
      Selects the active tag in range by its UID (including the BCC
      byte).

      Returns a tuple of status (OK on success) and the cards SAK.
      """
      assert len(UID) == 5

      buf = [self._PICC_SEL_CL1, 0x70] + UID

      status, data, bits = self._RC522Transceive(buf)

      if (status == OK) and (bits == 24):
         return OK, data[0]
      else:
         return ERR_UNKNOWN, 0

   def ISO_Authenticate(self, blockAddr, keyId, key, UID):
      """
      Authenticates access to a block.

      The keyId must be one of the constants:

         KEY_A
         KEY_B

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK
      assert KEY_A <= keyId <= KEY_B
      assert len(key) == 6
      assert 4 <= len(UID) <= 5

      if keyId == KEY_A:
         cmd = self._PICC_MF_AUTH_KEY_A
      else:
         cmd = self._PICC_MF_AUTH_KEY_B

      return self._RC522MFAuthent(blockAddr, cmd, key, UID)

   def ISO_StopCrypto(self):
      """
      Releases a card.
      """
      self._PCDClearBitMask(self._Status2Reg, 0x08)

   def MF_ReadBlock(self, blockAddr):
      """
      Reads a block from the card.

      Returns a tuple of status (OK on success) and the 16-byte block.
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK

      return self._MFRead(blockAddr)

   def MF_WriteBlock(self, blockAddr, block):
      """
      Writes a block to the card.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK
      assert len(block) == 16

      return self._MFWrite(blockAddr, block)

   def MF_IncrementBlock(self, blockAddr, val):
      """
      Adds val to the value stored in a value block.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK
      assert val >= 0

      return self._MFIncrement(blockAddr, val)

   def MF_DecrementBlock(self, blockAddr, val):
      """
      Subtracts val from the value stored in a value block.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK
      assert val >= 0

      return self._MFDecrement(blockAddr, val)

   def MF_RestoreBlock(self, blockAddr):
      """
      Reads a value block into card volatile memory.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK

      return self._MFRestore(blockAddr)

   def MF_TransferBlock(self, blockAddr):
      """
      Writes a value block from card volatile memory.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK

      return self._MFTransfer(blockAddr)

   def MF_SetValue(self, blockAddr, val):
      """
      Formats a block as a value block with the value val and
      writes the block to the card.

      Returns a status (OK on success).
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK
      assert val >= 0

      blk = [0]*16

      blk[0] = (val &       0xFF)
      blk[1] = (val &     0xFF00) >> 8
      blk[2] = (val &   0xFF0000) >> 16
      blk[3] = (val & 0xFF000000) >> 24

      blk[8] = blk[0]
      blk[9] = blk[1]
      blk[10] = blk[2]
      blk[11] = blk[3]

      blk[4] = ~blk[0]&0xFF
      blk[5] = ~blk[1]&0xFF
      blk[6] = ~blk[2]&0xFF
      blk[7] = ~blk[3]&0xFF

      blk[12] = blockAddr
      blk[13] = ~blockAddr&0xFF

      blk[14] = blockAddr
      blk[15] = ~blockAddr&0xFF

      return self._MFWrite(blockAddr, blk)

   def MF_GetValue(self, blockAddr):
      """
      Reads a value block from the card and returns its value
      (this function assumes the block is a valid value block).

      Returns a tuple of status (OK on success) and the 32-bit value.
      """
      assert 0 <= blockAddr <= PCD._MAX_BLK

      status, data = self._MFRead(blockAddr)

      if status == OK:
         value = data[3]<<24 | data[2]<<16 | data[1]<<8 | data[0]
      else:
         value = 0

      return status, value

   def Util_JoinAccessBits(self, b0, b1, b2, st):
      """
      Constructs the access bits needed for a combination
      of block and sector trailer permissions.

      b0-b2 define the permissions for data blocks 0-2 of the
      sector according to the following table:

         R    W    I    DTR
      0  AB   AB   AB   AB  value (default)
      1  AB   -    -    AB  value
      2  AB   -    -    -   data
      3  B    B    -    -   data
      4  AB   B    -    -   data
      5  B    -    -    -   data
      6  AB   B    B    AB  value
      7  -    -    -    -

      st defines the permissions for the sector trailer of the
      sector according to the following table:

          KeyA   Access   KeyB
          R  W   R    W   R  W
      0   -  A   A    -   A  A
      1   -  A   A    A   A  A (default)
      2   -  -   A    -   A  -
      3   -  B   AB   B   -  B
      4   -  B   AB   -   -  B
      5   -  -   AB   B   -  -
      6   -  -   AB   -   -  -
      7   -  -   AB   -   -  -
      """
      assert 0 <= b0 <= 7
      assert 0 <= b1 <= 7
      assert 0 <= b2 <= 7
      assert 0 <= st <= 7

      c1 = ((st&4) << 1) | ((b2&4) << 0) | ((b1&4) >> 1) | ((b0&4) >> 2)
      c2 = ((st&2) << 2) | ((b2&2) << 1) | ((b1&2) << 0) | ((b0&2) >> 1)
      c3 = ((st&1) << 3) | ((b2&1) << 2) | ((b1&1) << 1) | ((b0&1) << 0)

      ab0 = (~c2 & 0xF) << 4 | (~c1 & 0xF)
      ab1 =          c1 << 4 | (~c3 & 0xF)
      ab2 =          c3 << 4 | c2

      return [ab0, ab1, ab2]

   def Util_SplitAccessBits(self, accessBits):
      """
      Converts the three access bits bytes of the sector trailer to
      the individual permissions for each block of the sector.

      Returns a tuple of status (OK on success) and the
      permissions for blocks 0, 1, 2, and 3 of the sector.
      """
      assert len(accessBits) == 3

      c1  = accessBits[1] >> 4
      c2  = accessBits[2] & 0xF
      c3  = accessBits[2] >> 4
      c1_ = accessBits[0] & 0xF
      c2_ = accessBits[0] >> 4
      c3_ = accessBits[1] & 0xF

      b0 = ((c1 & 1) << 2) | ((c2 & 1) << 1) | ((c3 & 1) << 0);
      b1 = ((c1 & 2) << 1) | ((c2 & 2) << 0) | ((c3 & 2) >> 1);
      b2 = ((c1 & 4) << 0) | ((c2 & 4) >> 1) | ((c3 & 4) >> 2);
      st = ((c1 & 8) >> 1) | ((c2 & 8) >> 2) | ((c3 & 8) >> 3);

      if (c1 == (~c1_&0xF)) and (c2 == (~c2_&0xF)) and (c3 == (~c3_&0xF)):
         status = OK
      else:
         status = ERR_BAD_ACCESS_BITS

      return status, b0, b1, b2, st

   def Util_JoinSectorTrailer(self, keyA, keyB, accessBits, GPB):
      """
      Returns a 16-byte sector trailer formed from key A, key B,
      the access bits, and the GPB (General Purpose Byte).
      """
      assert len(keyA) == 6
      assert len(keyB) == 6
      assert len(accessBits) == 3
      assert 0 <= GPB <= 255

      return keyA + accessBits + [GPB] + keyB

   def Util_SplitSectorTrailer(self, block):
      """
      Takes a 16 byte sector trailer and returns a tuple of

         key A                          - bytes 0-5
         key B                          - bytes 10-15
         the access bits                - bytes 6-8
         the GPB (General Purpose Byte) - byte 9

      If the block was read from the card Key A will always be all
      zeros.
      """
      assert len(block) == 16

      return block[0:6], block[10:16], block[6:9], block[9]

   def Util_RC522ReadMem(self):
      """
      Returns the 25-byte PCD internal buffer.
      """
      return self._RC522Mem()

   def Util_RC522WriteMem(data):
      """
      Writes the 25-byte PCD internal buffer.
      """
      assert len(data) == 25

      self._RC522Mem(data)

   def Util_RC522GenerateRandomID(self):
      """
      Returns a PCD generated 10-byte random ID.
      """
      self._RC522GenerateRandomID() # Generate the random ID.
      data = self._RC522Mem() # Read internal buffer.

      return data[2:5] + data[8:14] + [data[24]]


   def Util_SetDebugLevel(self, level):
      """
      This function enables or disables internal debug diagnostics.

      The level may be one of the constants:

         DBG_OFF
         DBG_MIN
         DBG_MAX
      """
      assert DBG_OFF <= level <= DBG_MAX

      self._debug = level

   def stop(self):
      """
      Closes the connection to the 
      """
      self._RC522SoftReset()

      self._PCDAntennaOff()

      self.pi.spi_close(self.h)
