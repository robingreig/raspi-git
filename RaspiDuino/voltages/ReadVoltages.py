#!/usr/bin/env python

import serial
import time
import sys
import os
import subprocess
import re
import glob

# Set Variables
count = 0
delay = 2
DEBUG = 1
maxcount = 3

#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=5)
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

#while True:
while (count < maxcount):
  ser.flushInput()

  print "Count= {0}".format(count)
  #ok read all Analog
  for i in range(6):
    if DEBUG == 1:
	print "\t\ti={0}".format(i)
    ser.write(chr(48+i))
    line = ser.readline()
#    print "\t{0}".format(line),
    print "\tA{0}=".format(i),
    print "{0}".format(line),
    if i == 0:
      cht = open("/home/robin/ReadVoltage0", "wb")
      cht.write(line);
      cht.close()
  count = count +1
  time.sleep(delay)
