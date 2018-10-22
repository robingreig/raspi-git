#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, os

Sensor01 = 17 # Motion Sensor
Relay01 = 27 # Bear
Relay02 = 22 # Strobe Lights
Relay03 = 23 # Bear Light
Relay04 = 24 #

Count = 0
Test = 0
Debug = 1
SleepTime1 = 1.0
SleepTime2 = 10
SleepTime3 = 10 # Bear out timing shortened because of length of growls
SleepTime4 = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor01, GPIO.IN)
GPIO.setup(Relay01, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay02, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay03, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay04, GPIO.OUT, initial=GPIO.HIGH)


try:
    while True:
      if (Count == 6):
        if (Test == 0):
          GPIO.add_event_detect(Sensor01 , GPIO.RISING, bouncetime=1000)
          Test = 1
      if GPIO.event_detected(Sensor01):
        Test = 0
        Count = 0
        GPIO.output(Relay02, GPIO.HIGH)
        GPIO.output(Relay03, GPIO.LOW)
        GPIO.output(Relay01, GPIO.LOW)
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/bear2.mp3')
        if (Debug > 0):
          print('bear2 done')
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/bear2.mp3')
        if (Debug > 0):
          print('bear2 done')
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/beargrwl.mp3')
        if (Debug > 0):
          print('beargrwl done')
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/beargrowl1.mp3')
        if (Debug > 0):
          print('beargrowl1 done')
        time.sleep(SleepTime3)
        if (Debug > 0):
          print('Bear should be out fully')
        GPIO.output(Relay01, GPIO.HIGH)
        time.sleep(SleepTime1)
        if (Debug > 0):
          print('Time Up, Bear should be done growling')
        GPIO.output(Relay01, GPIO.LOW)
        time.sleep(SleepTime1)
        if (Debug > 0):
          print('Bear should be going back in')
        GPIO.output(Relay01, GPIO.HIGH)
        GPIO.output(Relay03, GPIO.HIGH)
        GPIO.remove_event_detect(Sensor01)
      else:
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/thunder.mp3')
        os.system('mpg123 /home/robin/raspi-git/Python3/Sounds/thunder2.mp3')
        GPIO.output(Relay02, GPIO.LOW)
        if (Count < 6):
          Count = Count + 1
        if (Debug > 0):
          print('Count: ',Count)
except KeyboardInterrupt:
    print('\nDebug: ',Debug)
    print('Count: ',Count)
    print ("Finish...")
GPIO.cleanup()
