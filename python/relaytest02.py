#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay01_pin = 23
input01_pin = 24

GPIO.setup(input01_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relay01_pin, GPIO.OUT)
GPIO.output(relay01_pin, False)

while True:
  if (GPIO.input(24) == False):
    GPIO.output(relay01_pin, False)
    print"button pressed"
  if (GPIO.input(24) == True):
    GPIO.output(relay01_pin, True)
    print"button released"
  time.sleep(0.1);

