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

// Debug LED outputs

#define	DEBUG_IRDA_LED	4
//#define	DEBUG_MAINS_LED	5
//#define	DEBUG_TWI_LED	6
//#define	DEBUG_RTC_LED	7
//#define	DEBUG_WAKE_LED	8

// Keyboard debugging

#define	DEBUG_KEYBOARD
#define	DEBUG_CLOCK_REGS
#define	DEBUG_IR_CODE

// Functions

extern void debugKey      (void) ;

extern void debugShutdown (void) ;
extern void debugInit     (void) ;
