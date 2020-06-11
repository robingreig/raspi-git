#!/usr/bin/env python3

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime
import os

# Variables
DEBUG = 0
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

for i in range(ports):
  inputAvg = 0
  for j in range(3): # Take 3 samples to average out
    input = analogInput(i) # Reading from port number
    if DEBUG > 0:
      print("Port Number = %d"%i)
      print("Port value = %d"%input)
    inputAvg = inputAvg + input # Add all 3 entries
  inputAvg = inputAvg / 3 # Average all 3 entries
  inputAvg = round(inputAvg,0) # Round Average
  if inputAvg < 470: # if inputAvg < 470, probe is saturated
    inputAvg = 470 # Zero it to 470, fully wet
  # Range is 470 (wet) & 870 (dry)
  percentAvg = ((inputAvg - 470) / 4) # Range - 470 / 4 will give percent dry
  percentAvg = (100 - percentAvg) # Reverse % to show how % wet
  if percentAvg < 0: # if percentAvg is negative, units > 870
    percentAvg = 0
  if DEBUG > 0:
    print("inputAvg = %d"%inputAvg)
    timestamp = datetime.datetime.now()
    print("\nInput 0: {} ({} Bits) ({} Average Percent)".format(timestamp, input,inputAvg))
    print("Percent Adjusted Average = %d"%percentAvg)
  file_name = '/home/robin/CurrentADC{}'.format(i)
  if DEBUG > 0:
    print(file_name)
  cht = open(file_name, "w")
  cht.write (str(percentAvg))
  cht.close()
  sleep(sleepTime)

