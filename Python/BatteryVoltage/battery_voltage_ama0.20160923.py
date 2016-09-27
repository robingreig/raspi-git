#!/usr/bin/env python

import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=5)


DEBUG = 0
count = 0

while (count < 2):
  ser.flushInput() # flush the serial input on raspi
  ser.write("1") # tell gertduino to send Sensor Value
  print ser.readline()
  count = count + 1
  time.sleep(1)
