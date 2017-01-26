#!/usr/bin/python
'''*****************************************************************************************************************
    Pi Temperature Station
    By Robin Greig
    www.robingreig.ca
    This is a Raspberry Pi project that measures weather values (temperature, humidity and pressure)
    then uploads the data to a Weather Underground weather station.
********************************************************************************************************************'''

import urllib
import urllib2
import datetime
import os
import sys
import time

# ============================================================================
# Constants
# ============================================================================

Debug = 0

# Set to True to enable upload of weather data to Weather Underground
WEATHER_UPLOAD = True
#WEATHER_UPLOAD = False

# the weather underground URL used to upload weather data
WU_URL = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"
#WU_URL2 = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=IROCKYVI10&PASSWORD=nmxihjyz&dateutc=now&action=updateraw&tempf="
#WU_URL = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=IROCKYVI10&PASSWORD=nmxihjyz&dateutc=now&action=updateraw&tempf=28.0"

def read_CurrentOutsideTemp():
  f = open('/home/robin/CurrentOutsideTemp','r')
  lines5 = f.readlines()
  f.close()
  return lines5

def read_OutsideTemp():
  lines5 = read_CurrentOutsideTemp()
  temp_string = lines5[0]
  temp_c1 = float(temp_string)
  temp_f1 = (temp_c1 * 1.8) + 32
  return temp_f1

temp_f = (round(read_OutsideTemp(),1))

if Debug > 0:
  print "Outside Temp (round(read_OutsideTemp(),1)): ", (round(read_OutsideTemp(),1))
  print "Outside Temp (temp_f): ", temp_f

# ============================================================================
#  Read Weather Underground Configuration Parameters
# ============================================================================
if Debug > 0:
  print("\nInitializing Weather Underground configuration")
wu_station_id = 'IROCKYVI10'
wu_station_key = 'nmxihjyz'
if (wu_station_id is None) or (wu_station_key is None):
    print("Missing values from the Weather Underground configuration file\n")
    sys.exit(1)

# we made it this far, so it must have worked...
if Debug > 0:
  print("Successfully read Weather Underground configuration values")
  print("Station ID:", wu_station_id)
  print("Station key:", wu_station_key)

# ========================================================
# Upload the weather data to Weather Underground
# ========================================================
# is weather upload enabled (True)?
if WEATHER_UPLOAD:
  # From http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
  print("Uploading data to Weather Underground")
  # build a weather data object
  data = {}
  data['action'] = 'updateraw'
  data['ID'] = wu_station_id
  data['PASSWORD'] = wu_station_key
  data['dateutc'] = 'now'
  data['tempf'] = str(temp_f)
  url_values = urllib.urlencode(data)
  if Debug > 0:
    print "url_values are: ", url_values  

  try:
    upload_url = WU_URL + '?' + url_values
    response = urllib2.urlopen(upload_url)
    html = response.read()
    if Debug > 0:
      print "upload_url is: ", upload_url
      print "The URL is: ", response.geturl()
      print "The Response Info is: ", response.info()
    print("Server response:", html)
    # do something
    response.close()  # best practice to close the file
  except:
    print("Exception:", sys.exc_info()[0])
  
