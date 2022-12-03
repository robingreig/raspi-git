#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23, 24, 25]

# Declare as named instance of class
mymotortest = RpiMotorLib.BYJMotor("myMotorOne", "28BYJ")
i = 100
# call the function
while i > 0:
    print('i = ',i)
#    print('GpioPins, .01, 512, False, False, "half", 0.05')
#    mymotortest.motor_run(GpioPins, .01, 512, False, False, "half", 0.05)
#    print('GpioPins, .005, 256, False, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .005, 256, False, False, "half", 0.01)
#    print('GpioPins, .005, 256, True, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .005, 256, True, False, "half", 0.01)
#    print('GpioPins, .004, 256, False, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .004, 256, False, False, "half", 0.01)
#    print('GpioPins, .004, 256, True, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .004, 256, True, False, "half", 0.01)
#    print('GpioPins, .003, 256, False, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .003, 256, False, False, "half", 0.01)
#    print('GpioPins, .003, 256, True, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .003, 256, True, False, "half", 0.01)
#    print('GpioPins, .002, 256, False, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .002, 256, False, False, "half", 0.01)
#    print('GpioPins, .002, 256, True, False, "half", 0.01')
#    mymotortest.motor_run(GpioPins, .002, 256, True, False, "half", 0.01)
    print('GpioPins, .001, 256, False, False, "half", 0.01')
    mymotortest.motor_run(GpioPins, .001, 256, False, False, "half", 0.01)
    time.sleep(0.5)
    print('GpioPins, .001, 256, True, False, "half", 0.01')
    mymotortest.motor_run(GpioPins, .001, 256, True, False, "half", 0.01)
    time.sleep(0.5)
    i -= 1
