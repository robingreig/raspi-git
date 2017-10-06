#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: museum1.py
# Author: Robin Greig
# Date 2017.10.06
# Email: robin.greig@calalta.com
# Check for input every 0.1 seconds
# Respond to input by playing sounds
#-------------------------------------------------------------------
import os, subprocess, sys, time, smbus
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
GPIO.setup(PIR_Sensor_2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors

#GPIO.add_event_detect(PIR_Sensor, GPIO.FALLING, callback=my_callback_one, bouncetime=200)

bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # DEvice Address (A0-A2)
IODIRA = 0x00 # Pin direction Register
OLATA = 0x14 # Register for Outputs
GPIOA = 0x12 # Register for Inputs

# Set all GPA pins as outputs by setting 
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)

# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)

for MyData in range (1,8):
  # Count from 1 to 8 which in binary will 
  # count from 001 to 111
  bus.write_byte_data(DEVICE,OLATA,MyData)
  print (MyData)
  time.sleep(1)

# Set all bity to zero
bus.write_byte_data(DEVICE,OLATA,0)

