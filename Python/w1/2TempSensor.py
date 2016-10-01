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
  device_folder1 = glob.glob(base_dir + '*260c')[0]
  device_folder2 = glob.glob(base_dir + '*30e3')[0]
  device_file1 = device_folder1 + '/w1_slave'
  device_file2 = device_folder2 + '/w1_slave'
   
  def read_temp_raw1():
      f = open(device_file1, 'r')
      lines1 = f.readlines()
      f.close()
      return lines1

  def read_temp_raw2():
      f = open(device_file2, 'r')
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

  def read_temp2():
      lines1 = read_temp_raw2()
      while lines1[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines1 = read_temp_raw1()
      equals_pos = lines1[1].find('t=')
      if equals_pos != -1:
          temp_string = lines1[1][equals_pos+2:]
          temp_c1 = float(temp_string) / 1000.0
          return temp_c1

  TestTemp1 = round(read_temp1(),1)
  TestTemp2 = round(read_temp2(),1)

  if DEBUG > 0:
    print "Test Temp1 (rounded): ", TestTemp1
    print "Test Temp2 (rounded): ", TestTemp2
  
  cht = open("/home/robin/CurrentTestTemp1", "w")
  cht.write (str(TestTemp1))
  cht.close()

  cht = open("/home/robin/CurrentTestTemp2", "w")
  cht.write (str(TestTemp2))
  cht.close()

  print "Test Temp1: ", (read_temp1())
  print "Test Temp2: ", (read_temp2())
    	
  time.sleep(1)
  
  sys.exit()

