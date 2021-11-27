import socket

# Create a socket object
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get the IP and port
ip = socket.gethostname()
port = 5490
# Bind the socket to the ip and port
soc.bind((ip,port))

soc.listen()

client, client_addr  = soc.accept()

print ('Got connection from', client_addr )
 
message = client.recv(1024)
print(message.decode('utf-8'))

client.send('Hello I am server'.encode('utf-8'))

client.close()
soc.close()