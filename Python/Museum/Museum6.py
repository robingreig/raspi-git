#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: museum6.py
# Author: Robin Greig
# Date 2017.12.08
# Email: robin.greig@calalta.com
# Check for input every 0.1 seconds
# Respond to input by playing sound & turning on all 16 outputs 
# one second at a time and then turning all off after 60 seconds
#-------------------------------------------------------------------
import os, subprocess, sys, time, smbus
import RPi.GPIO as GPIO

##### For troubleshooting, set DEBUG to 1
DEBUG = 0
debug_time = 1

##### Set Variables
cycles = 1
HoldTime = 600

##### Set GPIO pins
PIR_Sensor_1 = 24
PIR_Sensor_2 = 25
PI_Off = 18

##### Setup GPIO
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(PIR_Sensor_1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors
GPIO.setup(PIR_Sensor_2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors
GPIO.setup(PI_Off,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PIR Sensors

#GPIO.add_event_detect(PIR_Sensor, GPIO.FALLING, callback=my_callback_one, bouncetime=200)

bus = smbus.SMBus(1) # Rev 2 Pi uses 1
os.system('amixer cset numid=3 1')

DEVICE0 = 0x20 # DEvice Address (A0-A2)
IODIRA = 0x00 # Pin direction Register
OLATA = 0x14 # Register for Outputs
GPIOA = 0x12 # Register for Inputs
IODIRB = 0x01 # Pin direction Register
OLATB = 0x13 # Register for Outputs
GPIOB = 0x12 # Register for Inputs

# Set all GPA pins as outputs by setting 
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE0,IODIRA,0x00)
bus.write_byte_data(DEVICE0,IODIRB,0x00)

# Set output all 8 output bits to 0
bus.write_byte_data(DEVICE0,OLATA,0)
bus.write_byte_data(DEVICE0,OLATB,0)

while True:
  if(GPIO.input(PIR_Sensor_1)):
#    os.system('mpg123 /home/robin/raspi-git/Audio/6leds.mp3 &')
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,127)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATA,255)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,127)
    time.sleep(1)
    bus.write_byte_data(DEVICE0,OLATB,255)
    time.sleep(HoldTime)
    bus.write_byte_data(DEVICE0,OLATA,0)
    bus.write_byte_data(DEVICE0,OLATB,0)
#    break
  if(GPIO.input(PI_Off)):
    subprocess.call(["sudo", "poweroff"])

# Set all bits to zero
bus.write_byte_data(DEVICE0,OLATA,0)
bus.write_byte_data(DEVICE0,OLATB,0)
