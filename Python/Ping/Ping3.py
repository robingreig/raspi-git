#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: Ping2.py
# Author: Robin Greig
# Date 2017.11.14
# Email: robin.greig@calalta.com
# Ping an ip address and return result
#-------------------------------------------------------------------

# Import modules
import subprocess
import ipaddress

# Prompt the user to input a network address
net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
    elif "Request timed out" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
    else:
        print(str(all_hosts[i]), "is Online")# Import modules
