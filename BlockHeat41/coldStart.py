#!/usr/bin/env python3

import time
import datetime
import os

# Add a delay for boot
time.sleep(1)
DEBUG = 1

f = open("/home/robin/outsideTemp", 'r')
lines1 = f.readlines()
f.close()
lines2 = float(lines1[0])
print("Lines2 = ",lines2)


if  DEBUG > 0:
    if lines2 < -18:
        print("temp < -18 and turning on Block Heaters")
        os.system("/home/robin/raspi-git/BlockHeat41/BH-right23-on-mqtt.py")
        os.system("/home/robin/raspi-git/BlockHeat41/BH-left24-on-mqtt.py")
        cht = open("/home/robin/outsideTempLast", "w")
        cht.write (str(lines2))
        cht.close()
    else:
        print("temp > -18")
