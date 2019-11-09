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
pinNum = 23
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) # Replace pinNum with whatever pin you used, this sets up that pin as an output

#====================================================================
# Read back the voltage value & turn on the Battery Charger if necessary
#====================================================================

GPIO.output(pinNum,GPIO.LOW) # Turn the Battery Charger off
os.system("/home/robin/raspi-git/Python3/SMTP/Raspi15BattHigh.py")




