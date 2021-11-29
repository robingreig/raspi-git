import socket

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
while True:
    print('Made it to the while True loop')
    #Input = input('Say Something: ')
    Input = ("Hello")
    #ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
