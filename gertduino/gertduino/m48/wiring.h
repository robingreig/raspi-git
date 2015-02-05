/*
 * wiring.h:
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

#define	INPUT		0
#define OUTPUT		1
#define	PWM		2

#define	LOW		0
#define	HIGH		1


// Function prototypes

extern void    pinMode      (uint8_t pin, uint8_t mode) ;
extern void    pwmWrite     (uint8_t pin, uint8_t val) ;
extern void    digitalWrite (uint8_t pin, uint8_t val) ;
extern uint8_t digitalRead  (uint8_t pin) ;
extern uint8_t digitalMode  (uint8_t pin) ;
extern uint8_t digitalPort  (uint8_t pin) ;

extern uint32_t micros            (void) ;
extern uint32_t millis            (void) ;
extern void     delay             (int v) ;
extern void     delayMicroseconds (int v) ;

