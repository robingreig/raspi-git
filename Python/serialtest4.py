#!/usr/bin/env python

import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)
count = 0
while (count < 10):
  ser.flushInput()
  ser.write("^")
  rcv1 = ser.readline()
  rcv2 = ser.readline()
  print "rcv1 = ", (rcv1)
  print "rcv2 = ", (rcv2)
  ser.write("~")
  print ser.readline()
  ser.write("+")
  print ser.readline()
  print "Count = ", (count)
  time.sleep (1)
  count = count + 1
