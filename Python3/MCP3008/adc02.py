#!/usr/bin/env python3

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime

# To add delay
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0) 
# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data



# Below function will convert data to voltage
def Volts(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 2) # Round off to 2 decimal places
  return volts
 
while True:
  temp_output = analogInput(1) # Reading from CH0
  temp_volts = Volts(temp_output)                                                                                          
  x = datetime.datetime.now()
  print("vibration : {} {} ({}V)".format(temp_output,x,temp_volts))
  if (temp_output > 200):
    print ("The tap is ON")
  
  sleep(5)
