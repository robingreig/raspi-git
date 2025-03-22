#!/usr/bin/env python3

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime
import os

# Variables
DEBUG = 1
sleepTime = 1
repeat = 3
input0voltsAvg = 0
input1voltsAvg = 0
input2voltsAvg = 0
input3voltsAvg = 0
input4voltsAvg = 0
input5voltsAvg = 0

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Below function will convert data to max 15VDC
def Volts24(data):
#  volts = (data * 3.3) / float(1023)
  volts = (data * 0.026392961)
  volts = round(volts, 2) # Round off to 2 decimal places
  return volts
# Below function will convert data to max 27VDC
def Volts12(data):
  volts = (data * 0.014662756)
  volts = round(volts, 2) # Round off to 2 decimal places
  return volts
while repeat > 0:
  input0 = analogInput(0) # Reading from CH0
  input0_volts = Volts24(input0)
  input0voltsAvg = input0voltsAvg + input0_volts # Average all 3 entries
  timestamp = datetime.datetime.now()
  print("\nInput 0: {} ({} Bits) ({}V) ({}V)".format(timestamp, input0,input0_volts,input0voltsAvg))
  if repeat == 1:
    input0voltsAvg = input0voltsAvg / 3
    input0voltsAvg = round(input0voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 0: {} ({} Bits) ({}V) ({}V)".format(timestamp, input0,input0_volts,input0voltsAvg))
    cht = open("/home/robin/CurrentAdc0Volts", "w")
    cht.write (str(input0voltsAvg))
    cht.close()
  input1 = analogInput(1) # Reading from CH1
  input1_volts = Volts24(input1)
  input1voltsAvg = input1voltsAvg + input1_volts # Average all 3 entries
  print("Input 1: {} ({} Bits) ({}V) ({}V)".format(timestamp, input1,input1_volts,input1voltsAvg))
  if repeat == 1:
    input1voltsAvg = input1voltsAvg / 3
    input1voltsAvg = round(input1voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 1: {} ({} Bits) ({}V) ({}V)".format(timestamp, input1,input1_volts,input1voltsAvg))
    cht = open("/home/robin/CurrentAdc1Volts", "w")
    cht.write (str(input1voltsAvg))
    cht.close()
  input2 = analogInput(2) # Reading from CH2
  input2_volts = Volts12(input2)
  input2voltsAvg = input2voltsAvg + input2_volts # Average all 3 entries
  print("Input 2: {} ({} Bits) ({}V) ({}V)".format(timestamp, input2,input2_volts,input2voltsAvg))
  if repeat == 1:
    input2voltsAvg = input2voltsAvg / 3
    input2voltsAvg = round(input2voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 2: {} ({} Bits) ({}V) ({}V)".format(timestamp, input2,input2_volts,input2voltsAvg))
    cht = open("/home/robin/CurrentAdc2Volts", "w")
    cht.write (str(input2voltsAvg))
    cht.close()
  input3 = analogInput(3) # Reading from CH3
  input3_volts = Volts12(input3)
  input3voltsAvg = input3voltsAvg + input3_volts # Average all 3 entries
  print("Input 3: {} ({} Bits) ({}V) ({}V)".format(timestamp, input3,input3_volts,input3voltsAvg))
  if repeat == 1:
    input3voltsAvg = input3voltsAvg / 3
    input3voltsAvg = round(input3voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 3: {} ({} Bits) ({}V) ({}V)".format(timestamp, input3,input3_volts,input3voltsAvg))
    cht = open("/home/robin/CurrentAdc3Volts", "w")
    cht.write (str(input3voltsAvg))
    cht.close()
  input4 = analogInput(4) # Reading from CH4
  input4_volts = Volts12(input4)
  input4voltsAvg = input4voltsAvg + input4_volts # Average all 3 entries
  print("Input 4: {} ({} Bits) ({}V) ({}V)".format(timestamp, input4,input4_volts,input4voltsAvg))
  if repeat == 1:
    input4voltsAvg = input4voltsAvg / 3
    input4voltsAvg = round(input4voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 4: {} ({} Bits) ({}V) ({}V)".format(timestamp, input4,input4_volts,input4voltsAvg))
    cht = open("/home/robin/CurrentAdc4Volts", "w")
    cht.write (str(input4voltsAvg))
    cht.close()
  input5 = analogInput(5) # Reading from CH5
  input5_volts = Volts12(input5)
  input5voltsAvg = input5voltsAvg + input5_volts # Average all 3 entries
  print("Input 5: {} ({} Bits) ({}V) ({}V)".format(timestamp, input5,input5_volts,input5voltsAvg))
  if repeat == 1:
    input5voltsAvg = input5voltsAvg / 3
    input5voltsAvg = round(input5voltsAvg, 2) # Round off to 2 decimal places
    print("\nInput 5: {} ({} Bits) ({}V) ({}V)".format(timestamp, input5,input5_volts,input5voltsAvg))
    cht = open("/home/robin/CurrentAdc5Volts", "w")
    cht.write (str(input5voltsAvg))
    cht.close()
  sleep(sleepTime)
  repeat = repeat - 1
