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

  def read_voltage0():
     f = open('/home/robin/ReadVoltage0', 'r')
     lines0 = f.readlines()
     f.close()
     return lines0 


  def read_voltage00():
        lines0 = read_voltage0()
        temp_string = lines0[0]
        voltage00 = float(temp_string)
        return voltage00

 
  Voltage0 = (round(read_voltage00(),2))
  print "Voltage0: ", Voltage0
  time.sleep(1)


#  cht = open("/home/robin/CurrentOutsideTemp", "w")
#  cht.write (str(OutsideTemp))
#  cht.close()

  try:
    cursor.execute("""INSERT INTO voltages 
        (date, time, voltage0) 
	VALUES 
	(NOW(),NOW(),%s);""",
	((round(read_voltage00(),2))))

    dbc.commit()
  except:
    dbc.rollback()

  print "Wrote a new row to the database"

  break
dbc.close()
