#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, os

Sensor01 = 17 # Motion Sensor
Relay01 = 22 # Strobe Lights
Relay02 = 23 # Bear
Relay03 = 24 # LED lights
Relay04 = 27 # LED lights

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor01, GPIO.IN)
GPIO.setup(Relay01, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay02, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay03, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay04, GPIO.OUT, initial=GPIO.HIGH)

def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
    # Relay 1 to start strobe lights
    GPIO.output(Relay01, GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay01, GPIO.HIGH)
    time.sleep(0.5)
    # Play Audio Growl
    # Relay 2 to start bear
    GPIO.output(Relay02, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(Relay02, GPIO.HIGH)

try:
    GPIO.add_event_detect(Sensor01 , GPIO.RISING, callback=my_callback, bouncetime=5000)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print ("Finish...")
GPIO.cleanup()
