#!/usr/bin/env python3

import time
import datetime
#import MySQLdb
import pymysql
import warnings
import RPi.GPIO as GPIO

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Hostname, User, Password, Database
#dbc = MySQLdb.connect(host= "raspi15.local",
dbc = pymysql.connect(host= "localhost",
	user= "robin",
	passwd= "Micr0s0ft",
	db= "house_stats")

# Prepare a cursor
cursor = dbc.cursor()

# ==========================================================================
# Filter Warnings
# ==========================================================================

warnings.filterwarnings('ignore', category=pymysql.Warning)


# ==========================================================================
# Insert into table - variable
# ==========================================================================

# Continuously append data
while(True):

  pinNum0 = 21
  pinNum1 = 20
  pinNum2 = 16
  pinNum3 = 26
  pinNum4 = 19
  pinNum5 = 13
  pinNum6 = 6
  pinNum7 = 5
  pinNum8 = 22
  pinNum9 = 27
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
  GPIO.setup(pinNum0,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum1,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum2,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum3,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum4,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum5,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum6,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum7,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum8,GPIO.IN) #setup pinNum as an input
  GPIO.setup(pinNum9,GPIO.IN) #setup pinNum as an input

  state0 = GPIO.input(pinNum0)
  state1 = GPIO.input(pinNum1)
  state2 = GPIO.input(pinNum2)
  state3 = GPIO.input(pinNum3)
  state4 = GPIO.input(pinNum4)
  state5 = GPIO.input(pinNum5)
  state6 = GPIO.input(pinNum6)
  state7 = GPIO.input(pinNum7)
  state8 = GPIO.input(pinNum8)
  state9 = GPIO.input(pinNum9)

  if (state0):
      print ("Pin 21 is ON")
  else:
    print ("Pin 21 is OFF")
  if (state0 == 0):
    print ("State0 = 0")
  if (state0 == 1):
    print ("State0 = 1")

  try:
    cursor.execute("""INSERT INTO battmon 
       (date, time, voltage0, voltage1,voltage2,voltage3,voltage4,voltage5,voltage6,voltage7,voltage8,voltage9) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
	(state0,state1,state2,state3,state4,state5,state6,state7,state8,state9))
    dbc.commit()

  except:
    dbc.rollback()

  if cursor.lastrowid:
    print ('Number of rows updated: ', cursor.rowcount)
    print('Last insert id: ', cursor.lastrowid)
  else:
    print('Last insert id not found')

  break
dbc.close()


