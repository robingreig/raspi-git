#!/usr/bin/env python

import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

while (1):
  ser.write("\r\nSay Something")
  rcv = ser.read(10)
  ser.write("\r\nYou sent: " + repr(rcv)
