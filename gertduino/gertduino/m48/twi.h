/*
 * twi.h:
 *	Drive the TWI/I2C interface on the AVR processor.
 *
 * Note: This is a special cut-down version of the driver explicitly
 *	for the ATmega48p on the Gertuino
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
 *********************************************************************************
 */

extern void twiShutdown (void) ;
extern void twiInit     (uint8_t address, uint8_t mask) ;
