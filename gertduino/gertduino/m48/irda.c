/*
 * irda:
 *	Infra red reciever code.
 *
 * Strategy:
 *	* Set timer0 as a free-running timer with a small interval.
 *		(prescaler at 256 is an increment of 32µS)
 *	* Set the IRDA sensor to trigger on a falling interrupt.
 *		(Detector chip is active low)
 *	* Wait
 *
 *	On a Falling or Rising interrupt, check the timer0 value and
 *	store this for later processing.
 *	Re-program the interrupt for the next edge direction.
 *
 *	Meanwhile if the timer0 overflows, we've probably run out of IRDA
 *	pulses, so calculate the buffer and work out the code.
 *
 * Note: The sensor used is the TSOP38236. This has an active LOW output.
 *	(it's not that important, but...)
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
#include "rtc.h"
#include "wiring.h"
#include "serial.h"
#include "debug.h"

#include "irdaSettings.h"
#include "irda.h"

uint8_t  codeTimes [64] ;
uint16_t irdaCode ;
uint16_t irdaCount ;

static volatile uint8_t expectingRising ;
static volatile uint8_t startOfCode ;
static volatile uint8_t timesPtr ;
static volatile uint8_t readingCode ;

// Inline functions to fiddle with the Int1 edge detections

static void inline setInt1Rising (void)
  { EICRA = _BV (ISC11) | _BV (ISC10) ; }

static void inline setInt1Falling (void)
  { EICRA = _BV (ISC11) | _BV (ISC10) ; }

static void inline setInt1Off (void)
  { EIMSK &= ~_BV (INT1) ; }


/*
 * decodeCode:
 *	This is the heart of it all - sort of.
 *	We scan the buffer of times and based on the timings set for a particular
 *	controller, we calculate the code value.
 *	This uses the data held in irdaSetings.h
 *********************************************************************************
 */

static void decodeCode (void)
{
  uint16_t myCode = 0 ;
  uint8_t  ptr    = 0 ;
  uint8_t  t ;

#ifdef	DISCOVERY_MODE
  uint8_t i ;
  serialPuts (PSTR ("\nTimes: ")) ;
  for (i = 0 ; i < CODE_STORE_SIZE ; ++i)
  {
    if ((i % 16) == 0)
    {
      serialNewline () ;
      serialPrHex8 (i) ;
      serialPuts (PSTR (": ")) ;
    }
    serialPrHex8 (codeTimes [i]) ;
    serialPutchar (' ') ;
  }
   serialNewline () ;
#endif

  if ((START_BIT != 0) && (codeTimes [0] >= START_BIT))
    ptr = 1 ;

  ptr += SKIP_BITS ;

  while ((t = codeTimes [ptr++]) != 0)
  {
    if (t >= HIGH_BIT)
      myCode |= 1 ;

    if (ptr == CODE_STORE_SIZE)
      break ;

    myCode <<= 1 ;
  }

  if (myCode != 0)
  {
    irdaCode = myCode ;
    ++irdaCount ;
    almRtc [ 8] = (irdaCode  >> 8) & 0xFF ;
    almRtc [ 9] = (irdaCode  >> 0) & 0xFF ;
    almRtc [10] = (irdaCount >> 8) & 0xFF ;
    almRtc [11] = (irdaCount >> 0) & 0xFF ;
 
#ifdef	DISCOVERY_MODE
    serialPuts (PSTR ("Code: ")) ;
    serialPrHex16 (irdaCode) ;
    serialNewline () ;
#endif
  }

  memset (codeTimes, 0, CODE_STORE_SIZE) ;
  timesPtr    = 0 ;
  startOfCode = TRUE ;
}


/*
 * INT1_vect:
 *	Handle the edge triggered interrupt from the IR detector
 *********************************************************************************
 */

ISR(INT1_vect)
{
  if (startOfCode)
  {
#ifdef	DEBUG_IRDA_LED
    digitalWrite (DEBUG_IRDA_LED, 0) ;
#endif
    startOfCode     = FALSE ;
    expectingRising = FALSE ;
    readingCode     = TRUE ;
    TCNT0           = 0 ;
    return ;
  }

  codeTimes [timesPtr] = TCNT0 ;
  TCNT0 = 0 ;

  if (expectingRising)
  {
    expectingRising = FALSE ;
    setInt1Falling () ;
  }
  else
  {
    expectingRising = TRUE ;
    setInt1Rising () ;
  }

  if (++timesPtr == CODE_STORE_SIZE)
    decodeCode () ;
}


/*
 * TIMER0_OVF_vect:
 *	We ran out of time...
 *	Or we got a mis-fire... (and then ran out of time)
 *********************************************************************************
 */

ISR(TIMER0_OVF_vect)
{
#ifdef	DEBUG_IRDA_LED
  digitalWrite (DEBUG_IRDA_LED, 1) ;
#endif
  if (!startOfCode)
    decodeCode () ;
}

/*
 * irdaShutdown:
 *	Shutdown our systems nicely in preparation for deep sleep
 *********************************************************************************
 */

void irdaShutdown (void)
{

// Shutdown timer0

  TCCR0B = 0 ;
  power_timer0_disable () ;

// Diable the interrupt on Int1 - the IR sensor
//	No need for that to wake us up.

  EIMSK &= ~_BV (INT1) ;
}


/*
 * irdaInit:
 *	Initialise what we need to do for IRDA recieving.
 *********************************************************************************
 */

void irdaInit (void)
{

// Start looking for a falling interrupt on the IR pin (Int1)

  expectingRising = FALSE ;
  startOfCode     = TRUE ;

// Enable timer0

  power_timer0_enable () ; delay (1) ;

// Set the Int0 (IR Input) to the right state

  setInt1Falling () ;
  pinMode        (IR_REC, INPUT) ;
  EIMSK |= _BV (INT1) ;

  delay (1) ;

// Set Timer0 to divide by 256. This is one tick every 32µS, or rolls over
//	in 8.192mS. The longest pulse we're expecting to test for is
//	about 2500µS - that's a start pulse. A 1 is about 1200µS and a
//	0 is about 600µS, so 32µS should give us enough leeway to check.

// Prescale by 1024: One tick every 8000000/1024 or 128µS

  TCCR0A = 0 ;		// Normal mode
//TCCR0B = _BV (CS02) | _BV(CS00) ;	// Pre-scale by 1024
  TCCR0B = _BV (CS02) ;			// Pre-scale by  256
  TCNT0  = 0 ;

// Enable timer0 overflow interrupt

  TIMSK0 = _BV (TOIE0) ;	// Interrupt on overflow
  TIFR0  = _BV (TOV0) ;		// Clear any pending overflow interrupt

#ifdef	DEBUG_IRDA_LED
  pinMode (DEBUG_IRDA_LED, OUTPUT) ;
#endif
}
