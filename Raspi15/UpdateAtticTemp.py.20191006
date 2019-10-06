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
  device_folder4 = glob.glob(base_dir + '*539e')[0]
  device_file4 = device_folder4 + '/w1_slave'
 
  def read_temp_raw4():
      f = open(device_file4, 'r')
      lines4 = f.readlines()
      f.close()
      return lines4

  def read_temp4():
      lines4 = read_temp_raw4()
      while lines4[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines4 = read_temp_raw4()
      equals_pos = lines4[1].find('t=')
      if equals_pos != -1:
          temp_string = lines4[1][equals_pos+2:]
          temp_c4 = float(temp_string) / 1000.0
          return temp_c4

#  print "Garage Attic Temp: ", (round(read_temp4(),1))
  AtticTemp = (round(read_temp4(),1))
#  print "Garage Attic Temp: ", (round(read_temp4(),1))
  print "Garage Attic Temp: ", AtticTemp
#  OutsideTemp = (round(read_temp3(),1))
#  print "Outside Temp: ", OutsideTemp	

  cht = open("/home/robin/CurrentAtticTemp", "w")
  cht.write (str(AtticTemp))
  cht.close()

  break
