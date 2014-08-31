#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO
import eeml
 
GPIO.setmode(GPIO.BCM)

LOGGER = 1
 
# COSM variables. The API_KEY and FEED are specific to your COSM account and must be changed
#API_KEY = '5RNOO3ShYJxYiq2V2sgSRtz3112SAKxFQjNDQmNXc0RScz0g'
#FEED = 68872
API_KEY = 'kU8fGNND5nbRCWnYf8Nx4Rs1HgPj3AIHFDwopKDMr0An1nMP'
FEED = 1760791802

Temp = 21

API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)
 
if LOGGER:
  # open up your cosm feed
  pac = eeml.Pachube(API_URL, API_KEY)
 
  #send celsius data
  pac.update([eeml.Data("temp_sensor01", Temp, unit=eeml.Celsius())])
  pac.update([eeml.Data(1, Temp, unit=eeml.Celsius())])
 
  # send data to cosm
  pac.put()
 
