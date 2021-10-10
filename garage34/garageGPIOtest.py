#!/usr/bin/env python3

import RPi.GPIO as GPIO
import warnings
import time

# Setup GPIO24 as relay output
relay = 24
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
#GPIO.setmode(GPIO.BOARD) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(relay,GPIO.OUT) # Sets up variable relay as an output
GPIO.output(relay,GPIO.HIGH) # Turn the relay on and start the furnace
time.sleep(5)
GPIO.output(relay,GPIO.LOW) # Turn the relay on and start the furnace

