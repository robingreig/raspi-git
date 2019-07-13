#!/usr/bin/python3

import RPi.GPIO as GPIO		# Import the GPIO library
import time			# Import the time library

GPIO.setmode(GPIO.BCM)		# Set Pi to use BCM pin numbering
GPIO.setup(18, GPIO.OUT)	# Set pin 18 to output mode
pwm = GPIO.PWM(18, 100)		# Initialize PWM on pwmPin 100Hz frequency

# main loop of program
print("/nPress Ctl C to quit \n")	# Print blank line (\n = newline) before & after message
dc = 100					# set dc variable to 0 (will start PWM at 0% duty cycle)
pwm.start(dc)				# Start PWM with 0% duty cycle
while True:
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.5)
    print(dc)

pwm.stop()				# stop PWM
GPIO.cleanup()				# resets GPIO ports used in this program back to input mode

