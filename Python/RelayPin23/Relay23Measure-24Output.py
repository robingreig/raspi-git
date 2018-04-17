#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO

inputNum = 23
outputNum = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(inputNum,GPIO.IN) #replace pinNum with whatever pin you used, this sets up that pin as an input
GPIO.setup(outputNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an input
state = GPIO.input(inputNum)
if (state):
  print ("Pin 23 is measured on")
  print ("Pin 24 is turned on")
  GPIO.output(outputNum,GPIO.HIGH)
else:
  print ("Pin 23 is measured off")
  print ("Pin 24 is turned off")
  GPIO.output(outputNum,GPIO.LOW)

