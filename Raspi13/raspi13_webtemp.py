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

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Hostname, User, Password, Database
dbc = MySQLdb.connect(host= "raspi34.local",
	user= "robin",
	passwd= "Micr0s0ft",
	db= "house_stats")

# Prepare a cursor
cursor = dbc.cursor()

# ==========================================================================
# Filter Warnings
# ==========================================================================

warnings.filterwarnings('ignore', category=MySQLdb.Warning)


# ==========================================================================
# Insert into table - variable
# ==========================================================================

# Add a delay for boot
time.sleep(10)

# Continuously append data
while(True):

  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder1 = glob.glob(base_dir + '*2902')[0]
  device_file1 = device_folder1 + '/w1_slave'
  device_folder2 = glob.glob(base_dir + '*4478')[0]
  device_file2 = device_folder2 + '/w1_slave'
 
  def read_temp_raw1():
      f = open(device_file1, 'r')
      lines1 = f.readlines()
      f.close()
      return lines1

  def read_temp_raw2():
      f = open(device_file2, 'r')
      lines2 = f.readlines()
      f.close()
      return lines2
 
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
      lines2 = read_temp_raw2()
      while lines2[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines2 = read_temp_raw2()
      equals_pos = lines2[1].find('t=')
      if equals_pos != -1:
          temp_string = lines2[1][equals_pos+2:]
          temp_c2 = float(temp_string) / 1000.0
          return temp_c2

  print "Garden Cold Frame Temp: ", (round(read_temp1(),1))
  print "Garden Outside Temp: ", (round(read_temp2(),1))
  time.sleep(1)
  d = 0.0
  e = 0.0
  f = 0.0
  try:
    cursor.execute("""INSERT INTO garden_temp 
        (date, time, garden_temp1, garden_temp2, garden_temp3, garden_temp4, garden_temp5) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s);""",
	((round(read_temp1(),1)), (round(read_temp2(),1)), d, e, f))

    dbc.commit()
  except:
    dbc.rollback()

  print "Wrote a new row to the database"

  break
dbc.close()
