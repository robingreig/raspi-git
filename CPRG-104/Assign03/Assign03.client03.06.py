# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/11/30 21:33:21
Filename: Assig03.client03.06.py 

"""
import socket
import time

ClientSocket = socket.socket()
host = '127.0.0.1'
#host = '192.168.200.138'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
count = 0
while count < 51:
    clientNumber = str(6)
    ClientSocket.send(str.encode(clientNumber))
    Response = ClientSocket.recv(1024)
    responseString = Response.decode('utf-8')
    print('Server Sends: '+ Response.decode('utf-8'))
    time.sleep(1)
    count += 1

ClientSocket.close()
