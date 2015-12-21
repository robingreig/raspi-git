#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import os
import glob
import warnings

DEBUG = 1

# ==========================================================================
# Generate beacon01.txt file
# ==========================================================================

# Add a delay for boot
time.sleep(2)

# Continuously append data
while(True):

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

  def read_CurrentHouseTemp():
    f = open("/home/robin/CurrentHouseTemp", "r")
    lines5 = f.read(5)
    f.close()
    if DEBUG > 0:
      print "lines5: ", lines5
    return lines5

  GarageTemp =str(read_CurrentGarageTemp())
  GarageTemp = float(GarageTemp)
  GarageTemp = round(GarageTemp,1)
  GarageTemp = str(GarageTemp)
  if DEBUG > 0:
    print "Garage Temp: ", GarageTemp
  OutsideTemp = str(read_CurrentOutsideTemp())
  if DEBUG > 0:
    print "Outside Temp: ", OutsideTemp  
  HouseTemp = str(read_CurrentHouseTemp())
  if DEBUG > 0:
    print "House Temp: ", HouseTemp  
  # Have to convert the OutsideTemp to a number between 0 & 255.
  # -40C will be the lowest temp to measure so add 40 to the temp 
  # and subtract 40 with the EQN in aprs.fi
  TelemetryTemp = float(OutsideTemp)
  TelemetryTemp = (TelemetryTemp + 40)
  TelemetryTemp = str(TelemetryTemp)
  if DEBUG > 0:
    print "TelemetryTemp: ", TelemetryTemp
  # Generate APRS Time for beacon01.txt
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
  
  time.sleep(2)
  
  sys.exit()
  #time.sleep(10)

