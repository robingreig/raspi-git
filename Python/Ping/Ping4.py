#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: Ping4.py
# Author: Robin Greig
# Date 2018.04.29
# Email: robin.greig@calalta.com
# Ping an ip address and return result
#-------------------------------------------------------------------

import subprocess
import ipaddress
import time

out_file = open("alive.txt", "w")

TimeStart = time.time()
print(time.asctime(time.localtime(time.time())))

alive = []
subnet = ipaddress.ip_network('192.168.200.0/24', strict=False)
for i in subnet.hosts():
    i = str(i)
    retval = subprocess.call(["ping", "-c1", "-n", "-i0.2", "-W1", i])
#    retval = subprocess.call(["ping", "-c1", "-n", "-i0.2", "-W1", i, " > /dev/null 2>&1"])
    if retval == 0:
        alive.append(i)

for ip in alive:
    print(ip + " is alive")
    out_file.write(ip + "\n")
    length = len(alive)
    print(length)

TimeFinish = time.time()
print(time.asctime(time.localtime(time.time())))
print(TimeFinish - TimeStart)
TotalTime = round(TimeFinish - TimeStart,2)
print ("TotalTime: " + str(TotalTime))
out_file.write("Total time: " + str(TotalTime) + "\n")
out_file.write("List length: " + str(length) + "\n")
