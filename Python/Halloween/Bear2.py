#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: bear2.py
# Author: Robin Greig
# Date 2017.10.06
# Check for input every 0.1 seconds
# Respond to input by playing sounds
#-------------------------------------------------------------------
import os, subprocess, sys, time
import RPi.GPIO as GPIO

##### For troubleshooting, set DEBUG to 1
DEBUG = 0
debug_time = 1

##### Set Variables
cycles = 1

##### Set GPIO pins
PIR_Sensor_1 = 24
PIR_Sensor_2 = 25

##### Setup GPIO
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(PIR_Sensor_1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors
#GPIO.setup(PIR_Sensor_1,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO to input for PIR Sensors
GPIO.setup(PIR_Sensor_2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors
#GPIO.setup(PIR_Sensor_2,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO to input for PIR Sensors

#GPIO.add_event_detect(PIR_Sensor, GPIO.FALLING, callback=my_callback_one, bouncetime=200)

os.system('amixer cset numid=3 1')

#def main_loop():
while True:
  if (GPIO.input(PIR_Sensor_1)):
    os.system('mpg123 /home/robin/beargrowl1.mp3')

#try:
#  main_loop()
#except KeyboardInterrupt:
#  GPIO.cleanup()
#  pass
