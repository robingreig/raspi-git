#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

# import the library
from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23, 24, 25]

# Declare as named instance of class
mymotortest = RpiMotorLib.BYJMotor("myMotorOne", "28BYJ")
i = 20

# call the function
try:
    while True:
        current_state = GPIO.input(13)
        print('GpioPins, .001, 1, False, False, "half", 0.01')
        mymotortest.motor_run(GpioPins, .001, 1, False, False, "half", 0.01)
        time.sleep(0.01)
        if current_state == 1:
            print('Button not pressed')
        else:
            break
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
