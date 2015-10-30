#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import MySQLdb
import os
import glob
import warnings

while(True):

  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder1 = glob.glob(base_dir + '*3cb8')[0]
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

  GarageTemp = (round(read_temp1(),1))
  print "Garage Desk Temp: ", (round(read_temp1(),1))

  cht = open("/home/robin/CurrentDeskTemp", "w")
  cht.write (str(GarageTemp))
  cht.close()

  break
