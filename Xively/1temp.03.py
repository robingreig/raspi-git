#!/usr/bin/env python

import datetime
import glob
import os
import subprocess
import sys
import time
import xively

# extract feed_id and api_key from environment variables
#FEED_ID = os.environ["FEED_ID"]
FEED_ID = "1760791802"
#API_KEY = os.environ["API_KEY"]
API_KEY = "kU8fGNND5nbRCWnYf8Nx4Rs1HgPj3AIHFDwopKDMr0An1nMP"
#DEBUG = os.environ["DEBUG"] or false
DEBUG = 1

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# Continuously append data
while(True):

  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder1 = glob.glob(base_dir + '*2902')[0]
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

  print "Office Temp: ", (read_temp1())
    	
  break

# function to return a datastream object. This either creates a new datastream,
# or returns an existing one
def get_datastream(feed):
  try:
    datastream = feed.datastreams.get("temp_sensor01")
    if DEBUG:
      print "Found existing datastream"
    return datastream
  except:
    if DEBUG:
      print "Creating new datastream"
    datastream = feed.datastreams.create("temp_sensor01", tags="garage_temp")
    return datastream

# main program entry point - runs continuously updating our datastream with the
# current 1 minute load average
def run():
  print "Starting Xively tutorial script"

  feed = api.feeds.get(FEED_ID)

  datastream = get_datastream(feed)
  datastream.max_value = None
  datastream.min_value = None

  while True:
    garage_temp = read_temp1()

    if DEBUG:
      print "Updating Xively feed with value: %s" % garage_temp

    datastream.current_value = garage_temp
    datastream.at = datetime.datetime.utcnow()
    try:
      datastream.update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)

    time.sleep(10)

run()


