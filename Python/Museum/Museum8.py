#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: museum8.py
# Author: Robin Greig
# Date 2018.01.28
# Email: robin.greig@calalta.com
# Check for input every 0.1 seconds
# Respond to input by playing sound & turning on all 91 outputs 
# one second at a time and then turning all off after 180 seconds
#-------------------------------------------------------------------
import os, subprocess, sys, time, smbus
import RPi.GPIO as GPIO

##### For troubleshooting, set DEBUG to 1
DEBUG = 0
debug_time = 1

##### Set Variables
HoldTime = 180

##### Set GPIO pins
English = 24
French = 25
PI_Off = 18

##### Setup GPIO
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(English,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO to input for English pushbutton
GPIO.setup(French,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO to input for French pushbutton
GPIO.setup(PI_Off,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO to input for PI Off button

bus = smbus.SMBus(1) # Rev 2 Pi uses 1
os.system('amixer cset numid=3 1')

DEVICE1 = 0x21 # DEvice Address (A0-A2)
IODIRA = 0x00 # Pin direction Register
OLATA = 0x14 # Register for Outputs
GPIOA = 0x12 # Register for Inputs
IODIRB = 0x01 # Pin direction Register
OLATB = 0x13 # Register for Outputs
GPIOB = 0x12 # Register for Inputs

DEVICE2 = 0x22 # DEvice Address (A0-A2)
IODIRA = 0x00 # Pin direction Register
OLATA = 0x14 # Register for Outputs
GPIOA = 0x12 # Register for Inputs
IODIRB = 0x01 # Pin direction Register
OLATB = 0x13 # Register for Outputs
GPIOB = 0x12 # Register for Inputs

# Set all GPA pins as outputs by setting 
# all bits of IODIRA & IODIRB registers to 0
bus.write_byte_data(DEVICE1,IODIRA,0x00)
bus.write_byte_data(DEVICE1,IODIRB,0x00)
bus.write_byte_data(DEVICE2,IODIRA,0x00)
bus.write_byte_data(DEVICE2,IODIRB,0x00)

# Set output all 8 output bits on each register to 0
bus.write_byte_data(DEVICE1,OLATA,0)
bus.write_byte_data(DEVICE1,OLATB,0)
bus.write_byte_data(DEVICE2,OLATA,0)
bus.write_byte_data(DEVICE2,OLATB,0)

while True:
  if(GPIO.input(PI_Off)):
    subprocess.call(["sudo", "poweroff"])
  if(GPIO.input(English)):
    os.system('mpg123 /home/robin/raspi-git/Audio/6leds.mp3 &')
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,127)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATB,127)
    time.sleep(10)
    bus.write_byte_data(DEVICE0,OLATA,0)
    bus.write_byte_data(DEVICE0,OLATB,0)

# Set all bits to zero
bus.write_byte_data(DEVICE0,OLATA,0)
bus.write_byte_data(DEVICE0,OLATB,0)
