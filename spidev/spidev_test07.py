#!/usr/bin/python

import spidev
import time
import os

# Define Sensor channels
battery_voltage = 0
pott_voltage = 1

# Define Delay between readings
delay = 2

# Define number of loops through the program before exiting
count = 0

# Define Decimal places for Rounding Value
places = 2

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
while (count < 2):
# Read channel value on MCP3008
   batt_value = readadc(battery_voltage)
   pott_value = readadc(pott_voltage)
# Convert value into voltage
   batt_volts = ((batt_value*3.3)/1024)+10.85
   pott_volts = (pott_value*3.3)/1024
# Print Battery Values & Voltages
   print ("-" * 30)
   print "Battery Value = {}".format(batt_value)
   print "Battery Volts = {}".format(batt_volts)
# Print voltage rounded using ConvertVolts:
   rounded_batt_value = round(batt_value,places)
   print "Rounded Battery Value = {}".format(rounded_batt_value)
   rounded_batt_volts = ((rounded_batt_value*3.3)/1024)+10.85
   rounded_batt_volts = round(rounded_batt_volts,2)
   print "Rounded Battery Voltage = {}".format(rounded_batt_volts)
# Print Pott Values & Voltages
   print ("-" * 30)
   print "Pott Value = {}".format(pott_value)
   print "Pott Volts = {}".format(pott_volts)
# Print voltage rounded using ConvertVolts:
   rounded_pott_volts = ConvertVolts(pott_value,places)
   print "Rounded Pott Voltage = {}".format(rounded_pott_volts)
   time.sleep(delay)
   count = count + 1

