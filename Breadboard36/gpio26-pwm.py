#!/usr/bin/env python3

# gpio26-pwm.py
# Test program to adjust light intensity of LED string
# Using a IRLB8721 FET
#
# Robin Greig
# 2019.04.21


import time
import os
import RPi.GPIO as GPIO

pinNum = 26	# Pin number used to drive FET for LED's
delay = 1	# time.sleep delay
count = 1	# number of times to run thru the program

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) # This sets up pinNum as an output
pwm = GPIO.PWM(pinNum, 100) # Iintialize PWM on pinNum @ 100Hz frequency

# main loop of program
print("\nPress Ctrl C to quit \n")	# Print blank line before and after message
dc = 0 					# Set dc variable to 0 for 0%
pwm.start(dc)				# Start PWM with 0% duty cycle

try:
#    while True:			# Loop unti Ctrl C is pressed to stop
     while count > 0:
      for dc in range(0, 101, 10):	# Loop 0 to 100 stepping dc by 10 each loop
        pwm.ChangeDutyCycle(dc)
        time.sleep(delay)		# Wait 0.1 seconds at current LED brightness
        print(dc)
      for dc in range(90, 0, -10):	# Loop 95 to 0 stepping dc down by 10 each loop
        pwm.ChangeDutyCycle(dc)
        time.sleep(delay)		# Wait 0.1 seconds at current brightness
        print(dc)
      count = count - 1
except KeyboardInterrupt:
    print("Ctrl C pressed - ending program")

pwm.stop()			# Stop PWM
GPIO.cleanup()			# Resets GPIO ports used back to input mode
print("Program Ending!")
