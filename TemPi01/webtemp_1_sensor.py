#!/usr/bin/env python

import subprocess
import re
import sys
import time
import datetime
#import MySQLdb
import os
import glob
#import warnings

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Hostname, User, Password, Database
#dbc = MySQLdb.connect(host= "localhost",
#	user= "robin",
#	passwd= "raspberry",
#	db= "dms_stats")

# Prepare a cursor
#cursor = dbc.cursor()

# ==========================================================================
# Filter Warnings
# ==========================================================================

#warnings.filterwarnings('ignore', category=MySQLdb.Warning)


# ==========================================================================
# Insert into table - variable
# ==========================================================================

# Add a delay for boot
time.sleep(2)

# Continuously append data
while(True):

#  os.system('modprobe w1-gpio')
#  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder1 = glob.glob(base_dir + '*64ff')[0]
  device_file1 = device_folder1 + '/w1_slave'
#  device_folder2 = glob.glob(base_dir + '*3796')[0]
#  device_file2 = device_folder2 + '/w1_slave'
   
  def read_temp_raw1():
      f = open(device_file1, 'r')
      lines1 = f.readlines()
      f.close()
      return lines1

#  def read_temp_raw2():
#      f = open(device_file2, 'r')
#      lines2 = f.readlines()
#      f.close()
#      return lines2

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

#  def read_temp2():
#      lines2 = read_temp_raw2()
#      while lines2[0].strip()[-3:] != 'YES':
#          time.sleep(0.2)
#          lines2 = read_temp_raw2()
#      equals_pos = lines2[1].find('t=')
#      if equals_pos != -1:
#          temp_string = lines2[1][equals_pos+2:]
#          temp_c2 = float(temp_string) / 1000.0
#          return temp_c2

  MapleHouseTemp = (read_temp1())
#  print "Maple Creek House Temp: ", (read_temp1())
  print "Maple Creek House Temp: ", str(MapleHouseTemp)
#  print "E119 Temp: ", (read_temp2())
  cht = open("/home/robin/MapleHouseTemp", "w")
  cht.write(str(MapleHouseTemp))
  cht.close()
  	
  time.sleep(1)
  break 
#  try:
#    cursor.execute("""INSERT INTO dms_temp 
#        (date, time, dms_temp, E119_temp)
#	VALUES 
#	(NOW(),NOW(),%s,%s);""",
#	(read_temp1(), read_temp2()))

#    dbc.commit()
#  except:
#    dbc.rollback()

  # Wait 60 seconds before continuing
#  print "Wrote a new row to the database"
#  if read_temp1() > 25:
#    os.system("echo 'Overtemp!!!' | mail -s 'DMS Overtemp' robin.greig@calalta.com")
#    print "Sent an alert email"
#  sys.exit()
  #time.sleep(10)

#dbc.close()
