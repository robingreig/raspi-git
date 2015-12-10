#!/usr/bin/env python
#====================================================================
# Import subfiles
#====================================================================
import datetime
import subprocess
import sys
import time
import warnings

#====================================================================
# Set Variables
#====================================================================
DEBUG = 1

#====================================================================
# Read back the voltage value & turn on the Battery Charger if necessary
#====================================================================

while True:
# Read the Battery Voltage from BattMon1
  def read_CurrentAprxVoltage():
    f = open("/home/robin/ReadVoltage4", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    volts = float(line2)
    return volts

  BattVolts = (round(read_CurrentAprxVoltage(),2))

  if DEBUG == 1:
    print "Battery Voltage: ", (round(read_CurrentAprxVoltage(),2))
    print "Battery Voltage rounded: ", (round(read_CurrentAprxVoltage(),2))

# If the voltage is low, then print "Low", or "Critical", or shutdown Raspi
  if BattVolts >= 28:
    print "\t\tVoltage is > 28V"
  elif BattVolts < 28 and BattVolts >= 27:
    print "\t\tVoltage is between 27V & 28V"
  elif BattVolts < 27 and BattVolts >= 26:
    print "\t\tVoltage is between 26V & 27V"
  elif BattVolts < 26 and BattVolts >= 25:
    print "\t\tVoltage is between 25V & 26V"
  elif BattVolts < 25 and BattVolts >= 24:
    print "\t\tVoltage is low (between 24V & 25V)"
  elif BattVolts < 23.9 and BattVolts >= 23.5:
    print "\t\tVoltage is low (between 23.5V & 23.9V)"
  elif BattVolts < 23.5:
#    subprocess.call(["sudo", "shutdown", "-r", "now"])
    subprocess.call(["sudo", "shutdown", "-k", "now"])
#    subprocess.call(["sudo", "poweroff"])
  break
