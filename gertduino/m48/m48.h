/*
 * m48.h:
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

#define	I2C_ADDRESS	0x68
#define	I2C_MASK	0x01

// Some pin definitions

//	The TWI (I2C) pins
//		Needed to bring the Pi out of sleep mode

#define	SCL	19
#define	SDA	18

// Inputs

#define	SENSE_5V	2
#define	IR_REC		3

// Misc

#ifndef	TRUE
#  define TRUE	(1==1)
#  define FALSE	(!TRUE)
#endif

// Functions

extern void wakeUpPi    (void) ;
extern void powerDownPi (void) ;
