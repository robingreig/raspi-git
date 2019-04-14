#!/usr/bin/env python3

"""
'digital_out.py'
===================================
Example of turning on and off a LED
from the Adafruit IO Python Client

Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time
import time
import os
import RPi.GPIO as GPIO

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'e69155097ffa4624ae09d57213e200ed'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 've6rbn'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('masterbath')
except RequestError: # create a digital feed
    feed = Feed(name="masterbath")
    digital = aio.create_feed(feed)

count = 0
pinNum = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as$
GPIO.output(pinNum,GPIO.LOW) #set GPIO Low for default

while count < 5:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
        GPIO.output(pinNum,GPIO.HIGH) #set GPIO High
    elif int(data.value) == 0:
        print('received <- OFF\n')
        GPIO.output(pinNum,GPIO.LOW) #set GPIO Low

    time.sleep(1)
    count = count +1

GPIO.cleanup()
