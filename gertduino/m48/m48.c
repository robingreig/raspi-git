/*
 * m48:
 *	Code here to run on the ATmega48p that's part of the Gertduino.
 *
 *	We have to maintain a real-time clock
 *	Sense the 5v line to tell when we go to battery mode.
 *	Use the RTC to wake the Pi, if so desired.
 *	Do something with the IR reciever.
 *	Optionally: Provide space for preipherals to do optional
 *		stuff - like temp/humidity monitoring, etc.
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

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/power.h>

#include "wiring.h"
#include "twi.h"
#include "rtc.h"
#include "irda.h"
#include "serial.h"
#include "debug.h"

#include "m48.h"


/*
 * onTheMains:
 *	Little function to sample the 5v line
 *********************************************************************************
 */

static uint8_t onTheMains ()
  { return digitalRead (SENSE_5V) == 1 ; }


/*
 * wakUpPi:
 *	Signal the Pi to wake up. We do this by grounding it's I2C pins for
 *	a few milliseconds. Important to release them as the Pi will
 *	subsequently sample them to see if it wants to boot the emergency
 *	kernel...
 *********************************************************************************
 */

void wakeUpPi (void)
{
  if (!onTheMains ())	// No point
    return ;		// But one day we'll have the ability to turn on the SMPS...

#ifdef	DEBUG_WAKE_LED
    pinMode (DEBUG_WAKE_LED, OUTPUT) ; digitalWrite (DEBUG_WAKE_LED, 1) ;
#endif

// Disable TWI before we fiddle with the pins.
//	If we don't do this, then the internal plumbing is wrong
//	and the normal digital drivers are not connected to the pins.

  twiShutdown () ;

// Toggle both pins low for 100mS
//	this is the signal to the Pi to come out of halt mode

  pinMode      (SCL, OUTPUT) ; pinMode      (SDA, OUTPUT) ;
  digitalWrite (SCL, 0) ;      digitalWrite (SDA, 0) ;
    delay (100) ;
  digitalWrite (SCL, 1) ;      digitalWrite (SDA, 1) ;
  pinMode      (SCL, INPUT) ;  pinMode      (SDA, INPUT) ;

// Re-enable TWI

  twiInit (I2C_ADDRESS, I2C_MASK) ;
}


/*
 * powerDownPi:
 *	Pull the plug, as it were. We can toggle an output to low which will
 *	disable the SMPS, thus turning off the mains.
 * 	For now, we can do nothing as Gerts not put the hardware on the board...
 *	... but if someone wants to hack a little FET to control the SMPS, then
 *	    this is the place to code the output to it.
 *********************************************************************************
 */

void powerDownPi (void)
{
}


/*
 *********************************************************************************
 * main:
 *	Setup tasks and see what happens...
 *********************************************************************************
 *
 */

int main(void)
{
  register uint8_t i ;

// Start off by shutting down the peripherals, etc. that we will never use.

//	Initial tweaks for the low power... (no library calls for these)

  ADCSRA &= ~_BV (ADEN) ;			// Disable ADC
  ACSR    =  _BV (ACD) ;			// Disable the analog comparator
  DIDR0   =      0x3F ;				// Disable digital input buffers on all ADC 0-5 pins
  DIDR1   =  _BV (AIN1D) | _BV (AIN0D) ;	// Disable digital input buffers on AIN 1/0 (Analog Comparitor)

//	Standard library functions to turn off all other ATmega peripherals

  power_adc_disable    () ;
  power_twi_disable    () ;	// TWI/I2C
  power_spi_disable    () ;
  power_usart0_disable () ;	// Used for debugging
  power_timer0_disable () ;	// Used by the IR detector program
  power_timer1_disable () ;
  power_timer2_disable () ;	// Used by the async. 32768Hz osc.

// Rest of system initialisation now
//	Individual sections will re-enable ATmega peripherals as required.

  debugInit  () ;
  serialInit (115200) ;
  irdaInit   () ;
  rtcInit    () ;
  twiInit    (I2C_ADDRESS, I2C_MASK) ;
  sei        () ;

// Don't bother trying to print anything if we've been booted on battery...

  if (onTheMains ())
  {
    delay (100) ;
    serialPuts (PSTR ("\n\nGerduino ATmega 48p control processor\n")) ;
    serialPuts (PSTR ("Copyright 2013 Gordon Hendeson <projects@drogon.net>\n")) ;
    serialPuts (PSTR ("GPLv3: This is free software with ABSOLUTELY NO WARRANTY.\n")) ;
    serialPuts (PSTR ("Ready\n")) ;
  }

// Big loop:

  for (;;)
  {
    while (onTheMains ())
      debugKey () ;

// The plug has been pulled ...
//	We need to shutdown all peripherals to save energy as we're
//	now running off a 3v, 30mAh coin cell and we need it to last
//	for years...

    twiShutdown    () ;
    irdaShutdown   () ;
    serialShutdown () ;
    debugShutdown  () ;

// Set all pins to inputs with pullups disabled

    for (i = 0 ; i < 20 ; ++i)
    {
      pinMode      (i, INPUT) ;
      digitalWrite (i, 0) ;
    }

// This is the recommended sequence to enter sleep mode...
//	The fuses should have brown-out disabled (bod), but we go through the
//	mechanics of disabling it here just in-case.

    while (!onTheMains ())
    {
      set_sleep_mode    (SLEEP_MODE_PWR_SAVE) ;
      cli               () ;
      sleep_enable      () ;
      sleep_bod_disable () ;
      sei               () ;	// The next instruction is always executed
      sleep_cpu         () ;
      sleep_disable     () ;
    }

// We've woken up and we're back on the mains

    cli        () ;	// Disable ints until everything else has initialised
    debugInit  () ;
    serialInit (115200) ;
    irdaInit   () ;
    twiInit    (I2C_ADDRESS, I2C_MASK) ;
    delay      (1) ;
    sei        () ;	// Let 'er roll...
  }

}
