#!/usr/bin/env python

import subprocess
import re
import sys
import time
import datetime
import os
import glob
import warnings

DEBUG = 0

# Add a delay for boot
time.sleep(1)

# Continuously append data
while(True):

  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder1 = glob.glob(base_dir + '*27c2')[0]
#  device_folder1 = glob.glob(base_dir + '*284a')[0]
#  device_folder1 = glob.glob(base_dir + '*2af2')[0]
#  device_folder1 = glob.glob(base_dir + '*5c8c')[0]
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
    print "Basement Temp (rounded): ", BasementTemp
  
  cht = open("/home/robin/BasementTemp", "w")
  cht.write (str(BasementTemp))
  cht.close()

  print "Basement Temp: ", (read_temp1())
    	
  time.sleep(1)
  
  sys.exit()

