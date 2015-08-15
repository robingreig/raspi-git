#!/usr/bin/python

import spidev
import time
import os

# Define Sensor channels
battery_voltage = 0

# Define Delay between readings
delay = 3

# Define number of loops through the program before exiting
count = 0

# Define Decimal places for Rounding Value
places = 3

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

# Function to convert data to voltage level
# rounded to specified number of decimal places
def ConvertVolts(adcout,places):
    volts = (adcout * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

#while True:
while (count < 9):
# Read value of CH0 on MCP3008
   value01 = readadc(battery_voltage)
# Convert value into voltage
   volts = (value01*3.3)/1024
# Print Value & Voltage
   print "Value = {}".format(value01)
   print "Volts = {}".format(volts)
# Print voltage rounded using ConvertVolts:
   rounded_volts = ConvertVolts(value01,places)
   print "Rounded Voltage = {}".format(rounded_volts)
# Print voltage using original authors formula
   print ("%4d/1023 => %5.3f V " %(value01, volts))
   print "---------------------------------------------"
   time.sleep(delay)
   count = count + 1

