#!/usr/bin/env python 3

#---------------------------------------
# Alarm System
# Author: Robin Greig
# Date: 2017.06.12
#---------------------------------------

import curses
stdscr = curses.initscr()

print('Press a key. Press <ESC> to quit')

while True:
	x - stdscr.getkey()
	if ord(x) > 0:
		print('You pressed the ',x,' key)
	if x==27:
		break
print('Bye')
