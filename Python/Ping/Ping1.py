#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: Ping1.py
# Author: Robin Greig
# Date 2017.11.14
# Email: robin.greig@calalta.com
# Ping an ip address and return result
#-------------------------------------------------------------------
import subprocess

for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print ("No response from", address)
    else:
        print ("ping to", address, "failed!")
