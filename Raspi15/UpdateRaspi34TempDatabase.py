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

# Continuously append data
while(True):

  def read_CurrentOutsideTemp():
     f = open('/home/robin/CurrentOutsideTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
  def read_CurrentDeskTemp():
     f = open('/home/robin/CurrentDeskTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
  def read_CurrentCeilingTemp():
     f = open('/home/robin/CurrentCeilingTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
  def read_CurrentAtticTemp():
     f = open('/home/robin/CurrentAtticTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
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
 
  def read_CurrentCarefreeTemp():
     f = open('/home/robin/CurrentCarefreeTemp', 'r')
     lines5 = f.readlines()
     f.close()
     return lines5
 
  def read_OutsideTemp():
	lines5 = read_CurrentOutsideTemp()
	temp_string = lines5[0]
	temp_c1 = float(temp_string)
	return temp_c1

  def read_DeskTemp():
	lines5 = read_CurrentDeskTemp()
	temp_string = lines5[0]
	temp_c2 = float(temp_string)
	return temp_c2

  def read_CeilingTemp():
	lines5 = read_CurrentCeilingTemp()
	temp_string = lines5[0]
	temp_c3 = float(temp_string)
	return temp_c3

  def read_AtticTemp():
	lines5 = read_CurrentAtticTemp()
	temp_string = lines5[0]
	temp_c4 = float(temp_string)
	return temp_c4

  def read_HouseTemp():
	lines5 = read_CurrentHouseTemp()
	temp_string = lines5[0]
	temp_c5 = float(temp_string)
	return temp_c5

  def read_OfficeTemp():
	lines5 = read_CurrentOfficeTemp()
	temp_string = lines5[0]
	temp_c6 = float(temp_string)
	return temp_c6

  def read_CarefreeTemp():
	lines5 = read_CurrentCarefreeTemp()
	temp_string = lines5[0]
	temp_c7 = float(temp_string)
	return temp_c7

  print "Outside Temp: ", (round(read_OutsideTemp(),1))
  print "Desk Temp: ", (round(read_DeskTemp(),1))
  print "Ceiling Temp: ", (round(read_CeilingTemp(),1))
  print "Attic Temp: ", (round(read_AtticTemp(),1))
  print "House Temp: ", (round(read_HouseTemp(),1))
  print "Office Temp: ", (round(read_OfficeTemp(),1))
  print "Carefree Temp: ", (round(read_CarefreeTemp(),1))

  try:
    cursor.execute("""INSERT INTO garage_temp 
        (date, time, outside_temp, desk_temp, ceiling_temp, attic_temp, house_temp, office_temp, maple_house) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s,%s,%s);""",
	((round(read_OutsideTemp(),1)), (round(read_DeskTemp(),1)), (round(read_CeilingTemp(),1)), (round(read_AtticTemp(),1)), (round(read_HouseTemp(),1)), (round(read_OfficeTemp(),1)), (round(read_CarefreeTemp(),1))))

    dbc.commit()
  except:
    dbc.rollback()

  print "Wrote a new row to the database"

  break
dbc.close()
