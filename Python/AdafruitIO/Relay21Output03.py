#!/usr/bin/python

# Import Library & create instance of REST client
from Adafruit_IO import Client

import time
import os
import RPi.GPIO as GPIO

aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

last = 0
inputNum = 20
outputNum = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(outputNum,GPIO.OUT)
GPIO.setup(inputNum,GPIO.IN)


while True:
  if (time.time() - last) >= 7:
    # Retrieve the most recent value from BlockHeat01
    data = aio.receive('blockheat01')
    print('Received Value: {0}'.format(data.value))
    if data.value == "1":
      print('data = 1')
      GPIO.output(outputNum,GPIO.HIGH)
    else:
      print('data = 0')
      GPIO.output(outputNum,GPIO.LOW)
    state = GPIO.input(inputNum)
    if (state):
      print('Doorstate = 1')
      aio.send('doorstate',1)
    else:
      print('Doorstate = 0')
      aio.send('doorstate',0)
    last = time.time()
