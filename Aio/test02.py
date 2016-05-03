#!/usr/bin/env python

#====================================================================
# Import subfiles
#====================================================================
import datetime
import serial
import subprocess
import sys
import time
import warnings

# Set Variables
DEBUG = 1

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Read the Current Basement Temperature
def read_CurrentBasementTemp():
  f = open("/home/robin/BasementTemp", "r")
  line1 = f.readlines()
  f.close
  line2 = line1[0]
  BasementTemp = float(line2)
  return BasementTemp

BasementTempRound = (round(read_CurrentBasementTemp(),2))

if DEBUG == 1:
  print "BasementTemp: ", read_CurrentBasementTemp()
  print "BasementTempRound: ", BasementTempRound

# Send the value 100 to a feed called 'Foo'.
#aio.send('basement-temp', 19.8)
aio.send('basement-temp', BasementTempRound)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('basement-temp')
if DEBUG == 1:
  print('Received value: {0}'.format(data.value))

