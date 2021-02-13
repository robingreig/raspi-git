#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

camera.start_preview()
sleep(2)
frame = 1

for i in range(5):
    now = datetime.datetime.now()
    camera.capture('/home/robin/Desktop/image,%s.jpg' % now)
camera.stop_preview()
