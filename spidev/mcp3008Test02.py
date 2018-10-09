#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Define sensor channels
channel_0 = 0
channel_1 = 1
channel_2 = 2
channel_3 = 3
channel_4 = 4
channel_5 = 5
channel_6 = 6
channel_7 = 7
 
# Define delay between readings
delay = 2
 
while True:
 
  # Read the mcp3008 data
  channel0_level = ReadChannel(channel_0)
  channel1_level = ReadChannel(channel_1)
  channel2_level = ReadChannel(channel_2)
  channel3_level = ReadChannel(channel_3)
  channel4_level = ReadChannel(channel_4)
  channel5_level = ReadChannel(channel_5)
  channel6_level = ReadChannel(channel_6)
  channel7_level = ReadChannel(channel_7)

  # Convert data to voltage
  channel0_volts = ConvertVolts(channel0_level,2)
  channel1_volts = ConvertVolts(channel1_level,2)
  channel2_volts = ConvertVolts(channel2_level,2)
  channel3_volts = ConvertVolts(channel3_level,2)
  channel4_volts = ConvertVolts(channel4_level,2)
  channel5_volts = ConvertVolts(channel5_level,2)
  channel6_volts = ConvertVolts(channel6_level,2)
  channel7_volts = ConvertVolts(channel7_level,2)
 
  # Print out results
  print "--------------------------------------------"
  print("Channel: {}     {}     ({}V)".format(channel_0,channel0_level,channel0_volts))
  print("Channel: {}     {}     ({}V)".format(channel_1,channel1_level,channel1_volts))
  print("Channel: {}     {}     ({}V)".format(channel_2,channel2_level,channel2_volts))
  print("Channel: {}     {}     ({}V)".format(channel_3,channel3_level,channel3_volts))
  print("Channel: {}     {}     ({}V)".format(channel_4,channel4_level,channel4_volts))
  print("Channel: {}     {}     ({}V)".format(channel_5,channel5_level,channel5_volts))
  print("Channel: {}     {}     ({}V)".format(channel_6,channel6_level,channel6_volts))
  print("Channel: {}     {}     ({}V)".format(channel_7,channel7_level,channel7_volts))
 
  # Wait before repeating loop
  time.sleep(delay)
