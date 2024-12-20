#!/usr/bin/env python3

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime

# Variables
DEBUG = 1
sleepTime = 1
repeat = 3

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
while repeat > 0:
  input0 = analogInput(0) # Reading from CH0
  input0_volts = Volts(input0)
  timestamp = datetime.datetime.now()
  print("\nInput 0: {} ({} Bits) ({}V)".format(timestamp, input0,input0_volts))
  input1 = analogInput(1) # Reading from CH1
  input1_volts = Volts(input1)
  print("Input 1: {} ({} Bits) ({}V)".format(timestamp, input1,input1_volts))
  input2 = analogInput(2) # Reading from CH2
  input2_volts = Volts(input2)
  print("Input 2: {} ({} Bits) ({}V)".format(timestamp, input2,input2_volts))
  input3 = analogInput(3) # Reading from CH3
  input3_volts = Volts(input3)
  print("Input 3: {} ({} Bits) ({}V)".format(timestamp, input3,input3_volts))
  input4 = analogInput(4) # Reading from CH4
  input4_volts = Volts(input4)
  print("Input 4: {} ({} Bits) ({}V)".format(timestamp, input4,input4_volts))
  input5 = analogInput(5) # Reading from CH5
  input5_volts = Volts(input5)
  print("Input 5: {} ({} Bits) ({}V)".format(timestamp, input5,input5_volts))
  sleep(sleepTime)
  repeat = repeat - 1
