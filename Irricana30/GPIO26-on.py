#!/usr/bin/env python3

# 2023.11.26 GPIO26-on.py
# Robin Greig
# Turn on GPIO26 - Relay#2 - VPN

import time
import os
import RPi.GPIO as GPIO

pinNum = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output

GPIO.output(pinNum,GPIO.LOW) # turn GPIO on
#GPIO.cleanup()
