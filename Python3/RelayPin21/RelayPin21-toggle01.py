#!/usr/bin/env python3
#
# File: RelayPin21-toggle01.py
# Date: 2018.08.10
# Author: Robin Greig
#
# Toggles pin 21 back and forth without cleaning up GPIO when done
#

import time
import os
import RPi.GPIO as GPIO

pinNum = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.IN) #replace pinNum with whatever pin you used, this sets up that pin as an input
state = GPIO.input(pinNum) #variable state = value of pinNum variable
if (state):
  print ("Pin 21 is measured on")
  GPIO.setup(pinNum,GPIO.OUT) # Set pinNum to an output
  GPIO.output(pinNum,GPIO.LOW) # toggle pinNum to LOW (if it was high)
else:
  print ("Pin 21 is measured off")
  GPIO.setup(pinNum,GPIO.OUT) # Set pinNum to an output
  GPIO.output(pinNum,GPIO.HIGH) # Toggle pinNum to HIGH (if it was low)

