#!/usr/bin/env python3

#====================================================================
# Import subfiles
#====================================================================
import datetime
import sys
import time
import os
import RPi.GPIO as GPIO
import warnings
from Adafruit_IO import Client

#====================================================================
# Set Variables
#====================================================================
DEBUG = 0
pinNum = 23
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) # Replace pinNum with whatever pin you used, this sets up that pin as an output

#====================================================================
# Read back the voltage value & turn on the Battery Charger if necessary
#====================================================================

while True:
# Read the Battery Voltage from BattMon24
  def read_CurrentBatteryVoltage():
    f = open("/home/robin/Raspi15BatteryVoltage", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    volts = float(line2)
    return volts

  BattVolts = (round(read_CurrentBatteryVoltage(),2))

  if DEBUG > 0:
    print ("Battery Voltage: ", (round(read_CurrentBatteryVoltage(),2)))
    print ("\tBattVolts: ", BattVolts)
    os.system("/home/robin/raspi-git/Python3/SMTP/sendanemail3.py")
  if BattVolts >= 27:
    GPIO.output(pinNum,GPIO.LOW) # Turn the Battery Charger off
    os.system("/home/robin/raspi-git/Python3/SMTP/Raspi15BattHigh.py")
  elif BattVolts < 24:
    os.system("/home/robin/raspi-git/Python3/SMTP/Raspi15BattLow.py")
    GPIO.output(pinNum,GPIO.HIGH) # Turn the Battery Charger on
#  elif BattVolts < 23.0:
#    subprocess.call(["sudo", "shutdown", "-r", "now"])
#    subprocess.call(["sudo", "shutdown", "-k", "now"])
#    subprocess.call(["sudo", "poweroff"])
# Send voltage to Adafruit AIO
  aio = Client('robingreig', 'd0c57dc7661d4b2e8a1868133f9e162c')
  aio.send('raspi15-voltage', BattVolts)
  if DEBUG > 0:
    print('Raspi15 Battery Voltage sent to aio: ', BattVolts)
# Receive data back from Adafruit AIO to verify send above
  if DEBUG > 0:
    data = aio.receive('raspi15-voltage')
    print('Received value: {0}'.format(data.value))

  break
