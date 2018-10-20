#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, os

Sensor01 = 17 # Motion Sensor
Relay01 = 24 # Strobe Lights
Relay02 = 27 # Bear
Relay03 = 22 # LED lights
Relay04 = 23 # LED lights

Test = 0

Debug = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor01, GPIO.IN)
GPIO.setup(Relay01, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay02, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay03, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay04, GPIO.OUT, initial=GPIO.HIGH)

#def my_callback(channel):
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    global Test
    Test = 1
    print('Test: ',Test)
    global count
    count = 3
    if (Debug > 0):
        print('There was a movement!')
        print('Test: ',Test)
    # Relay 1 to start strobe lights
    while (count > 0):
      GPIO.output(Relay01, GPIO.LOW)
      time.sleep(0.5)
      GPIO.output(Relay01, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(Relay02, GPIO.LOW)
      time.sleep(0.5)
      GPIO.output(Relay02, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(Relay03, GPIO.LOW)
      time.sleep(0.5)
      GPIO.output(Relay03, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(Relay04, GPIO.LOW)
      time.sleep(0.5)
      GPIO.output(Relay04, GPIO.HIGH)
      time.sleep(0.5)
      count = count - 1
    # Play Audio Growl
    # Relay 2 to start bear
#    GPIO.output(Relay02, GPIO.LOW)
#    time.sleep(1)
#    GPIO.output(Relay02, GPIO.HIGH)
#    os.system('mpg123 /home/robin/Desktop/beargrowl1.mp3')

try:
    GPIO.add_event_detect(Sensor01 , GPIO.RISING, callback=my_callback, bouncetime=5000)
    while True:
        if (Test < 1):
#            os.system('mpg123 /home/robin/Desktop/Thunder01.mp3')
            if (Debug > 0):
              print('Test: ',Test)
except KeyboardInterrupt:
    print('\nDebug: ',Debug)
    print('Test: ',Test)
    print('Count: ',count)
    print ("Finish...")
GPIO.cleanup()
