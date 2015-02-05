/*
 * twi.c:
 *	Drive the TWI/I2C on the AVR processor.
 *
 * Note: This is a special cut-down version of the driver explicitly
 *	for the ATmega48p on the Gertuino
 *
 * More notes:
 *	This code is stupidly fragile - in that the Raspberry Pi has no
 *	concept of clock stretching... This means that if this code is
 *	slow by another microseconds then bad things will happen on the
 *	Pi. 
 *
 *	Improvements may be possible, but who knows.
 *
 * Copyright (c) 2013 Gordon Henderson <projects@drogon.net>
 ********************************************************************************
 * This file is part of gertduino-m48:
 *	Software to run on the ATmega48p processor on the Gerduino board
 *
 *    This is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    This is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with this.  If not, see <http://www.gnu.org/licenses/>.
 ********************************************************************************
 */

// This version to work with 2 I2C slave devices, so we'll check the
//	TWAR register each time...

#include <stdint.h>
#include <string.h>

#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/power.h>
#include <util/twi.h>

#include "debug.h"
#include "m48.h"
#include "wiring.h"
#include "serial.h"
#include "rtc.h"

#include "twi.h"


/*
 * twiStop:
 * twiReleaseBus:
 * twiAck: twiNak:
 *	Various I2C/TWI bus activity
 *
 */

static inline void twiStop (void)       { TWCR = _BV (TWINT) | _BV (TWEA) | _BV (TWSTO)  | _BV (TWEN) | _BV (TWIE) ; }
static inline void twiReleaseBus (void) { TWCR = _BV (TWINT) | _BV (TWEA) |                _BV (TWEN) | _BV (TWIE) ; }
static inline void twiAck (void)        { TWCR = _BV (TWINT) | _BV (TWEA) |                _BV (TWEN) | _BV (TWIE) ; }
static inline void twiNak (void)        { TWCR = _BV (TWINT) |                             _BV (TWEN) | _BV (TWIE) ; }

/*
 * waitForNextI2Cint:
 *	Wait for the next interrupt to happen, but not for too long
 *********************************************************************************
 */

static inline uint8_t waitForNextI2Cint (void)
{
  int i = 2000 ;
  while ((TWCR & _BV(TWINT)) == 0)
    if (--i == 0)
    {
      twiStop       () ;			// ack and shutdown
      twiReleaseBus () ;
      return 0 ; // timed out )-:
    }

  return 1 ;
}


/*
 * TWI_vect:
 *	handle all interrupts coming back from the hardware.
 *
 * Note: This is now highly specific code designed to handle a very small
 *	subset of the I2C protocol. Just enough for our needs without
 *	incurring too many overheads. The strategy is to take the interrupt
 *	on the first Rx or Tx ACK (after address) coming in, then poll the
 *	bus for the rest of the transaction.
 *	This may stall another interrupt (as ints are OFF at this point in
 *	time!) however if it keeps the Pi happy, then we're OK.
 *********************************************************************************
 */

ISR (TWI_vect)
{
  static   uint8_t  ptr = 0 ;
  register uint8_t  status ;
  register uint8_t  stored ;
  register uint8_t *localRtc ;

  status = TW_STATUS ;			// Read the status register.

  if ((TWDR & 0x02) == 0)		// Primary device
    localRtc = rtc ;
  else					// Secondary device
    localRtc = almRtc ;

// This is the most bizarre thing, but without this, the system will
//	sometimes return data with the top-bit set. Most of the time.

  delayMicroseconds (1) ;

  /**/ if (status == TW_SR_SLA_ACK)	// Start of a Slave Recieve sequence
  {
    twiAck () ;
    ptr = 0xFF ;				// Marker value
    memcpy (extRtc, localRtc, RTC_SIZE) ;	// Snapshot internal version
    stored = 0 ;
    for (;;)
    {
      if (waitForNextI2Cint () == 0)
	return ;
      if (TW_STATUS == TW_SR_DATA_ACK)
      {
	twiAck () ;
	if (ptr == 0xFF)			// Initialise ptr
	  ptr = TWDR & (RTC_SIZE - 1) ;
	else					// Store data @ ptr
	{
	  extRtc [ptr] = TWDR ;
	  ptr = (ptr + 1) & (RTC_SIZE - 1) ;
	  ++stored ;
	}
      }
      else
      {
	twiStop       () ;			// ack and shutdown
	twiReleaseBus () ;
	if (stored != 0)			// If we recieved anything from the Pi, then
	  memcpy (localRtc, extRtc, RTC_SIZE) ;	//	copy it back to the working version
	return;
      }
    }
  }
  else if (status == TW_ST_SLA_ACK)	// Start of a Slave Transmit sequence
  {
    memcpy (extRtc, localRtc, RTC_SIZE) ;	// Snapshot internal version
    do
    {
      TWDR = extRtc [ptr] ;
      twiAck () ;
      ptr = (ptr + 1) & (RTC_SIZE - 1) ;
      if (waitForNextI2Cint () == 0)
	return ;
    } while (TW_STATUS == TW_ST_DATA_ACK) ;
    twiStop       () ;				// ack and shutdown
    twiReleaseBus () ;
  }
  else					// Unknown status
  {
    twiStop       () ;
    twiReleaseBus () ;
#ifdef	DEBUG_TWI_LED
    digitalWrite (DEBUG_TWI_LED, 1) ;
#endif
  }

}


/*
 * twiShutdown:
 *	Shutdown the TWI/I2C hardware in an orderly manner for sleep mode
 *********************************************************************************
 */

void twiShutdown (void)
{
  twiStop           () ;
  twiReleaseBus     () ;
  TWCR &= ~_BV(TWEN) ;
  power_twi_disable () ;
}


/* 
 * twiInit:
 *	Get the hardware ready for TWI operations
 *********************************************************************************
 */

void twiInit (uint8_t address, uint8_t mask)
{
  power_twi_enable () ; delay (1) ;

  TWSR  = 0 ;
  TWBR  = 0 ;
  TWAR  = address << 1 ;
  TWAMR = mask    << 1 ;
  TWCR  = _BV(TWEN) | _BV(TWIE) | _BV(TWEA) ;

  twiStop       () ;
  twiReleaseBus () ;

#ifdef	DEBUG_TWI_LED
  digitalWrite (DEBUG_TWI_LED, 0) ;
#endif
}
