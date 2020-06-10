#!/usr/bin/env python3

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime
import os

# Variables
DEBUG = 1
sleepTime = 1
ports = 1 # Number of ports being read


# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Below function will convert data to percentage
def water(data):
  water = ((data / 870 * 100) # convert to percentage
  water = 100 - water # reverse percentage
  return water


for i in range(ports):
  input = analogInput(ports) # Reading from port number
  print("Port value = %d"%input)
#  input0Avg = input0Avg + input0 # Average all 3 entries
#  timestamp = datetime.datetime.now()
#  print("\nInput 0: {} ({} Bits) ({} Bits Average)".format(timestamp, input0,input0Avg))
#  if repeat == 1:
#    input0Avg = input0Avg / 3
#    input0Avg = round(input0Avg, 2) # Round off to 2 decimal places
#    print("\nInput 0: {} ({} Bits) ({} Bits Average) ".format(timestamp, input0,input0Avg))
#    cht = open("/home/robin/CurrentAdc0", "w")
#    cht.write (str(input0Avg))
#    cht.close()
#  sleep(sleepTime)
#  repeat = repeat - 1
