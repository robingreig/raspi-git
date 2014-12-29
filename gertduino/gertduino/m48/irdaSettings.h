/*
 * irdaSettings.h:
 *	Infra red reciever code.
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


/*
 * Timings for the IR Pulses.
 *	These are determined by running the system in sense mode and
 *	using something line Minicom on the serial port.
 *********************************************************************************
 */

#undef	DISCOVERY_MODE

// Sony Multi Controller
//	No start-bit, just straight into data bits!

//#define	START_BIT	0x00
//#define	SKIP_BITS	0x00
//#define	HIGH_BIT	0x37
//#define	LOW_BIT		0x24

// No-Name TV controller from Currys
//	Seems to output 16 bits which are the same for each key,
//	then a 16-bit data burst.

#define	START_BIT	0x9E
#define	SKIP_BITS	0x10
#define	HIGH_BIT	0x45
#define	LOW_BIT		0x20

// Roberts DAB radio controller
//	Seems to output 16 bits which are the same for each key,
//	then a 16-bit data burst.

//#define	START_BIT	0xB0
//#define	SKIP_BITS	0x10
//#define	HIGH_BIT	0x42
//#define	LOW_BIT		0x20
