#!/usr/bin/python3
import serial
import time


serial_port = serial.Serial('/dev/serial0', 115200, timeout=1, writeTimeout=0)
print("Data from input A: ")
serial_port.write('A'.encode())
dataA = serial_port.readline(6).decode()
print (dataA)
print("Data from input B: ")
serial_port.write('B'.encode())
dataB = serial_port.readline(6).decode()
print (dataB)
print("Data from input C: ")
serial_port.write('C'.encode())
dataC = serial_port.readline(6).decode()
print (dataC)

