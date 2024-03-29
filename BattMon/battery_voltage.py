#!/usr/bin/env python

import serial
import time
import os

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=5)


DEBUG = 0
count = 0
Voltage = 0

while (count < 10):
  ser.flushInput() # flush the serial input on raspi
  ser.write("~") # tell gertduino to send Sensor Value
  print ser.readline()
  ser.write("+") # tell gertduino to send Output Value
  print ser.readline()
  ser.flushInput()
  ser.write("^") # tell gertduino to send battery voltage
  battVolt = ser.readline()
  if DEBUG != 0:
    print "\nSerial Line: ", (battVolt)

  cht = open("/home/robin/ArduinoSerialString", "w")
  cht.write(str(battVolt))
  if DEBUG != 0:
    print "\nSerial Line after file write: ", (battVolt)
  cht.close()

  device_file1 = '/home/robin/ArduinoSerialString'
  if DEBUG != 0:
    print"\ndevice_file1: ", (device_file1)

  def read_batt_volt_file():
      f = open(device_file1, 'r')
      lines1 = f.readlines()
      if DEBUG != 0:
	print "\nlines1: ", (lines1)
      f.close()
      return lines1

  def save_batt_volt():
    lines1 = read_batt_volt_file()
    equals_pos = lines1[0].find('\r')
    if equals_pos != -1:
            batt_volt_str = lines1[0][equals_pos-5:]
	    if DEBUG != 0:
		print "\nequals_pos: ", (equals_pos)
		print "\nBattery Voltage: ", (batt_volt_str)
	    return batt_volt_str

  cht = open("/home/robin/CurrentBatteryVoltage", "w")
  cht.write(str(save_batt_volt()))
  cht.close()

  print "Count is: ",(count)

  Voltage = (float(save_batt_volt()))

  print "Battery Voltage is: ", (Voltage)

  if Voltage < 12.00:
    print "Battery LOW!!!!!"
#    os.system('sudo reboot')
  count = count + 1
  time.sleep(1)
