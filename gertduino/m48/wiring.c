/*
 * wiring.c:
 *	Emulate most of the Arduino wiring functionality. This essentailly
 *	is a logical mapping of IO pins and functions to their physical
 *	entities.
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

#include <avr/io.h>
#include <avr/pgmspace.h>
#include <avr/interrupt.h>


#include "wiring.h"

#define	NO_TIMER	0
#define	TIMER0A		1
#define	TIMER0B		2
#define	TIMER1A		3
#define	TIMER1B		4
#define	TIMER2		5
#define	TIMER2A		6
#define	TIMER2B		7


// ATMega 168 and 328 chip layouts and Arduino equivalents:
//
//                    +-\/-+
//        Reset PC6  1|    |28  PC5 (AI 5, pin 19) I2C-SCL
//  RxD (pin 0) PD0  2|    |27  PC4 (AI 4, pin 18) I2C-SDA
//  TxD (pin 1) PD1  3|    |26  PC3 (AI 3, pin 17)
//      (pin 2) PD2  4|    |25  PC2 (AI 2, pin 16)
// PWM+ (pin 3) PD3  5|    |24  PC1 (AI 1, pin 15)
//      (pin 4) PD4  6|    |23  PC0 (AI 0, pin 14)
//              VCC  7|    |22  GND
//              GND  8|    |21  AREF
//              PB6  9|    |20  AVCC
//              PB7 10|    |19  PB5 (pin 13)     SPI-SCKL On-Board LED
// PWM+ (pin 5) PD5 11|    |18  PB4 (pin 12)     SPI-MISO
// PWM+ (pin 6) PD6 12|    |17  PB3 (pin 11) PWM SPI-MOSI
//      (pin 7) PD7 13|    |16  PB2 (pin 10) PWM SPI-SS
//      (pin 8) PB0 14|    |15  PB1 (pin  9) PWM
//                    +----+
// 
// (PWM+ indicates the additional PWM pins on the ATmega168 and 328
//	vs. the "Tiny/Nano" versions)


// digitalPinToPortReg:
//	Map an Arduino Pin to an AVR port
//
// Definitions for the ATMega 168 or 328 chips.

const uint16_t PROGMEM pinToPortOut [] =
{
  (uint16_t)&PORTD, (uint16_t)&PORTD, (uint16_t)&PORTD, (uint16_t)&PORTD,	// Pins  0- 3
  (uint16_t)&PORTD, (uint16_t)&PORTD, (uint16_t)&PORTD, (uint16_t)&PORTD,	// Pins  4- 7
  (uint16_t)&PORTB, (uint16_t)&PORTB, (uint16_t)&PORTB, (uint16_t)&PORTB,	// Pins  8-11
  (uint16_t)&PORTB, (uint16_t)&PORTB,                                    	// Pins 12-13
                                      (uint16_t)&PORTC, (uint16_t)&PORTC,	// Pins 14-15 - Analog port normally
  (uint16_t)&PORTC, (uint16_t)&PORTC, (uint16_t)&PORTC, (uint16_t)&PORTC,	// Pins 16-19 -  ditto
} ;

const uint16_t PROGMEM pinToPortIn [] =
{
  (uint16_t)&PIND, (uint16_t)&PIND, (uint16_t)&PIND, (uint16_t)&PIND,		// Pins  0- 3
  (uint16_t)&PIND, (uint16_t)&PIND, (uint16_t)&PIND, (uint16_t)&PIND,		// Pins  4- 7
  (uint16_t)&PINB, (uint16_t)&PINB, (uint16_t)&PINB, (uint16_t)&PINB,		// Pins  8-11
  (uint16_t)&PINB, (uint16_t)&PINB,						// Pins 12-13
                                    (uint16_t)&PINC, (uint16_t)&PINC,		// Pins 14-15 - Analog port normally
  (uint16_t)&PINC, (uint16_t)&PINC, (uint16_t)&PINC, (uint16_t)&PINC,		// Pins 16-19 -  ditto
} ;

const uint16_t PROGMEM pinToDDR [] =
{
  (uint16_t)&DDRD, (uint16_t)&DDRD, (uint16_t)&DDRD, (uint16_t)&DDRD,		// Pins  0- 3
  (uint16_t)&DDRD, (uint16_t)&DDRD, (uint16_t)&DDRD, (uint16_t)&DDRD,		// Pins  4- 7
  (uint16_t)&DDRB, (uint16_t)&DDRB, (uint16_t)&DDRB, (uint16_t)&DDRB,		// Pins  8-11
  (uint16_t)&DDRB, (uint16_t)&DDRB,						// Pins 12-13
                                    (uint16_t)&DDRC, (uint16_t)&DDRC,		// Pins 14-15 - Analog port normally
  (uint16_t)&DDRC, (uint16_t)&DDRC, (uint16_t)&DDRC, (uint16_t)&DDRC,		// Pins 16-19 -  ditto
} ;

// pinBits:
//	Indexed by pin. Returns the bit in whaterver port corresponds
//	to the given pin.
//
//	e.g. pin 13 is 0x20 in the given register

const uint8_t PROGMEM pinBits [] =
{
  0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80,	// Pins  0- 7: Port D
  0x01, 0x02, 0x04, 0x08, 0x10, 0x20,			// Pins  8-13: Port B
  0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 			// Pins 14-19: Port C
} ;

// Mapping of pins to timers. Note TIMER0A is not present as we use it
//	internally in DROSS

const uint8_t PROGMEM pinToTimer [] =
{
  NO_TIMER, NO_TIMER, NO_TIMER, TIMER2B,					// Pins  0- 3
  NO_TIMER, TIMER0B,  NO_TIMER, NO_TIMER,					// Pins  4- 7
  NO_TIMER, TIMER1A,  TIMER1B,  TIMER2A,					// Pins  8-11
  NO_TIMER, NO_TIMER,								// Pins 12-13
} ;


/*
 * disablePWM:
 *	turn off PWM on a pin
 *********************************************************************************
 */

