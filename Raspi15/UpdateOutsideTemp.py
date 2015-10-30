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
#  device_folder3 = glob.glob(base_dir + '*41a4')[0]
  device_folder3 = glob.glob(base_dir + '*5e62')[0]
  device_file3 = device_folder3 + '/w1_slave'
 
  def read_temp_raw3():
      f = open(device_file3, 'r')
      lines3 = f.readlines()
      f.close()
      return lines3

  def read_temp3():
      lines3 = read_temp_raw3()
      while lines3[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines3 = read_temp_raw3()
      equals_pos = lines3[1].find('t=')
      if equals_pos != -1:
          temp_string = lines3[1][equals_pos+2:]
          temp_c3 = float(temp_string) / 1000.0
          return temp_c3

  OutsideTemp = (round(read_temp3(),1))
  print "Outside Temp: ", OutsideTemp	

  cht = open("/home/robin/CurrentOutsideTemp", "w")
  cht.write (str(OutsideTemp))
  cht.close()

  break
