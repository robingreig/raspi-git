#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO

Inputpin = 25
#Outputpin = 21
count = 10

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(Inputpin,GPIO.IN) #replace pinNum with whatever pin you used, this sets up that pin as an input
#GPIO.setup(Outputpin,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an input

while count > 0:
  if GPIO.input(Inputpin) == 0:
#    GPIO.output(Outputpin,GPIO.LOW)
    print ('Pin 25 is low')
    time.sleep(3)
  if GPIO.input(Inputpin) == 1:
#    GPIO.output(Outputpin,GPIO.HIGH)
    print ('Pin 25 is high')
    time.sleep(3)
  count = count - 1
GPIO.cleanup()
