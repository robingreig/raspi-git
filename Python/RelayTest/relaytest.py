#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

relay01_pin = 21

GPIO.setup(relay01_pin, GPIO.IN)

state = GPIO.input(relay01_pin)

if (state):
  print "Pin is High"
if (state == 1):
  print "State = 1"
if (state == 0):
  print "Pin is Low"
  print "State = 0"


