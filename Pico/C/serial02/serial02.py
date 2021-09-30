#!/usr/bin/python3
import serial
import time


serial_port = serial.Serial('/dev/serial0', 115200, timeout=1, writeTimeout=0)
#serial_port.write('robin\n'.encode())
serial_port.write('C'.encode())
#data = serial_port.readline(7).decode()
data = serial_port.readline(6).decode()
print (data)
