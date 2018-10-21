#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 17
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print ("Finish...")
GPIO.cleanup()
