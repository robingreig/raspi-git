#!/usr/bin/env python3

#====================================================================
# Import subfiles
#====================================================================
import sys
import os
import RPi.GPIO as GPIO
import warnings

#====================================================================
# Set Variables
#====================================================================
pinNum = 24
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) # Replace pinNum with whatever pin you used, this sets up that pin as an output


GPIO.output(pinNum,GPIO.HIGH) # Turn the Outside Lights ON



