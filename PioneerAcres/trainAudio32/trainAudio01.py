#!/usr/bin/env python3

import time
import datetime as dt
import os

# if debug > 0 then outputs will be turned OFF
debug = 1

# if debug is OFF and temp is COLD turn on outputs
if debug > 0:
#    os.system("/home/robin/raspi-git/trainAudio32/loadAsoundrc.sh")
    os.system("aplay /home/robin/raspi-git/trainAudio32/TrainHorn01.wav")
else: # if debug is ON just print
       print("debug == 0")

