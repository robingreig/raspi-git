#!/usr/bin/env python3

#====================================================================
# Import subfiles
#====================================================================
import datetime
import glob
import os
import re
#import serial
import subprocess
import sys
import time
import warnings

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('robingreig', '7e01e8b5e56360efc48a27682324fc353e18d14f')

# Set Variables
DEBUG = 1

# Add a delay for boot
time.sleep(1)

# Continuously append data
while(True):

#  os.system('modprobe w1-gpio')
#  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
#  device_folder1 = glob.glob(base_dir + '*27c2')[0]
#  device_folder1 = glob.glob(base_dir + '*284a')[0]
#  device_folder1 = glob.glob(base_dir + '*2af2')[0]
  device_folder1 = glob.glob(base_dir + '*5c8c')[0]
  device_file1 = device_folder1 + '/w1_slave'
   
  def read_temp_raw1():
      f = open(device_file1, 'r')
      lines1 = f.readlines()
      f.close()
      return lines1

  def read_temp1():
      lines1 = read_temp_raw1()
      while lines1[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines1 = read_temp_raw1()
      equals_pos = lines1[1].find('t=')
      if equals_pos != -1:
          temp_string = lines1[1][equals_pos+2:]
          temp_c1 = float(temp_string) / 1000.0
          return temp_c1

  BasementTemp = round(read_temp1(),1)

  if DEBUG > 0:
    print ("Basement Temp before writing to file (rounded): ", BasementTemp)
  
  cht = open("/home/robin/CurrentBasementTemp", "w")
  cht.write (str(BasementTemp))
  cht.close()
  time.sleep(1)

  # Read the Current Basement Temperature
  def read_CurrentBasementTemp():
    f = open("/home/robin/CurrentBasementTemp", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    BasementTemp = float(line2)
    return BasementTemp

  BasementTempRound = (round(read_CurrentBasementTemp(),2))

  if DEBUG > 0:
    print ("Basement Temp File reads: ", read_CurrentBasementTemp())
    print ("Basement Temp Rounded: ", BasementTempRound)

  # Send the value 100 to a feed called 'Foo'.
  #aio.send('basement-temp', 19.8)
  aio.send('basement-temp', BasementTempRound)

  # Retrieve the most recent value from the feed 'Foo'.
  # Access the value by reading the `value` property on the returned Data object.
  # Note that all values retrieved from IO are strings so you might need to convert
  # them to an int or numeric type if you expect a number.
  data = aio.receive('basement-temp')
  if DEBUG > 0:
    print('Received value: {0}'.format(data.value))
  sys.exit()

