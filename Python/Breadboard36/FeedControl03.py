#!/usr/bin/python

#import os, subprocess, sys, time, smbus
import time
import RPi.GPIO as GPIO

#Import library and create new REST client
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

##### For troubleshooting, set DEBUG to 1
DEBUG = 0

##### Set Variables

##### Set GPIO pins
Light = 21

##### Setup GPIO
GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(Light,GPIO.OUT) # Set GPIO to output for lamp
GPIO.output(Light,GPIO.LOW)

while True:
    # Get data
    data = aio.receive('Lamp')
    # Print out feed metadata
    print('Data Value: {0}'.format(data.value))
    # Turn it into an integer
    LightStatus = int(data.value)
    # Test the value of the toggle switch
    if LightStatus > 0:
        GPIO.output(Light,GPIO.HIGH)
    else:
        GPIO.output(Light,GPIO.LOW)
    time.sleep(1)
