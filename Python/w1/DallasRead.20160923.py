##!/usr/bin/env python
#====================================================================
# Import subfiles
#====================================================================
import serial
import time

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
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)
ser = serial.Serial('/dev/serial0', 9600, timeout=5)

#====================================================================
# Send the Analogue Port number to Gertduino & read back the voltage value
#====================================================================

while (count < maxcount):
  print "Count= {0}".format(count)
#  write the Port number to Uno
  print ("Sending a 1")
  ser.flushInput()
  ser.write(chr(49))
  line1 = ser.readline()
  print line1
  cht = open("/home/robin/DallasTemp1", "wb")
  cht.write(line1);
  cht.close()
  time.sleep(delay)
  ser.flushInput()
  print ("Sending a 2")
  ser.write(chr(50))
  line2 = ser.readline()
  print line2
  cht = open("/home/robin/DallasTemp2", "wb")
  cht.write(line2);
  cht.close()
  time.sleep(delay)
  ser.flushInput()
  count = count +1
  time.sleep(delay)
# Read the voltage back to evaluate it
  def read_DallasTemp1():
    f = open("/home/robin/DallasTemp1", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    volts = float(line2)
    return volts
  def read_DallasTemp2():
    f = open("/home/robin/DallasTemp2", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    volts = float(line2)
    return volts

  print "DallasTemp1: ", (round(read_DallasTemp1(),2))
  print "DallasTemp2: ", (round(read_DallasTemp2(),2))
