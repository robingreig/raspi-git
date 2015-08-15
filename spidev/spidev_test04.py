#!/usr/bin/python

import spidev
import time
import os

# Open SPI Bus
spi=spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7

def readadc(adcnum):
   if adcnum > 7 or adcnum< 0:
      return -1
   r= spi.xfer2([1, 8 + adcnum << 4, 0])
   adcout = ((r[1] & 3)<< 8) +r [2]
   return adcout


while True:
# Read value of CH0 on MCP3008
   value = readadc(0)
# Convert value into voltage
   volts = (value*3.3)/1024
# Print Value & Voltage
   print (value)
   print (volts)
   print ("%4d/1023 => %5.3f V " %(value, volts))
   print (-5.8296*(volts)**3+36.327*(volts)**2-74.48*(volts)+56.733)
   time.sleep(2)
