
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
    #connection.send(str.encode('Welcome to the Server'))
#    while True:
    #data = connection.recv(2048)
    #if not data:
    #    return
    x = 5
    while x > 0 and x < 6:
        connection.send(str.encode('Welcome to the Server'))
        data = connection.recv(2048)
        if not data:
            break
        #for x in range(50):
        xStr = str(x)
            #reply = 'Server Says: ' + data.decode('utf-8')
        reply = '\nServer Says: ' + xStr
            #connection.sendall(str.encode(reply))
        connection.send(str.encode(reply))
        x -= 1
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Client: ',Client)
    print('Client Address: ',address)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
