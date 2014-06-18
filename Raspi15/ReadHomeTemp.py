#!/usr/bin/python3

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
dbc = MySQLdb.connect(host= "192.168.200.15",
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
  device_folder1 = glob.glob(base_dir + '*3cb8')[0]
  device_file1 = device_folder1 + '/w1_slave'
  device_folder2 = glob.glob(base_dir + '*533e')[0]
  device_file2 = device_folder2 + '/w1_slave'
  device_folder3 = glob.glob(base_dir + '*41a4')[0]
  device_file3 = device_folder3 + '/w1_slave'
 
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

  def read_temp_raw3():
      f = open(device_file3, 'r')
      lines3 = f.readlines()
      f.close()
      return lines3

  def read_CurrentHouseTemp():
     f = open('/home/robin/CurrentHouseTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
  def read_CurrentOfficeTemp():
     f = open('/home/robin/CurrentOfficeTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
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

#  def read_temp5():
#	lines5 = read_CurrentHouseTemp()
#	temp_string = lines5[0]
#	temp_c5 = float(temp_string)
#	return temp_c5

#  def read_temp6():
#	lines5 = read_CurrentOfficeTemp()
#	temp_string = lines5[0]
#	temp_c6 = float(temp_string)
#	return temp_c6

  print ("Garage Desk Temp: ", (read_temp1()))
  print ("Garage Ceiling Temp: ", (read_temp2()))
  print ("Outside Temp: ", (read_temp3()))	
#  print ("House Temp: ", (read_temp5()))
#  print ("Office Temp: ", (read_temp6()))
  time.sleep(1)
  d = 20.0
  e = 20.0
  f = 20.0
  try:
    cursor.execute("""INSERT INTO garage_temp 
        (date, time, outside_temp, desk_temp, ceiling_temp, attic_temp, house_temp, office_temp) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s,%s);""",
	(read_temp3(), read_temp1(), read_temp2(), d, e, f))

    dbc.commit()
  except:
    dbc.rollback()

  print ("Wrote a new row to the database")

  break
dbc.close()
