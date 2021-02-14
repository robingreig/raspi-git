#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime
from gpiozero import Button
import os

camera = PiCamera()
button = Button(23)

Debug = 0
Camera_Sleep = 2
Picture_Cycle = 5

if Debug > 0:
    camera.start_preview()

sleep(Camera_Sleep)

while True:
    try:
        button.wait_for_release()
        os.system("/home/robin/raspi-git/Python3/SMTP/Garage34Door.py")
        for i in range(10):
            now = datetime.datetime.now()
            camera.capture('/home/robin/Pictures/image,%s.jpg' % now)
        sleep(Picture_Cycle)
    except KeyboardInterrupt:
        camera.stop_preview()
        break
