#!/usr/bin/env python
#====================================================================
# Import subfiles
#====================================================================
import datetime
import subprocess
import sys
import time
import os
import RPi.GPIO as GPIO
import warnings

#====================================================================
# Set Variables
#====================================================================
DEBUG = 0
pinNum = 23
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) # Rreplace pinNum with whatever pin you used, this sets up that pin as an output

#====================================================================
# Read back the voltage value & turn on the Battery Charger if necessary
#====================================================================

while True:
# Read the Battery Voltage from BattMon1
  def read_CurrentBatteryVoltage():
    f = open("/home/robin/ReadVoltage4", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    volts = float(line2)
    return volts

  BattVolts = (round(read_CurrentBatteryVoltage(),2))

  if DEBUG == 1:
    print "Battery Voltage: ", (round(read_CurrentBatteryVoltage(),2))
    print "\tBattVolts: ", BattVolts

# If the voltage is low, then print "Low", or "Critical", or shutdown Raspi
  if BattVolts >= 28:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is near the maximum level, & turning Battery Charger off"
    GPIO.output(pinNum,GPIO.LOW) # Turn the Battery Charger off
  elif BattVolts < 28 and BattVolts >= 27:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is Normal"
  elif BattVolts < 27 and BattVolts >= 26:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is Normal"
  elif BattVolts < 26 and BattVolts >= 25:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is getting Low"
  elif BattVolts < 25 and BattVolts >= 24:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is getting Low"
  elif BattVolts < 24 and BattVolts >= 23.5:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is getting too LOW & Battery Charger is turning on"
    GPIO.output(pinNum,GPIO.HIGH) # Turn the Battery Charger on
  elif BattVolts < 23.5 and BattVolts >= 23.0:
    print "\tBattVolts: ", BattVolts
    print "\tVoltage is CRITICAL & trying to turn Battery Charger on again"
    GPIO.output(pinNum,GPIO.HIGH) # Turn the Battery Charger on
  elif BattVolts < 23.0:
#    subprocess.call(["sudo", "shutdown", "-r", "now"])
#    subprocess.call(["sudo", "shutdown", "-k", "now"])
    subprocess.call(["sudo", "poweroff"])
  break




