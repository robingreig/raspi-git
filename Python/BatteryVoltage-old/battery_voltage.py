#!/usr/bin/env python

import serial
import time


count = 0
while (1):
  ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)
#  time.sleep(1) # wait for arduino
  print "Count = ", (count)
  print ser.readline()
#  ser.close()
#  time.sleep(1)
  count = count + 1
