#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
for i in range(5):
    camera.capture('/home/robin/Desktop/image%s.jpg' % i)
camera.stop_preview()
