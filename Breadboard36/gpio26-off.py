#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO

pinNum = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output

GPIO.output(pinNum,GPIO.LOW)
#GPIO.cleanup()
