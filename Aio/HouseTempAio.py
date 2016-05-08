#!/usr/bin/env python

#====================================================================
# Import subfiles
#====================================================================
import datetime
import glob
import os
import re
import serial
import subprocess
import sys
import time
import warnings

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Set Variables
DEBUG = 1

# Add a delay for boot
time.sleep(1)

# Continuously append data
while(True):

  time.sleep(1)

  # Read the Current Garage Temperature
  def read_CurrentHouseTemp():
    f = open("/home/robin/CurrentHouseTemp", "r")
    line1 = f.readlines()
    f.close
    line2 = line1[0]
    HouseTemp = float(line2)
    return HouseTemp

  HouseTempRound = (round(read_CurrentHouseTemp(),2))

  if DEBUG > 0:
    print "House Temp File reads: ", read_CurrentHouseTemp()
    print "House Temp Rounded: ", HouseTempRound

  # Send the value 100 to a feed called 'Foo'.
  #aio.send('basement-temp', 19.8)
  aio.send('house-temp', HouseTempRound)

  # Retrieve the most recent value from the feed 'Foo'.
  # Access the value by reading the `value` property on the returned Data object.
  # Note that all values retrieved from IO are strings so you might need to convert
  # them to an int or numeric type if you expect a number.
  data = aio.receive('house-temp')
  if DEBUG > 0:
    print('Received value: {0}'.format(data.value))
  sys.exit()

