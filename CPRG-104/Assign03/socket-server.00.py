
import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
#host = '192.168.200.138'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('ping'))
    while True:
        data = connection.recv(2048)
        if not data:
            return
        connection.send(str.encode('Welcome to the Server from: ',str(ThreadCount),'\n'))
        reply = 'Server replies: ' + data.decode('utf-8')
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
