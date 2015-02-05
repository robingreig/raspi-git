/*
 * gdset:
 *	Program to set the powerUp or powerDown registers in the Gertduino
 *	ATmega48p RTC.
 *
 *	This program must be used in conjunction with the Sample code
 *	provided by myself.
 *
 *	It's designed to be used in conjunction with the standard date
 *	command as follows:
 * 
 *	gdset -wakeup `date '+%s' -d '7pm'`
 *	gdset -wakeup `date '+%s' -d '+30 minutes'`
 *	gdset -powerdown `date '+%s' -d '+30 seconds'` ; halt
 *	gdset -h
 *
 *	and so on.
 *
 * Copyright (c) 2013 Gordon Henderson <projects@drogon.net>
 ********************************************************************************
 * This file is part of the Gertduino m48 project.
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <ctype.h>

#include <wiringPiI2C.h>

/*
 * failUsage:
 *	Do just that.
 *********************************************************************************
 */

void failUsage (const char *name)
{
  fprintf (stderr, "Usage: %s [-h | -wakeup | -powerdown] \"time specification\"\n", name) ;
  exit (EXIT_FAILURE) ;
}

void help (const char *name)
{
  printf ("%s: Examples of usage\n", name) ;
  printf ("  %s -wakeup \"now +1 hour\"\n", name) ;
  printf ("  %s -wakeup \"8am\"\n", name) ;
  printf ("  %s -wakeup \"july 5 8am\"\n", name) ;
  printf ("Remember to surround the time specification with quotes.\n") ;
  printf ("See the man page for date for more examples in the -d section\n") ;
}


#define	DATE_CMD	"/bin/date '+%%s' -d '%s'"

/*
 * main:
 *********************************************************************************
 */

int main (int argc, char *argv [])
{
  int fd ;
  int i ;
  int offset ;
  unsigned int timeToSet ;
  unsigned char v, buffer [4] ;

  FILE *dateFd ;
  char *dateCommand ;
  char  dateReply [128] ;

  if ((argc == 2) && (strcasecmp (argv [1], "-h") == 0)) 
  {
    help (argv [0]) ;
    return 0 ;
  }

  if (argc != 3)
    failUsage (argv [0]) ;

  fd = wiringPiI2CSetup (0x69) ;

  /**/ if (strcasecmp (argv [1], "-wakeup")    == 0)
    offset = 0 ;
  else if (strcasecmp (argv [1], "-powerdown") == 0)
    offset = 4 ;
  else
    failUsage (argv [0]) ;

  dateCommand = malloc (strlen (DATE_CMD) + strlen (argv [2])) ;
  sprintf (dateCommand, DATE_CMD, argv [2]) ;

  if ((dateFd = popen (dateCommand, "re")) == NULL)
  {
    fprintf (stderr, "%s: Unable to run date command: %s\n", argv [0], strerror (errno)) ;
    exit (EXIT_FAILURE) ;
  }

  if ((fgets (dateReply, 128, dateFd)) == NULL)
  {
    fprintf (stderr, "%s: Bad reply from date command\n", argv [0]) ;
    exit (EXIT_FAILURE) ;
  }

  if (!isdigit (dateReply [0]))
  {
    fprintf (stderr, "%s: Non numeric reply from date command\n", argv [0]) ;
    exit (EXIT_FAILURE) ;
  }

  pclose (dateFd) ;

// Decodes hex or decimal

  timeToSet = (unsigned int)strtol (dateReply, NULL, 0) ;

// Write it to the device

  for (i = 0 ; i < 4 ; ++i)
  {
    buffer [i] = (timeToSet >> (8 * i)) & 0xFF ;
    wiringPiI2CWriteReg8 (fd, offset + i, buffer [i]) ;
  }

// Read and verify

  for (i = 0 ; i < 4 ; ++i)
  {
    v = wiringPiI2CReadReg8 (fd, offset + i) ;
    if (v < 0)
    {
      fprintf (stderr, "%s: Device read failure at: %d\n", argv [0], i) ;
      exit (EXIT_FAILURE) ;
    }
    if (v != buffer [i])
    {
      fprintf (stderr, "%s: Data read failure at: %d Got: 0x%02X, expected: 0x%02X\n",
		argv [0], i, v, buffer [i]) ;
      exit (EXIT_FAILURE) ;
    }
  }

  return 0 ;
}

