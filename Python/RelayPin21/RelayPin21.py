#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO

pinNum = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.IN) #replace pinNum with whatever pin you used, this sets up that pin as an input
state = GPIO.input(pinNum)
if (state):
  print ("Pin 21 is measured on")
else:
  print ("Pin 21 is measured off?")
if (state == 0):
  print ("State = 0")
if (state == 1):
  print ("State = 1")

