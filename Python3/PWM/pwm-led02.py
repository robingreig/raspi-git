#!/usr/bin/python3

import RPi.GPIO as GPIO		# Import the GPIO library
import time			# Import the time library

GPIO.setmode(GPIO.BCM)		# Set Pi to use BCM pin numbering
GPIO.setup(18, GPIO.OUT)	# Set pin 18 to output mode
pwm = GPIO.PWM(18, 100)		# Initialize PWM on pwmPin 100Hz frequency

# main loop of program
print("/nPress Ctl C to quit \n")	# Print blank line (\n = newline) before & after message
dc = 0					# set dc variable to 0 (will start PWM at 0% duty cycle)
pwm.start(dc)				# Start PWM with 0% duty cycle
while True:
  for dc in range (0, 101, 5):		# Loop with dc set from 0 to 100 stepping dc up by 5 each loop
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)			# wait for 0.1 seconds at current LED brightness level
    print(dc)				# display the current brightness level
  for dc in range (95, 0, -5):		# Loop with dc set from 95 to 5 stepping dc down by 5 each loop
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)
    print(dc)

pwm.stop()				# stop PWM
GPIO.cleanup()				# resets GPIO ports used in this program back to input mode

