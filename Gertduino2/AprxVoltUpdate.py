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
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

#====================================================================
# Send the Analogue Port number to Gertduino & read back the voltage value
#====================================================================

#while True:
while (count < maxcount):
  ser.flushInput()
  print "Count= {0}".format(count)
#   OK read all Analog
  for i in range(6):
    if DEBUG == 1:
	print "\ti={0}".format(i)
#   write the Analogue Port number to GertDuino
    ser.write(chr(48+i))
#   read the response back from GertDuino
    line = ser.readline()
#    print "\t{0}".format(line),
    print "\tA{0}=".format(i),
    print "{0}".format(line),
#   If reading Analogue 0 then save the voltage to /home/robin/ReadVoltage0
    if i == 0:
      cht = open("/home/robin/AprxVoltage", "wb")
      cht.write(line);
      cht.close()
#     If the voltage is low on Analogue 0 then print "Low", or "Critical", or shutdown Raspi
      if float(line) < 12.00 and float(line) > 11.51:
        print "\t\tVoltage is low"
      elif float(line) < 11.50 and float(line) > 11.01:
        print "\t\tVoltage is CRITICAL"
      elif float(line) < 11.00:
#        subprocess.call(["sudo", "shutdown", "-k"])
        subprocess.call(["sudo", "shutdown", "-k", "now"])
  count = count +1
  time.sleep(delay)
