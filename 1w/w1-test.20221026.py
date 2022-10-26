#!/usr/bin/env python

import subprocess
import re
import sys
import time
import datetime
import os
import glob
import warnings

DEBUG = 0

# Add a delay for boot
time.sleep(1)

# Continuously append data
while(True):

	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder1 = base_dir + '*64ff'
	device_folder1 = glob.glob(base_dir + '*64ff')[0]
#	device_folder1 = glob.glob(base_dir + '*284a')[0]
	device_file1 = device_folder1 + '/temperature'
	if DEBUG > 0:
		print(base_dir)
		print(device_folder1)
		print(device_folder1)
		print(device_file1)

	def read_temp_raw1():
		f = open(device_file1, 'r')
		lines1 = f.readlines()
		f.close()
		if DEBUG > 0:
			print(lines1)
		return lines1

	def read_temp1():
		lines1 = read_temp_raw1()
		lines1 = int(lines1[0])
		lines1 = lines1/1000
		if DEBUG > 0:
			print("lines1= ",lines1)
			print("lines1(int)= ",lines1)
		return lines1

	TestTemp = round(read_temp1(),1)

	if DEBUG > 0:
		print ("Test Temp (rounded): ", TestTemp)

	cht = open("/home/robin/CurrentTestTemp", "w")
	cht.write (str(TestTemp))
	cht.close()

	time.sleep(1)
	sys.exit()

