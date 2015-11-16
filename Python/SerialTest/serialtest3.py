#!/usr/bin/env python

import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

while (1):
  ser.write("\r\n^")
  rcv1 = ser.readline()
  rcv2 = ser.readline()
  print "rcv1 = ", (rcv1)
  print "rcv2 = ", (rcv2)
  time.sleep (1)
