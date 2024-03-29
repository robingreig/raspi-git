#!/usr/bin/python3

import os
import glob
import time
import warnings
from Adafruit_IO import Client

DEBUG = 0

while(True):

# Should be able to enable 1 wire from raspi-config
#  os.system('modprobe w1-gpio')
#  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
  device_folder2 = glob.glob(base_dir + '*533e')[0]
  device_file2 = device_folder2 + '/w1_slave'

  def read_temp_raw2():
      f = open(device_file2, 'r')
      lines2 = f.readlines()
      f.close()
      return lines2

  def read_temp2():
      lines2 = read_temp_raw2()
      if DEBUG > 0:
        print("lines2 before while = ", lines2)
      while lines2[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines2 = read_temp_raw2()
      if DEBUG > 0:
        print("lines2 after while = ", lines2)
      equals_pos = lines2[1].find('t=')
      if equals_pos != -1:
          temp_string = lines2[1][equals_pos+2:]
          if DEBUG > 0:
            print("temp_string = ", temp_string)
          temp_c2 = float(temp_string) / 1000.0
          if DEBUG > 0:
            print("temp_c2 = ", temp_c2)
          return temp_c2

  CeilingTemp = (round(read_temp2(),1))
  if DEBUG > 0:
    print ("Garage Ceiling Temp sent to aio: ", CeilingTemp)

  cht = open("/home/robin/CurrentCeilingTemp", "w")
  cht.write (str(CeilingTemp))
  cht.close()

  aio = Client('robingreig', 'd0c57dc7661d4b2e8a1868133f9e162c')
  aio.send('ceiling-temp', CeilingTemp)
# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
  if DEBUG > 0:
    data = aio.receive('ceiling-temp')
    print('Received value from aio: {0}'.format(data.value))
  break
