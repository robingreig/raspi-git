#!/usr/bin/env python3

# gpio26-pwm50.py
# Test program to adjust light intensity of LED string @ 50%
# Using a IRLB8721 FET
#
# Robin Greig
# 2019.04.21

import RPi.GPIO as GPIO
import time

pinNum = 26	# Pin number used to drive FET for LED's
dc = 0		# Set dc variable to 0 for 0% to start

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 		# Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) 	# This sets up pinNum as an output
pwm = GPIO.PWM(pinNum, 100) 	# Iintialize PWM on pinNum @ 100Hz frequency

# main loop of program
print("\nPress Ctrl C to quit \n")
pwm.start(dc)			# Start pwm @ 0%

try:
  while True:				# Loop unti Ctrl C is pressed to stop
    if dc < 50:
      for dc in range (0, 51, 10):	# Ramp up to 50% by 5
        pwm.ChangeDutyCycle(dc)		# Ramp up to 50% duty cycle
        time.sleep(0.1)			# Sleep 0.1 sec
        print(dc)
except KeyboardInterrupt:
    print("Ctrl C pressed - ending program")

pwm.stop()			# Stop PWM
GPIO.cleanup()			# Resets GPIO ports used back to input mode
