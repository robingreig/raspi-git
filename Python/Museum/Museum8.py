#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: museum8.py
# Author: Robin Greig
# Date 2018.01.28
# Email: robin.greig@calalta.com
# Check for input every 0.1 seconds
# Respond to input by playing sound & turning on all 91 outputs
# Device1, Bank A & Device 1, Bank B ..... Device7, Bank A & Device 7, Bank B 
# one second at a time and then turning all off
#-------------------------------------------------------------------
import os, subprocess, sys, time, smbus
import RPi.GPIO as GPIO

##### For troubleshooting:
##### Set DEBUG to 0 for normal operation
##### Set DEBUG to 1 for single run through then exit program
DEBUG = 1

##### Set GPIO pins
English = 24
French = 25
PI_Off = 18

##### Setup GPIO
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(English,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for English pushbutton
if DEBUG > 0:
  GPIO.setup(English,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set English to HIGH to automatically start sequence for Debugging
GPIO.setup(French,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for French pushbutton
GPIO.setup(PI_Off,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO to input for PI Off button

bus = smbus.SMBus(1) # Rev 2 Pi uses 1
os.system('amixer cset numid=3 1')

##### Set Device names to MCP23017 1 - 7 (7 IC's)
##### I started at device 1, 0x21, rather than device 0, 0x20
DEVICE1 = 0x21 # Device Address (A0-A2)
DEVICE2 = 0x22 # Device Address (A0-A2)
DEVICE3 = 0x23 # Device Address (A0-A2)
DEVICE4 = 0x24 # Device Address (A0-A2)
DEVICE5 = 0x25 # Device Address (A0-A2)
DEVICE6 = 0x26 # Device Address (A0-A2)
DEVICE7 = 0x27 # Device Address (A0-A2)

##### Set Pin Directions & Input/Outpus selections for IC's
IODIRA = 0x00 # Pin direction Register
OLATA = 0x14 # Register for Outputs
GPIOA = 0x12 # Register for Inputs
IODIRB = 0x01 # Pin direction Register
OLATB = 0x13 # Register for Outputs
GPIOB = 0x12 # Register for Inputs

# Set all GPA & GPB pins as outputs by setting 
# all bits of IODIRA & IODIRB registers to 0
bus.write_byte_data(DEVICE1,IODIRA,0x00)
bus.write_byte_data(DEVICE1,IODIRB,0x00)
bus.write_byte_data(DEVICE2,IODIRA,0x00)
bus.write_byte_data(DEVICE2,IODIRB,0x00)
bus.write_byte_data(DEVICE3,IODIRA,0x00)
bus.write_byte_data(DEVICE3,IODIRB,0x00)
bus.write_byte_data(DEVICE4,IODIRA,0x00)
bus.write_byte_data(DEVICE4,IODIRB,0x00)
bus.write_byte_data(DEVICE5,IODIRA,0x00)
bus.write_byte_data(DEVICE5,IODIRB,0x00)
bus.write_byte_data(DEVICE6,IODIRA,0x00)
bus.write_byte_data(DEVICE6,IODIRB,0x00)
bus.write_byte_data(DEVICE7,IODIRA,0x00)
bus.write_byte_data(DEVICE7,IODIRB,0x00)

# Set all 8 output bits on each register to 0
bus.write_byte_data(DEVICE1,OLATA,0)
bus.write_byte_data(DEVICE1,OLATB,0)
bus.write_byte_data(DEVICE2,OLATA,0)
bus.write_byte_data(DEVICE2,OLATB,0)
bus.write_byte_data(DEVICE3,OLATA,0)
bus.write_byte_data(DEVICE3,OLATB,0)
bus.write_byte_data(DEVICE4,OLATA,0)
bus.write_byte_data(DEVICE4,OLATB,0)
bus.write_byte_data(DEVICE5,OLATA,0)
bus.write_byte_data(DEVICE5,OLATB,0)
bus.write_byte_data(DEVICE6,OLATA,0)
bus.write_byte_data(DEVICE6,OLATB,0)
bus.write_byte_data(DEVICE7,OLATA,0)
bus.write_byte_data(DEVICE7,OLATB,0)

while True:
  if(GPIO.input(PI_Off)):
    subprocess.call(["sudo", "poweroff"])
  if(GPIO.input(English)):
    os.system('mpg123 /home/robin/raspi-git/Audio/6leds.mp3 &')
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device1, Bank A started")
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
    if(DEBUG > 0):
      print ("Device1, Bank B started")
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
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device2, Bank A started")
    bus.write_byte_data(DEVICE2,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device2, Bank B started")
    bus.write_byte_data(DEVICE2,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE2,OLATB,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device3, Bank A started")
    bus.write_byte_data(DEVICE3,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device3, Bank B started")
    bus.write_byte_data(DEVICE3,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE3,OLATB,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device4, Bank A started")
    bus.write_byte_data(DEVICE4,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device4, Bank B started")
    bus.write_byte_data(DEVICE4,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE4,OLATB,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device5, Bank A started")
    bus.write_byte_data(DEVICE5,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device5, Bank B started")
    bus.write_byte_data(DEVICE5,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE5,OLATB,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device6, Bank A started")
    bus.write_byte_data(DEVICE6,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device6, Bank B started")
    bus.write_byte_data(DEVICE6,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE6,OLATB,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device7, Bank A started")
    bus.write_byte_data(DEVICE7,OLATA,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATA,127)
    time.sleep(1)
    if(DEBUG > 0):
      print ("Device7, Bank B started")
    bus.write_byte_data(DEVICE7,OLATB,1)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,3)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,7)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,15)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,31)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,63)
    time.sleep(1)
    bus.write_byte_data(DEVICE7,OLATB,127)
    time.sleep(1)
    bus.write_byte_data(DEVICE1,OLATA,0)
    bus.write_byte_data(DEVICE1,OLATB,0)
    bus.write_byte_data(DEVICE2,OLATA,0)
    bus.write_byte_data(DEVICE2,OLATB,0)
    bus.write_byte_data(DEVICE3,OLATA,0)
    bus.write_byte_data(DEVICE3,OLATB,0)
    bus.write_byte_data(DEVICE4,OLATA,0)
    bus.write_byte_data(DEVICE4,OLATB,0)
    bus.write_byte_data(DEVICE5,OLATA,0)
    bus.write_byte_data(DEVICE5,OLATB,0)
    bus.write_byte_data(DEVICE6,OLATA,0)
    bus.write_byte_data(DEVICE6,OLATB,0)
    bus.write_byte_data(DEVICE7,OLATA,0)
    bus.write_byte_data(DEVICE7,OLATB,0)
    if(DEBUG > 0):
      break

# Set all bits to zero
bus.write_byte_data(DEVICE1,OLATA,0)
bus.write_byte_data(DEVICE1,OLATB,0)
bus.write_byte_data(DEVICE2,OLATA,0)
bus.write_byte_data(DEVICE2,OLATB,0)
bus.write_byte_data(DEVICE3,OLATA,0)
bus.write_byte_data(DEVICE3,OLATB,0)
bus.write_byte_data(DEVICE4,OLATA,0)
bus.write_byte_data(DEVICE4,OLATB,0)
bus.write_byte_data(DEVICE5,OLATA,0)
bus.write_byte_data(DEVICE5,OLATB,0)
bus.write_byte_data(DEVICE6,OLATA,0)
bus.write_byte_data(DEVICE6,OLATB,0)
bus.write_byte_data(DEVICE7,OLATA,0)
bus.write_byte_data(DEVICE7,OLATB,0)
