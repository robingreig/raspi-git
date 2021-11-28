# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:42:39 2021

"""

import socket

# Create a socket object
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get the IP and port
#ip = socket.gethostname()
ip = '192.168.200.138'
port = 5490
# Bind the socket to the ip and port
soc.bind((ip,port))
# Make the server listen for incoming connections
soc.listen()

# Wait until client connects and 
# accept the connection when client tries to connect.
client, client_addr  = soc.accept()

print ('Got connection from', client_addr )
 
# send a thank you message to the client.
client.send('Thank you for connecting'.encode('utf-8'))

# Close the connection with the client
client.close()
soc.close()
