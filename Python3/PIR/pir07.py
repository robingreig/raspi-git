#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, os

Sensor01 = 4 # Motion Sensor
Relay01 = 24 # Strobe Lights
Relay02 = 27 # Bear
Relay03 = 22 # LED lights
Relay04 = 23 # LED lights

Test = 0
SleepTime1 = 1.0
SleepTime2 = 0.5
Debug = 1

GPIO.setmode(GPIO.BCM)
#GPIO.setup(Sensor01, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Sensor01, GPIO.IN)
GPIO.setup(Relay01, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay02, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay03, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay04, GPIO.OUT, initial=GPIO.HIGH)

try:
  while True:
    print('Test: ',Test)
    count = 1
    if (Debug > 0):
        print('Test: ',Test)
    # Relay 1 to start strobe lights
    if (Sensor01):
      print('There was a movement!')
      GPIO.output(Relay01, GPIO.LOW)
      time.sleep(SleepTime1)
      GPIO.output(Relay01, GPIO.HIGH)
      time.sleep(SleepTime2)
      GPIO.output(Relay02, GPIO.LOW)
      time.sleep(SleepTime1)
      GPIO.output(Relay02, GPIO.HIGH)
      time.sleep(SleepTime2)
      GPIO.output(Relay03, GPIO.LOW)
      time.sleep(SleepTime1)
      GPIO.output(Relay03, GPIO.HIGH)
      time.sleep(SleepTime2)
      GPIO.output(Relay04, GPIO.LOW)
      time.sleep(SleepTime1)
      GPIO.output(Relay04, GPIO.HIGH)
      time.sleep(5)
      count = count - 1
    # Play Audio Growl
    # Relay 2 to start bear
#    GPIO.output(Relay02, GPIO.LOW)
#    time.sleep(1)
#    GPIO.output(Relay02, GPIO.HIGH)
#    os.system('mpg123 /home/robin/Desktop/beargrowl1.mp3')
except KeyboardInterrupt:
  print("Finished!")
  GPIO.cleanup()