void disablePWM (uint8_t pin)
{
  switch (pgm_read_byte (pinToTimer + pin))
  {
    case TIMER0A: TCCR0A &= ~_BV(COM0A1) ; break ;
    case TIMER0B: TCCR0A &= ~_BV(COM0B1) ; break ;
    case TIMER1A: TCCR1A &= ~_BV(COM1A1) ; break ; 
    case TIMER1B: TCCR1A &= ~_BV(COM1B1) ; break ; 
    case TIMER2A: TCCR2A &= ~_BV(COM2A1) ; break ; 
    case TIMER2B: TCCR2A &= ~_BV(COM2B1) ; break ;
  }
}


/*
 * pinMode:
 *	Set a pin to input, output, or PWM (if possible)
 *********************************************************************************
 */

void pinMode (uint8_t pin, uint8_t mode)
{
  volatile uint8_t *reg = (uint8_t *)pgm_read_word (pinToDDR + pin) ;
  uint8_t bit           =            pgm_read_byte (pinBits  + pin) ;

  /**/ if (mode == OUTPUT)	// Output
  {
    disablePWM (pin) ;
    *reg |=  bit ;
  }
  else if (mode == PWM)		// PWM
  {
    *reg |=  bit ;
    switch (pgm_read_byte (pinToTimer + pin))
    {
      case TIMER0A: TCCR0A |= _BV(COM0A1) ; break ; 
      case TIMER0B: TCCR0A |= _BV(COM0B1) ; break ; 
      case TIMER1A: TCCR1A |= _BV(COM1A1) ; break ; 
      case TIMER1B: TCCR1A |= _BV(COM1B1) ; break ; 
      case TIMER2A: TCCR2A |= _BV(COM2A1) ; break ; 
      case TIMER2B: TCCR2A |= _BV(COM2B1) ; break ;
    }
  }
  else				// Default to Input
  {
    disablePWM (pin) ;
    *reg &= ~bit ;
  }
}


/*
 * digitalWrite:
 *	Set/Clear an output pin
 *********************************************************************************
 */

void digitalWrite (uint8_t pin, uint8_t val)
{
  volatile uint8_t *port = (uint8_t *)pgm_read_word (pinToPortOut + pin) ;
  uint8_t bit            =            pgm_read_byte (pinBits      + pin) ;

  if (val == LOW)
    *port &= ~bit ;
  else
    *port |=  bit ;
}


/*
 * digitalRead:
 *	Return the state of an input pin
 *********************************************************************************
 */

uint8_t digitalRead (uint8_t pin)
{
  volatile uint8_t *port = (uint8_t *)pgm_read_word (pinToPortIn + pin) ;
  uint8_t bit            =            pgm_read_byte (pinBits     + pin) ;

  return ((*port & bit) == 0) ? LOW : HIGH ;
}

/*
 * pwmWrite:
 *	Set the PWM output value
 *********************************************************************************
 */

void pwmWrite (uint8_t pin, uint8_t value)
{
  switch (pgm_read_byte (pinToTimer + pin))
  {
    case TIMER0A: OCR0A = value ; break ;
    case TIMER0B: OCR0B = value ; break ;
    case TIMER1A: OCR1A = value ; break ;
    case TIMER1B: OCR1B = value ; break ;
    case TIMER2A: OCR2A = value ; break ;
    case TIMER2B: OCR2B = value ; break ;
  }
}


/*
 * digitalMode: digitalPort:
 *	These are really for debugging
 *********************************************************************************
 */

uint8_t digitalMode (uint8_t pin)
{
  volatile uint8_t *reg = (uint8_t *)pgm_read_word (pinToDDR + pin) ;
  uint8_t bit           =            pgm_read_byte (pinBits  + pin) ;
  return ((*reg & bit) == 0) ? 0 : 1 ;
}

uint8_t digitalPort (uint8_t pin)
{
  volatile uint8_t *reg = (uint8_t *)pgm_read_word (pinToPortOut + pin) ;
  uint8_t bit           =            pgm_read_byte (pinBits      + pin) ;
  return ((*reg & bit) == 0) ? 0 : 1 ;
}


/*
 * delayMicroseconds: delay:
 *	These are "fake" delays in that they don't use any timers, etc. so are
 *	just best guesses at the actual delay time.
 *********************************************************************************
 */

void delayMicroseconds (int x)
{
  for( ; x > 0 ; x--)
  {
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
    __asm__("nop\n\t"); 
  }
}

void delay (int x)
{
  for ( ; x > 0 ; x--)
   delayMicroseconds (1000) ;
}
