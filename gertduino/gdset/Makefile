# Makefile:
#	Make the Gertduino m48p alarm set program.
#
# Copyright (c) 2013 Gordon Henderson
#################################################################################
# This file is part of gertduino-m48:
#	Software to run on the ATmega48p processor on the Gerduino board
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this.  If not, see <http://www.gnu.org/licenses/>.
#################################################################################


DESTDIR=/usr
PREFIX=/local

#DEBUG	= -g -O0
DEBUG	= -O3
CC	= gcc
INCLUDE	= -I$(DESTDIR)$(PREFIX)/include
CFLAGS	= $(DEBUG) -Wall $(INCLUDE) -Winline -pipe

LDFLAGS	= -L$(DESTDIR)$(PREFIX)/lib
LDLIBS    = -lwiringPi -pthread

###############################################################################

SRC	=	gdset.c

OBJ	=	$(SRC:.c=.o)

BINS	=	$(SRC:.c=)

all:	$(BINS)

gdset:	gdset.o
	@echo [link]
	@$(CC) -o $@ gdset.o $(LDFLAGS) $(LDLIBS)

.c.o:
	@echo [Compile] $<
	@$(CC) -c $(CFLAGS) $< -o $@

.PHONEY:	clean
clean:
	@echo "[Clean]"
	@rm -f $(OBJ) *~ core tags $(BINS)

.PHONEY:	tags
tags:	$(SRC)
	@echo [ctags]
	@ctags $(SRC)

.PHONEY:	install
install:
	@echo "[Install]"
	@cp gdset		$(DESTDIR)$(PREFIX)/bin
	@chmod 2755		$(DESTDIR)$(PREFIX)/bin/gset

.PHONEY:	depend
depend:
	makedepend -Y $(SRC)

# DO NOT DELETE
