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
dbc = MySQLdb.connect(host= "raspi15.local",
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
#time.sleep(10)

# Continuously append data
while(True):

  def read_AprxVoltage():
     f = open('/home/robin/AprxVoltage', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 


  def AprxVoltageRead():
     lines0 = read_AprxVoltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       AprxVoltage = float(temp_string)
     else:
       AprxVoltage = 7.77
     return AprxVoltage

  def read_BlackTruckVoltage():
     f = open('/home/robin/ReadVoltage0', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 

  def BlackTruckRead():
     lines0 = read_BlackTruckVoltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       BlackTruckVoltage = float(temp_string)
     else:
       BlackTruckVoltage = 7.77
     return BlackTruckVoltage

  def read_GreyTruckVoltage():
     f = open('/home/robin/ReadVoltage1', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 

  def GreyTruckRead():
     lines0 = read_GreyTruckVoltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       GreyTruckVoltage = float(temp_string)
     else:
       GreyTruckVoltage = 7.77
     return GreyTruckVoltage

  def read_Bank1Voltage():
     f = open('/home/robin/ReadVoltage3', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 

  def Bank1Read():
     lines0 = read_Bank1Voltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       Bank1Voltage = float(temp_string)
     else:
       Bank1Voltage = 7.77
     return Bank1Voltage

  def read_Bank2Voltage():
     f = open('/home/robin/ReadVoltage4', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 

  def Bank2Read():
     lines0 = read_Bank2Voltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       Bank2Voltage = float(temp_string)
     else:
       Bank2Voltage = 7.77
     return Bank2Voltage

  def read_Bank3Voltage():
     f = open('/home/robin/ReadVoltage5', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 

  def Bank3Read():
     lines0 = read_Bank3Voltage()
     temp_string = lines0[0]
     # Test to see if the string is empty, if so, then assign a value of 7.77
     if temp_string and not temp_string.isspace():
       Bank3Voltage = float(temp_string)
     else:
       Bank3Voltage = 7.77
     return Bank3Voltage

 
  Voltage0 = (round(AprxVoltageRead(),2))
  print "APRX Voltage: ", Voltage0
  Voltage1 = (round(BlackTruckRead(),2))
  print "Black Truck Voltage: ", Voltage1
  Voltage2 = (round(GreyTruckRead(),2))
  print "Grey Truck Voltage: ", Voltage2
  Voltage3 = (round(Bank1Read(),2))
  print "Bank 1, A3, Orange Voltage: ", Voltage3
  Voltage4 = (round(Bank2Read(),2))
  print "Bank 2, A4, Green  Voltage: ", Voltage4
  Voltage5 = (round(Bank3Read(),2))
  print "Bank 3, A5, Blue Voltage: ", Voltage5
  time.sleep(1)


  try:
    cursor.execute("""INSERT INTO voltages 
        (date, time, voltage0, voltage1, voltage2, voltage3, voltage4, voltage5) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s,%s);""",
	((round(AprxVoltageRead(),2)), (round(BlackTruckRead(),2)), (round(GreyTruckRead(),2)), (round(Bank1Read(),2)), (round(Bank2Read(),2)), (round(Bank3Read(),2))))

    dbc.commit()
  except:
    dbc.rollback()

  print "Wrote a new row to the database"

  break
dbc.close()
