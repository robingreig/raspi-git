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

DEBUG = 1

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Hostname, User, Password, Database
dbc = MySQLdb.connect(host= "localhost",
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
#  device_folder1 = glob.glob(base_dir + '*27c2')[0]
  device_folder1 = glob.glob(base_dir + '*3484')[0]
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

  def read_CurrentOutsideTemp():
    f = open("/home/robin/CurrentOutsideTemp", "r")
    lines3 = f.read(5)
    f.close()
    if DEBUG > 0:
      print "lines3: ", lines3
    return lines3

  def read_CurrentGarageTemp():
    f = open("/home/robin/CurrentGarageTemp", "r")
    lines4 = f.read(5)
    f.close()
    if DEBUG > 0:
      print "lines4: ", lines4
    return lines4

  GarageTemp =str(read_CurrentGarageTemp())
  GarageTemp = float(GarageTemp)
  GarageTemp = round(GarageTemp,1)
  GarageTemp = str(GarageTemp)
  if DEBUG > 0:
    print "Garage Temp: ", GarageTemp
  OutsideTemp = str(read_CurrentOutsideTemp())
  if DEBUG > 0:
    print "Outside Temp: ", OutsideTemp  
  # Have to convert the OutsideTemp to a number between 0 & 255.
  # -40C will be the lowest temp to measure so add 40 to the temp 
  # and subtract 40 with the EQN in aprs.fi
  TelemetryTemp = float(OutsideTemp)
  TelemetryTemp = (TelemetryTemp + 40)
  TelemetryTemp = str(TelemetryTemp)
  if DEBUG > 0:
    print "TelemetryTemp: ", TelemetryTemp
  HouseTemp = round(read_temp1(),1)
  if DEBUG > 0:
    print "House Temp: ", HouseTemp
  aprs_hour = int(time.strftime("%H"))
  if DEBUG > 0:
    print "aprs_hour: ", aprs_hour
  aprs_minute = int(time.strftime("%M"))
  if DEBUG > 0:
    print "aprs_minute: ", aprs_minute
  aprs_time = int((aprs_hour * 60) + (aprs_minute))
  if DEBUG > 0:
    print "aprs_time: ", aprs_time
  aprs_unique = ((aprs_time)/4)
  if DEBUG > 0:
    print "aprs_unique: ", int(aprs_unique)

  cht = open("/home/robin/beacon01.txt", "w")
  #cht.write(str(read_temp1()))
  cht.write ("T#")
  cht.write (str(aprs_unique))
  cht.write (",")
  cht.write (str(HouseTemp)) 
  cht.write (",")
  cht.write (str(TelemetryTemp))
  cht.write (",")
  cht.write (str(GarageTemp))
  cht.write(",0,0,00000000")
  cht.close()
  
  cht = open("/home/robin/CurrentHouseTemp", "w")
  cht.write (str(HouseTemp))
  cht.close()
    	
  time.sleep(1)
  
  try:
    cursor.execute("""INSERT INTO house_stats 
        (date, time, house_temp) 
	VALUES 
	(NOW(),NOW(),%s);""",
	(read_temp1()))

    dbc.commit()
  except:
    dbc.rollback()

  # Wait 60 seconds before continuing
  print "Wrote a new row to the database"
  sys.exit()
  #time.sleep(10)

dbc.close()
