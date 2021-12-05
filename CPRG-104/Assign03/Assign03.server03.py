# -*- coding: utf-8 -*-
"""

Class: CPRG-104
Instructor: Hamdy Ibrahim
Student: Robin Greig
Created on 2021/11/30 21:33:21
Filename: Assig03.server03.py 

"""
import socket
import os
from _thread import *
import time

ServerSocket = socket.socket()
host = '127.0.0.1'
#host = '192.168.200.138'
port = 1233
ThreadCount = 0
try:
	ServerSocket.bind((host, port))
except socket.error as problem:
	print(str(problem))

print('Waitiing for a Connection..')
ServerSocket.listen(10)


def threaded_client(connection):
	connection.send(str.encode('ping'))
	while True:
		data = connection.recv(2048)
		if not data:
			return
		threadNumber = 'Client Thread Number: ' + data.decode('utf-8') + ('\n')
		connection.send(str.encode(threadNumber))
		x = range(1,51)
		for count in x:
			print(count)
			newCount = str(count)
			connection.send(str.encode(newCount))
			time.sleep(2)
		return
	connection.close()

while True:
	Client, address = ServerSocket.accept()
	print('Connected to: ' + address[0] + ':' + str(address[1]))
	start_new_thread(threaded_client, (Client, ))
	ThreadCount += 1
	print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
