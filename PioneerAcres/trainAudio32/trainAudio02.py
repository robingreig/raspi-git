#!/usr/bin/env python3

import time
import os
from gpiozero import Button

button = Button(2) # set GPIO2 as input trigger for audio

# if debug > 0 then outputs will be turned OFF
debug = 0

while True:
    try:
        # button.when_released  = os.system('aplay /home/robin/raspi-git/trainAudio32/TrainHorn01.wav')
        button.wait_for_release()
        os.system('aplay /home/robin/raspi-git/trainAudio32/TrainHorn01.wav')
        if debug > 0:
            print('Train Detected')
    except KeyboardInterrupt:
        break
