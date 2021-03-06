#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime
from gpiozero import Button

camera = PiCamera()
button = Button(23)

camera.start_preview()
sleep(2)

while True:
    try:
        button.wait_for_release()
        for i in range(5):
            now = datetime.datetime.now()
            camera.capture('/home/robin/Desktop/image,%s.jpg' % now)
        sleep(5)
    except KeyboardInterrupt:
        camera.stop_preview()
        break
