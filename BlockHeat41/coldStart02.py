#!/usr/bin/env python3

import time
import datetime as dt
import os

# if debug > 0 then outputs will be turned OFF
debug = 0

# outside temp stored in file by blockheat program running every 10 mins
f = open("/home/robin/outsideTemp", 'r')
lines1 = f.readlines()
f.close()
lines2 = float(lines1[0])
if debug > 0:
    print("Lines2 = ",lines2)

# Get current time
x = dt.datetime.now()
if debug > 0:
    print(x)

# Strip of everything but H & M
y = x.strftime("%H:%M")
if debug > 0:
    print(y)

# Convert to datetime format
z = dt.datetime.strptime(y,'%H:%M')
if debug > 0:
    print("z should be in datetime formatt = ",z)

# Convert back to a string
z0 = dt.datetime.strftime(z,'%H:%M')
if debug > 0:
    print("z0 should be only hours & mins = ",z0)

if '03:00'<= z0 <= '03:20':
#if '09:36' <= z0 <= '09:40':
#if '08:56' <= z0 <= '09:00' and lines2 <= -9.31:
    # if debug is OFF and temp is COLD turn on outputs
    if debug == 0 and lines2 <= -18:
        os.system("/home/robin/raspi-git/BlockHeat41/BH-right23-on-mqtt.py")
        os.system("/home/robin/raspi-git/BlockHeat41/BH-left24-on-mqtt.py")
    else: # if debug is ON or temp is not COLD enough, just print
           print("temp < -9 and debug > 0")
    cht = open("/home/robin/outsideTempLast", "w")
    cht.write (str(lines2))
    cht.close()
