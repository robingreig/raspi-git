#!/usr/bin/env python

import time
import pigpio

def key2str(key):
   return "".join("{:02X}".format(c) for c in key)

def str2key(keystr):
   return [int(keystr[x:x+2],16) for x in range(0,12,2)]

def generateKey():
   k = os.urandom(6)
   key = []
   for c in k:
      key.append(ord(c))
   return key2str(key)

STB=7

def card_present(obj):

   ATQA=0
   UID=[]
   SAK=0

   status = RC522.ERR_NO_TAG
   timeout = time.time() + 5

   while status != RC522.OK and time.time() < timeout:

      obj.ISO_StopCrypto()

      status, ATQA = obj.ISO_Request()

      if status == RC522.OK:
         print("Card request, ATQA={}".format(ATQA))
         status, UID = obj.ISO_Anticollision() # Get the UID of the card
         if status == RC522.OK:
            print("Card anticollision, UID=[{}, {}, {}, {}]".
               format(UID[0], UID[1], UID[2], UID[3]))
            status, SAK = obj.ISO_Select(UID)
            if status == RC522.OK:
               print("Card select, SAK={}".format(SAK))
            else:
               print("Card select failed,")
         else:
            print("Card anticollision failed,")
      else:
         print("Card request failed,")

   return status, ATQA, UID, SAK

def card_wipe(obj, keyA):

   keyD = [255]*6
   blockD = [0]*16

   status, ATQA, UID, SAK = card_present(obj)

   if status == RC522.OK:

      # Authenticate sector trailer

      status = obj.ISO_Authenticate(STB, RC522.KEY_A, keyA, UID)

      if status == RC522.OK: # Check if authenticated.

         print("authenticated with key A")

         # Set default keys and access bits.

         AB = obj.Util_JoinAccessBits(0, 0, 0, 1)

         block = obj.Util_JoinSectorTrailer(keyD, keyD, AB, 0)

         status = obj.MF_WriteBlock(STB, block)

         if status == RC522.OK:

            print("new st written okay")

            # Authenticate sector trailer against default keys

            status = obj.ISO_Authenticate(STB, RC522.KEY_A, keyD, UID)

            if status == RC522.OK:

               for i in range(STB-3, STB):
                  status = obj.MF_WriteBlock(i, blockD)
                  if status == RC522.OK:
                     print("block {} cleared ok".format(i))
                  else:
                     print("*** block {} not cleared ok".format(i))

            else:
               print("*** authentication error with default keys")
         else:
            print("*** write ST failed with old keys")
      else:
         print("*** authentication error with old keys")
   else:
      print("*** card not present")

   return status


def card_read_AB(obj, keyA, keyB):

   status, ATQA, UID, SAK = card_present(obj)

   answer = ""

   if status == RC522.OK:

      # Authenticate sector trailer

      status = obj.ISO_Authenticate(STB, RC522.KEY_A, keyA, UID)

      if status == RC522.OK: # Check if authenticated.

         print("authenticated sector trailer with key A")

         status, block = obj.MF_ReadBlock(STB)

         answer = str(block)

         print(block)

         status = obj.ISO_Authenticate(STB-3, RC522.KEY_B, keyB, UID)

         if status == RC522.OK: # Check if authenticated.

            print("authenticated data blocks with key B")

            for i in range(STB-3, STB):
               status, block = obj.MF_ReadBlock(i)
               answer += "\n" + str(block)
               print(block)
         else:
            print("*** authentication error with key B")
      else:
         print("*** authentication error with key A")
   else:
      print("*** card not present")

   return status, answer

def card_read_B(obj, keyB):

   status, ATQA, UID, SAK = card_present(obj)

   answer = ""

   if status == RC522.OK:

      status = obj.ISO_Authenticate(STB-3, RC522.KEY_B, keyB, UID)

      if status == RC522.OK: # Check if authenticated.

         print("authenticated data blocks with key B")

         s1, v1 = obj.MF_GetValue(STB-3)
         s2, v2 = obj.MF_GetValue(STB-2)
         s3, v3 = obj.MF_GetValue(STB-1)

         answer = "{}:{}\n{}:{}\n{}:{}".format(s1,v1,s2,v2,s3,v3)

         if s1 == RC522.OK and s2 == RC522.OK and s3 == RC522.OK:
            print("blocks read ok")
         else:
            print("*** blocks not read ok")

      else:
         print("*** authentication error with key B")
   else:
      print("*** card not present")

   return status, answer

def card_personalise(obj, keyA, keyB, val1, val2, val3):

   keyD = [255]*6
   blockD = [0]*16

   status, ATQA, UID, SAK = card_present(obj)

   if status == RC522.OK:

      # Authenticate sector trailer with default key

      status = obj.ISO_Authenticate(STB, RC522.KEY_A, keyD, UID)

      if status == RC522.OK: # Check if authenticated.

         print("authenticated with default key")

         s1 = obj.MF_SetValue(STB-3, val1)
         s2 = obj.MF_SetValue(STB-2, val2)
         s3 = obj.MF_SetValue(STB-1, val3)

         if s1 == RC522.OK and s2 == RC522.OK and s3 == RC522.OK:
            print("blocks written ok")
         else:
            print("*** blocks not written ok")

         # Set new keys and access bits.

         AB = obj.Util_JoinAccessBits(5, 3, 6, 1)

         block = obj.Util_JoinSectorTrailer(keyA, keyB, AB, 0)

         status = obj.MF_WriteBlock(STB, block)

         if status == RC522.OK:
            print("new st written okay")
         else:
            print("*** write ST failed with default keys")
      else:
         print("*** authentication error with default keys")
   else:
      print("*** card not present")

   return status

import pigpio
import RC522

pi = pigpio.pi()

if not pi.connected:
   exit()

keyA=[255]*6 # Default key A.
keyB=[255]*6 # Default key B.

cr = RC522.PCD(pi, 0, 50e3) # SPI channel 0

card_read_AB(cr, keyA, keyB)

print("exiting")

cr.stop()

pi.stop()
