/*
 * debug:
 *	Debugging help for the Gerduino m48p
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

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/power.h>

#include "wiring.h"
#include "rtc.h"
#include "serial.h"
#include "irda.h"
#include "debug.h"

#include "m48.h"


/*
 * debugKey:
 *	Provide some sort of debugging via keyboard entry
 *********************************************************************************
 */

void debugKey (void)
{
#ifdef	DEBUG_KEYBOARD
  uint8_t i ;
  register uint8_t key ;

  if (!serialKeypressed ())
    return ;

  key = serialGetchar () ;

#ifdef	DEBUG_CLOCK_REGS
  if (key == 'r')
  {
    serialPuts (PSTR ("Read\nInt: ")) ;
    for (i = 0 ; i < sizeof (rtc) ; ++i)
    {
      serialPutchar (' ') ;
      serialPrHex8 (rtc [i]) ;
    }
    serialPuts (PSTR ("\nExt: ")) ;
    for (i = 0 ; i < sizeof (rtc) ; ++i)
    {
      serialPutchar (' ') ;
      serialPrHex8 (extRtc [i]) ;
    }
    serialPuts (PSTR ("\nAlm: ")) ;
    for (i = 0 ; i < sizeof (rtc) ; ++i)
    {
      serialPutchar (' ') ;
      serialPrHex8 (almRtc [i]) ;
    }
    serialNewline ()  ;
    return ;
  }
#endif

#ifdef	DEBUG_IR_CODE
  if (key == 'i')
  {
    serialPuts (PSTR ("\nCode: ")) ;
    serialPrHex16 (irdaCode) ;
    serialNewline () ;
  }
  else
#endif

    serialPutchar ('?') ;
#endif
}


/*
 * debugShutdown:
 *	Make the debug system as low-power as possible
 *********************************************************************************
 */

void debugShutdown (void)
{
#ifdef	DEBUG_MAINS_LED
  pinMode (DEBUG_MAINS_LED, INPUT) ;	digitalWrite (DEBUG_MAINS_LED, 0) ;
#endif
#ifdef	DEBUG_TWI_LED
  pinMode (DEBUG_TWI_LED, INPUT) ;	digitalWrite (DEBUG_TWI_LED, 0) ;
#endif
#ifdef	DEBUG_RTC_LED
  pinMode (DEBUG_RTC_LED, INPUT) ;	digitalWrite (DEBUG_RTC_LED, 0) ;
#endif
#ifdef	DEBUG_WAKE_LED
  pinMode (DEBUG_WAKE_LED, INPUT) ;	digitalWrite (DEBUG_WAKE_LED, 0) ;
#endif
#ifdef	DEBUG_IRDA_LED
  pinMode (DEBUG_IRDA_LED, INPUT) ;	digitalWrite (DEBUG_IRDA_LED, 0) ;
#endif
}

/*
 * debugInit:
 *	Initialise the digital outputs for the various LED functions
 *********************************************************************************
 */

void debugInit (void)
{
#ifdef	DEBUG_MAINS_LED
  pinMode (DEBUG_MAINS_LED, OUTPUT) ;	digitalWrite (DEBUG_MAINS_LED, 1) ;	// 1 is on the mains
#endif
#ifdef	DEBUG_TWI_LED
  pinMode (DEBUG_TWI_LED, OUTPUT) ;	digitalWrite (DEBUG_TWI_LED, 0) ;	// 1 is a general error
#endif
#ifdef	DEBUG_RTC_LED
  pinMode (DEBUG_RTC_LED, OUTPUT) ;	digitalWrite (DEBUG_RTC_LED, 0) ;	// Blinky
#endif
#ifdef	DEBUG_WAKE_LED
  pinMode (DEBUG_WAKE_LED, OUTPUT) ;	digitalWrite (DEBUG_WAKE_LED, 0) ;	// 1 when alarm goes off
#endif
#ifdef	DEBUG_IRDA_LED
  pinMode (DEBUG_IRDA_LED, OUTPUT) ;	digitalWrite (DEBUG_IRDA_LED, 0) ;	// 1 when a code decoded
#endif
}
