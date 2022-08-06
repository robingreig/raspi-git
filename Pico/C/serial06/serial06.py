#!/usr/bin/python3
import serial
import time
import subprocess

ser = serial.Serial('/dev/serial0', 115200, timeout=1, writeTimeout=0)

while (True):
    if (ser.inWaiting() > 0):
         data_str1 = ser.read(ser.inWaiting()).decode('ascii')
         print("Data String1: ",data_str1)
         file1 = open("/home/robin/voltage", "w")
         file1.write(data_str1)
         file1.close()
    time.sleep(2)

