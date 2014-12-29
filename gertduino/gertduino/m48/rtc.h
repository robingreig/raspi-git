/*
 * rtc.h:
 *	The RTC code for the ATmega48p on the Gertduino
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

// Today, we're emulating the DS1374

// RTC_SIZE:
//	Define the size of the RTC's RAM.
//	Must be a power of 2 for the register wrap code in twi.c

#define	RTC_SIZE	16

// The RTC "memory" locations

extern uint8_t rtc    [RTC_SIZE] ;
extern uint8_t almRtc [RTC_SIZE] ;
extern uint8_t extRtc [RTC_SIZE] ;

extern void rtcInit (void) ;
