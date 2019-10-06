#!/usr/bin/python3

import os
import glob
import time
import warnings
from Adafruit_IO import Client

# Run DEBUG parts of program when DEBUG > 0
DEBUG = 0

while(True):

# Should be able to enable 1 wire in raspi-config and not use
#  os.system('modprobe w1-gpio')
#  os.system('modprobe w1-therm')
 
  base_dir = '/sys/bus/w1/devices/'
#  device_folder3 = glob.glob(base_dir + '*41a4')[0]
  device_folder3 = glob.glob(base_dir + '*5e62')[0]
  device_file3 = device_folder3 + '/w1_slave'
 
  def read_temp_raw3():
      f = open(device_file3, 'r')
      lines3 = f.readlines()
      f.close()
      return lines3

  def read_temp3():
      lines3 = read_temp_raw3()
      if DEBUG > 0:
        print ("lines3 before while= ", lines3)
      while lines3[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines3 = read_temp_raw3()
      equals_pos = lines3[1].find('t=')
      if DEBUG > 0:
        print ("lines3 after while= ", lines3)
      if equals_pos != -1:
          temp_string = lines3[1][equals_pos+2:]
          if DEBUG > 0:
            print("temp_string = ", temp_string)
          temp_c3 = float(temp_string) / 1000.0
          if DEBUG > 0:
            print("temp_c3 = ", temp_c3)
          return temp_c3

  OutsideTemp = (round(read_temp3(),1))
  if DEBUG > 0:
    print ("Outside Temp sent to aio: ", OutsideTemp)

  cht = open("/home/robin/CurrentOutsideTemp", "w")
  cht.write (str(OutsideTemp))
  cht.close()
  
  aio = Client('robingreig', 'd0c57dc7661d4b2e8a1868133f9e162c')
  aio.send('outside-temp', OutsideTemp)
# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
  if DEBUG > 0:
    data = aio.receive('outside-temp')
    print('Received value: {0}'.format(data.value))

  break
