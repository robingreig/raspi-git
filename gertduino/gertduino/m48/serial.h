/*
 * serial.h:
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

// Function prototypes

extern void    serialPutchar    (uint8_t c) ;
extern void    serialPrHex8     (const uint8_t  x) ;
extern void    serialPrHex16    (const uint16_t x) ;
extern void    serialPuts       (const char *s) ;
extern void    serialNewline    (void) ;
extern uint8_t serialKeypressed (void) ;
extern uint8_t serialGetchar    (void) ;

extern void    serialShutdown   (void) ;
extern void    serialInit       (uint32_t baud) ;
