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
maxcount = 2

#====================================================================
# Setup Serial Port
# /tty/AMA0 is used with the GertDuino board
#====================================================================
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

#====================================================================
# Send the Analogue Port number to Gertduino & read back the voltage value
#====================================================================

while True:
  while (count < maxcount):
    ser.flushInput()
    print "Count= {0}".format(count)
#     OK read all Analog
    for i in range(6):
      if DEBUG == 1:
	print "\ti={0}".format(i)
#     write the Analogue Port number to GertDuino
      ser.write(chr(48+i))
#     read the response back from GertDuino
      line = ser.readline()
#     print "\t{0}".format(line),
      print "\tA{0}=".format(i),
      print "{0}".format(line),
#     If reading Analogue 0 then save the voltage to /home/robin/ReadVoltage0
      if i == 0:
        cht = open("/home/robin/AprxVoltage", "wb")
        cht.write(line);
        cht.close()

    count = count +1
    time.sleep(delay)
# Read the voltage back to evaluate it
  def read_CurrentAprxVoltage():
    f = open("/home/robin/AprxVoltage", "r")
    volts = f.readlines()
    f.close
    return volts

# Convert the reading to a float
  def read_AprxVoltage():
    line1 = read_CurrentAprxVoltage()
    line2 = line1[0]
    line3 = float(line2)
    return line3

  BattVolts = (round(read_AprxVoltage(),2))

  if DEBUG == 1:
    print "AprxVoltage: ", (round(read_AprxVoltage(),2))
    print "BattVolts: ", (round(read_AprxVoltage(),2))

# If the voltage is low on Analogue 0 then print "Low", or "Critical", or shutdown Raspi
  if BattVolts >= 13.00:
    print "\t\tVoltage is > 13V"
  elif BattVolts < 13.0 and BattVolts >= 12.5:
    print "\t\tVoltage is between 12.5V & 13V"
  elif BattVolts < 12.5 and BattVolts >= 12.0:
    print "\t\tVoltage is between 12V & 12.5V"
  elif BattVolts < 12.0 and BattVolts >= 11.5:
    print "\t\tVoltage is low (between 11.5V & 12V)"
  elif BattVolts < 11.50 and BattVolts >= 11.0:
    print "\t\tVoltage is CRITICAL (between 11.0V & 11.5V)"
  elif BattVolts < 11.0:
#   subprocess.call(["sudo", "shutdown", "-k"])
    subprocess.call(["sudo", "shutdown", "-k", "now"])
  break
