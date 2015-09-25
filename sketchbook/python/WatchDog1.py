#!/usr/bin/env python

import serial
import time
import subprocess

# Set Variables
count = 0
delay = 2
DEBUG = 0
maxcount = 3

#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=5)
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)

while True:
#while (count < maxcount):
  ser.flushInput()

  print "\nCount= {0}".format(count)
  #ok read all Analog
  for i in range(6):
    if DEBUG == 1:
	print "\ti={0}".format(i)
    ser.write(chr(48+i))
    line = ser.readline()
    voltage = float(line) + 10
#    print "\t 0-5V Voltage of A{0}=".format(i),
#    print "{0}".format(line),
#    print "\t10-12V Voltage of A{0}=".format(i),
#    print "{0}\n".format(voltage),
#    print "\n",

    if i == 0:
      cht = open("/home/robin/ReadVoltage0", "wb")
      cht.write(line);
      cht.close()
      print "\tVoltage of A{0}=".format(i),
      print "{0}\n".format(voltage),
      print "\n",
      if float(line) < 2.0 and float(line) > 1.5:
        print "\tVoltage is low\n"
      elif float(line) < 1.49 and float(line) > 1.0:
        print "\tVoltage is CRITICAL\n"
      elif float(line) <= 1.0:
        subprocess.call(["sudo", "shutdown", "-k", "now"])
    if i == 1:
      cht = open("/home/robin/ReadVoltage1", "wb")
      cht.write(line);
      cht.close()
    if i == 2:
      cht = open("/home/robin/ReadVoltage2", "wb")
      cht.write(line);
      cht.close()
    if i == 3:
      cht = open("/home/robin/ReadVoltage3", "wb")
      cht.write(line);
      cht.close()
    if i == 4:
      cht = open("/home/robin/ReadVoltage4", "wb")
      cht.write(line);
      cht.close()
    if i == 5:
      cht = open("/home/robin/ReadVoltage5", "wb")
      cht.write(line);
      cht.close()

  count = count +1
  time.sleep(delay)
