#!/usr/bin/env python3

##########
# Author: Robin Greig
# Date: 2021.12.27
# Filenae: /raspi-git/garage34/resetGPIO.py
# 1) GPIO23 is for the relay that controls the lite for the camera
# 2) GPIO24 is for the thermostat
# 3) GPIO24 connected to relay so when output is high, relay is off
# 4) Outputs are in an uncertain state when pi boots up so
# 4) Set them as outputs and 'HIGH' so relays are OFF
##########

import RPi.GPIO as GPIO
import warnings


# Setup GPIO23 as relay output = Light for Camera
relay1 = 23
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(relay1,GPIO.OUT) # Sets up variable relay1 as an output
GPIO.output(relay1,GPIO.HIGH) # Turn the relay OFF

# Setup GPIO24 as relay output
relay2 = 24
GPIO.setup(relay2,GPIO.OUT) # Sets up variable relay2 as an output
GPIO.output(relay2,GPIO.HIGH) # Turn the relay OFF

