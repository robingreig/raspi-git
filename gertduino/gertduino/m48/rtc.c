/*
 * rtc:
 *	The RTC code for the ATmega48p on the Gertduino.
 *
 * This code is emulating a DS1374 internally (mostly)
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

#include <stdint.h>
#include <string.h>

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <avr/power.h>

#include "m48.h"
#include "wiring.h"

#include "rtc.h"

// Today, we're emulating the DS1374
//	This has a 32-bit timer and a count-down alarm timer which
//	we (and Linux) are not going to use.
//	Instead, we'll create a 2nd I2C device to use as the
//	wakeup device - which we can't use directly in Linux, but
//	hey ho..

uint8_t rtc    [RTC_SIZE] ;
uint8_t almRtc [RTC_SIZE] ;
uint8_t extRtc [RTC_SIZE] ;


/*
 * TIMER2_OVF_vect:
 *	This gets called when timer 2 overflows. This is driven by the
 *	32768Hz xtal and the dividers are normally set such that it overflows
 *	once a second.
 *
 *	This ISR is allowed to be pre-empted by other interrupt sources
 *	(mostly the I2C code)
 *********************************************************************************
 */

ISR(TIMER2_OVF_vect, ISR_NOBLOCK)
{
#ifdef	DEBUG_RTC_LED
  digitalWrite (DEBUG_RTC_LED, digitalRead (DEBUG_RTC_LED) ^ 1) ;
#endif

  if (++rtc [0] == 0)
    if (++rtc [1] == 0)
      if (++rtc [2] == 0)
	++rtc [3] ;

// Time to wake up?

  if (memcmp (&rtc [0], &almRtc [0], 4) == 0)
  {
    almRtc [0] = almRtc [1] = almRtc [2] = almRtc [3] = 0 ;
    wakeUpPi () ;
  }

// Time to powerdown ?

  if (memcmp (&rtc [0], &almRtc [4], 4) == 0)
  {
    almRtc [4] = almRtc [5] = almRtc [6] = almRtc [7] = 0 ;
    powerDownPi () ;
  }

}


/*
 * rtcInit:
 *	Initialise what we need to do for the RTC
 *********************************************************************************
 */

static const uint8_t PROGMEM fancyThat [] =		// Someone might run i2cdump ;-)
{
  0x00, 0x00, 0x00, 0x00,	// Wakeup
  0x00, 0x00, 0x00, 0x00,	// Powerdown
  0xBA, 0xBE, 0xCA, 0xFE,
  0xFE, 0xED, 0xBE, 0xEF,
} ;

void rtcInit (void)
{
  register int i ;

  power_timer2_enable () ; delay (1) ;

  for (i = 0 ; i < sizeof (rtc) ; ++i)
    almRtc [i] = pgm_read_byte (&fancyThat [i]) ;

// Setup Timer2

  TCCR2A = 0x00 ;			// Normal mode
  TCCR2B = _BV(CS22 ) | _BV(CS20) ;	// Divide by 128 -> overflow every 256 counts = 1 per second.
  ASSR   = _BV(AS2) ;			// Enable asynchronous operation - clock from xtal
  TIMSK2 = _BV(TOIE2) ;			// Enable the timer 2 interrupt

#ifdef	DEBUG_RTC_LED
  digitalWrite (DEBUG_RTC_LED, 1) ;
#endif

#ifdef	DEBUG_WAKE_LED
  digitalWrite (DEBUG_WAKE_LED, 0) ;
#endif
}
