#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO

pinNum = 21
print ("Pin 21 is ON")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output
GPIO.output(pinNum,GPIO.HIGH)
#GPIO.setup(pinNum,GPIO.IN) #replace pinNum with whatever pin you used, this sets up that pin as an output
#state = GPIO.input(pinNum)
#if (state):
#  print ("Pin 21 is measured on")
#else:
#  print ("Pin 21 is measured off?")

