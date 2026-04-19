#!/usr/bin/env python3

# trainAudio02.py
# Robin Greig for Pioneer Acres
# 2026.04.19
# Hall Effect device will trigger the audio track when the train engine
# passes over top near the car crossing 

import time
import os
from gpiozero import Button

# set GPIO 02 as input trigger for hall effect device
button = Button(2)

# if debug > 0 then printed outputs will be turned OFF
debug = 0

while True:
    try:
        # button.when_released()
        # button.wait_for_release()
        button.wait_for_press()
        os.system('aplay /home/robin/raspi-git/trainAudio32/TrainHorn01.wav')
        if debug > 0:
            print('Train Detected')
    except KeyboardInterrupt:
        break
