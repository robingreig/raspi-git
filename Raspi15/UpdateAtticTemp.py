#!/usr/bin/python3

import os
import glob
import time
import warnings
from Adafruit_IO import Client

# Run DEBUG portions of program if > 0
DEBUG = 0

while(True):

# Should be able to enable 1 wire from raspi-config
#  os.system('modprobe w1-gpio')
#  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder = glob.glob(base_dir + '*539e')[0]
  device_file = device_folder + '/w1_slave'

  def read_temp_raw():
      f = open(device_file, 'r')
      lines = f.readlines()
      f.close()
      return lines

  def read_temp():
      lines = read_temp_raw()
      if DEBUG > 0:
        print("lines before while = ", lines)
      while lines[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines = read_temp_raw()
      if DEBUG > 0:
        print("lines after while = ", lines)
      equals_pos = lines[1].find('t=')
      if equals_pos != -1:
          temp_string = lines[1][equals_pos+2:]
          if DEBUG > 0:
            print("temp_string = ", temp_string)
          temp_c = float(temp_string) / 1000.0
          if DEBUG > 0:
            print("temp_c = ", temp_c)
          return temp_c

  AtticTemp = (round(read_temp(),1))
  if DEBUG > 0:
    print ("Garage Attic Temp sent to aio: ", AtticTemp)

  cht = open("/home/robin/CurrentAtticTemp", "w")
  cht.write (str(AtticTemp))
  cht.close()

  aio = Client('robingreig', 'd0c57dc7661d4b2e8a1868133f9e162c')
  aio.send('attic-temp', AtticTemp)
# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
  if DEBUG > 0:
    data = aio.receive('attic-temp')
    print('Received value from aio: {0}'.format(data.value))

  break
