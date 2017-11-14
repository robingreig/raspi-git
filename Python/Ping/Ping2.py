#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: Ping2.py
# Author: Robin Greig
# Date 2017.11.14
# Email: robin.greig@calalta.com
# Ping an ip address and return result
#-------------------------------------------------------------------

import subprocess
import ipaddress

alive = []
subnet = ipaddress.ip_network('192.168.200.0/27', strict=False)
for i in subnet.hosts():
    i = str(i)
    retval = subprocess.call(["ping", "-c1", "-n", "-i0.2", "-W1", i])
    if retval == 0:
        alive.append(i)
for ip in alive:
    print(ip + " is alive") 
