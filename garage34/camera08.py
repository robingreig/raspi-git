#!/usr/bin/env python3

##########
# Author: Robin Greig
# Filename: garageCamera.py
# 2021.12.28
# 1) If the garage mandoor is opened
# 2) Turn on the LED light
# 3) Take 10 pics (Num_Pics)
##########

from picamera import PiCamera
from time import sleep
import datetime
from gpiozero import Button, LED
import os

# Assign variable 'camera' to the Pi Camera
camera = PiCamera()
# Assign variable 'door' as an input (Button) on GPIO23
door = Button(23)
# Assign variable 'light' as an output (LED) on GPIO25
light = LED(25)
# Relay for light is off when output is High (on)
light.on()
# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1
# Number of pics to be taken each time door is opened
Num_Pics = 20
# Delay between pics taken
Camera_Sleep = 0.5
# Delay x 60 before additional sets of pics taken if door isn't closed
Picture_Cycle = 5

sleep(Camera_Sleep)

while True:
    try:
        door.wait_for_release() # Door opened
        if Debug > 0:
            print("Door Opened!")
            light.off() # output low = Light ON
# Send email that door is opened
        os.system("/home/robin/raspi-git/Python3/SMTP/Garage34Door.py")
        for i in range(Num_Pics):
            now = datetime.datetime.now()
            camera.capture('/home/robin/PicsTemp/%s.jpg' % now)
# Send a copy of the pics to battmon24
        os.system("/home/robin/raspi-git/garage34/movePics.sh")
        for j in range(60):
            if door.is_pressed:
                light.on() # output high = Light OFF
                if Debug > 0:
                    print("Door is closed")
                break
            if Debug > 0:
                print("Waiting for door to close: %s" %j)
            sleep(Picture_Cycle)
    except KeyboardInterrupt:
        break
