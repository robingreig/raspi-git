#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime
from gpiozero import Button
import os

camera = PiCamera()
button = Button(23)

# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1
Num_Pics = 10
Camera_Sleep = 1
Picture_Cycle = 5

sleep(Camera_Sleep)

while True:
    try:
        button.wait_for_release()
        if Debug > 0:
            print("Door Opened!")
        os.system("/home/robin/raspi-git/Python3/SMTP/Garage34Door.py")
        for i in range(Num_Pics):
            now = datetime.datetime.now()
            camera.capture('/home/robin/Pictures/image,%s.jpg' % now)
        for j in range(60):
            if button.is_pressed:
                if Debug > 0:
                    print("Door is closed")
                break
            if Debug > 0:
                print("Waiting for door to close: %s" %j)
            sleep(Picture_Cycle)
    except KeyboardInterrupt:
        break
