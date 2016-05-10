#!/usr/bin/env python
#====================================================================
# Import subfiles
#====================================================================
import datetime
import serial
import subprocess
import sys
import time
import warnings

#====================================================================
# Set Variables
#====================================================================
count = 0
delay = 2
DEBUG = 0
maxcount = 1

#====================================================================
# Setup Serial Port
# /tty/AMA0 is used with the GertDuino board
#====================================================================
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

#====================================================================
# Send the Analogue Port number to Gertduino & read back the voltage value
#====================================================================

while True:
  def read_CurrentAprxVoltage():
    f = open("/home/robin/AprxVoltage", "r")
    volts = f.readlines()
    f.close
    return volts

  def read_AprxVoltage():
    line1 = read_CurrentAprxVoltage()
    line2 = line1[0]
    line3 = float(line2)
    return line3

  print "AprxVoltage: ", (round(read_AprxVoltage(),2))
# If the voltage is low on Analogue 0 then print "Low", or "Critical", or shutdown Raspi
#  if float(line3) < 12.00 and float(line) > 11.51:
  if (round(read_AprxVoltage(),2)) < 12.00 and (round(read_AprxVoltage(),2)) > 11.51:
    print "\t\tVoltage is LOW!"
#  elif float(line3) < 11.50 and float(line) > 11.01:
  if (round(read_AprxVoltage(),2)) < 11.50 and (round(read_AprxVoltage(),2)) > 11.01:
    print "\t\tVoltage is CRITICAL!!"
  elif (round(read_AprxVoltage(),2)) < 11.00:
#   subprocess.call(["sudo", "shutdown", "-k"])
    subprocess.call(["sudo", "shutdown", "-k", "now"])
  break
