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
  device_folder2 = glob.glob(base_dir + '*533e')[0]
  device_file2 = device_folder2 + '/w1_slave'

  def read_temp_raw2():
      f = open(device_file2, 'r')
      lines2 = f.readlines()
      f.close()
      return lines2

  def read_temp2():
      lines2 = read_temp_raw2()
      while lines2[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines2 = read_temp_raw2()
      equals_pos = lines2[1].find('t=')
      if equals_pos != -1:
          temp_string = lines2[1][equals_pos+2:]
          temp_c2 = float(temp_string) / 1000.0
          return temp_c2

  CeilingTemp = (round(read_temp2(),1))
#  print "Garage Ceiling Temp: ", (round(read_temp2(),1))
  print "Garage Ceiling Temp: ", CeilingTemp

#  OutsideTemp = (round(read_temp3(),1))
#  print "Outside Temp: ", OutsideTemp	

  cht = open("/home/robin/CurrentCeilingTemp", "w")
  cht.write (str(CeilingTemp))
  cht.close()

  break
