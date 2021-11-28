# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:48:36 2021

"""

import socket

# Create a socket connection for client
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get the server IP and port
#ip = socket.gethostname()
ip = '192.168.200.138'
port = 5490

# Try connecting to the server
soc.connect((ip,port))


# Prepare a cursor
##cursor = dbc.cursor()
# See what server sent
message = soc.recv(1024)
print(message.decode('utf-8'))

# Close the connection
soc.close()
