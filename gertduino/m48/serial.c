/*
 * serial.c:
 *	Version of DROSS standard serial code for the Gerduino.
 *	This version running without interrupts, and expecting all
 *	strings in PROGMEM.
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

#include <inttypes.h>
#include <stdlib.h>

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/power.h>

#include "wiring.h"
#include "serial.h"

#include "m48.h"


/*
 * baudRate:
 *	Calculate the baud rate numbers for the AVR (Arduino) serial ports,
 *	taking into account the error factor to use x2 mode or not.
 *********************************************************************************	
 */

static void baudRate (uint32_t baud, uint8_t *lo, uint8_t *hi, uint8_t *u2x)
{
  uint8_t  nonu2x_baud_error ;
  uint8_t  u2x_baud_error ;
  uint16_t setting ;

// U2X mode is needed for baud rates higher than (CPU Hz / 16)

  if (baud > F_CPU / 16)
    *u2x = TRUE ;
  else
  {

// Calculate the percent difference between the baud-rate specified and the
//	real baud rate for both U2X and non-U2X mode (0-255 error percent)

    nonu2x_baud_error = abs ((int)(255 - ((F_CPU / (16 * (((F_CPU / 8 / baud - 1) / 2) + 1)) * 255) / baud))) ;
    u2x_baud_error    = abs ((int)(255 - ((F_CPU / ( 8 * (((F_CPU / 4 / baud - 1) / 2) + 1)) * 255) / baud))) ;

// Figure out of U2X mode would allow for a better connection, so
//	we prefer non-U2X mode because it handles clock skew better

    *u2x = (nonu2x_baud_error > u2x_baud_error) ;
  }

  if (*u2x)
    setting = (F_CPU / 4 / baud - 1) / 2 ;
  else
    setting = (F_CPU / 8 / baud - 1) / 2 ;

  *hi = setting >> 8 ;
  *lo = setting & 0xFF ;
}


/*
 * serialPutchar:
 *	Output the supplied character over the serial port
 *
 */

void serialPutchar (uint8_t c)
{
  if (c == '\n')
    serialPutchar ('\r') ;

  while ((UCSR0A & _BV (UDRE0)) == 0)
    ;

  UDR0 = c ;
}


/*
 * serialPrHex8:
 *	Output a byte as a hex number
 *********************************************************************************
 */

const char hexes[] PROGMEM = "0123456789ABCDEF" ;

void serialPrHex8 (const uint8_t x)
{
  int x1 = x / 16 ;
  serialPutchar (pgm_read_byte (&hexes [x1])) ;
  serialPutchar (pgm_read_byte (&hexes [x - (x1 * 16)])) ; 
}

void serialPrHex16 (const uint16_t x)
{
  serialPrHex8 ((x >> 8) & 0xFF) ;
  serialPrHex8 ((x >> 0) & 0xFF) ;
}


/*
 * serialPuts:
 *	Output a string
 *********************************************************************************
 */

void serialPuts (const char *s)
{
  while (pgm_read_byte (s))
    serialPutchar (pgm_read_byte (s++)) ;
}

void serialNewline (void)
  { serialPutchar ('\r') ; serialPutchar ('\n') ; }


/*
 * serialKeypressed:
 *	Return true/false depending on a character being avalable
 *
 */

uint8_t serialKeypressed (void)
{
  return (UCSR0A & _BV (RXC0)) != 0 ;
}

/*
 * serialGetchar:
 *	Return the next character in the buffer, or wait for one to be typed
 *	
 */

uint8_t serialGetchar (void)
{
  while (!serialKeypressed ())
    ;

  return UDR0 ;
}
  

/*
 * serialShutdown:
 *	Close down the serial port in an orderly manner
 *********************************************************************************
 */

void serialShutdown (void)
{
  UCSR0B = 0 ;
  UCSR0C = 0 ;
  power_usart0_disable () ; 
}

/*
 * serialInit:
 *	Initialise the standard serial port in the AVR Mega chips
 *********************************************************************************
 */

void serialInit (uint32_t baud)
{
  uint8_t hi, lo ;
  uint8_t    u2x ;

  power_usart0_enable () ; delay (1) ;

  baudRate (baud, &lo, &hi, &u2x) ;

  if (u2x)
    UCSR0A  |= (1 << U2X0) ;
  else
    UCSR0A  &= ~(1 << U2X0) ;

  UBRR0H = hi ;
  UBRR0L = lo ;

  (void)UDR0 ;	// dummy read to clear any flag

// Set Rx enable, Tx enable flags and
//	Rx Complete Interrupt flag

  UCSR0B = _BV (RXEN0)  | _BV (TXEN0) ;
  UCSR0C = _BV (UCSZ01) | _BV (UCSZ00) ;
}
