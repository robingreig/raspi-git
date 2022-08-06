#!/usr/bin/python3
import serial
import time


serial_port = serial.Serial('/dev/serial0', 115200, timeout=1, writeTimeout=0)
# First read of A
serial_port.write('A'.encode())
dataA1 = serial_port.readline(6).decode()
#print('DataA1 = ',dataA1)
floatA1 = float(dataA1)
#print ('floatA1 = ',floatA1)
time.sleep(0.1)
# Second read of A
serial_port.write('A'.encode())
serial_port.flushInput()
dataA2 = serial_port.readline(6).decode()
#print('DataA2 = ',dataA2)
floatA2 = float(dataA2)
#print ('floatA2 = ',floatA2)
time.sleep(0.1)
# Third read of A
serial_port.write('A'.encode())
serial_port.flushInput()
dataA3 = serial_port.readline(6).decode()
#print('DataA3 = ',dataA3)
floatA3 = float(dataA3)
#print ('floatA3 = ',floatA3)
# Average the 3 reading of A1
#print ('Average = ', ((floatA1 + floatA2 + floatA3)/3))
AverageA1 = ((floatA1 + floatA2 + floatA3)/3)
#print ('AverageA1 = ', AverageA1)
AverageA1 = "{:.4f}".format(AverageA1)
print ('Average A = ', AverageA1)
time.sleep(0.1)
