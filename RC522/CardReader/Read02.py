#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

GPIO.setmode(GPIO.BCM)
LED = 18
GPIO.setup(LED,GPIO.OUT)
DEBUG = 0
if DEBUG > 0:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED, GPIO.LOW)

reader = SimpleMFRC522.SimpleMFRC522()

try:
	id, text = reader.read()
	print (id)
	print (text)
	print ('LED off')
#No	if (text)=='Robin':
#No	name = str(text)
#No	if name.lower in ['Robin', 'robin']:
#Works	if int(id) == 263390081689:
#No	if (id) in ['263390081689', '552599753657']:
	if text[0:5] == 'Robin':
	    print ('Welcome Robin!')
	    print ('LED ON')
	    GPIO.output(LED, GPIO.HIGH)
            time.sleep(5)
	    GPIO.output(LED, GPIO.LOW)
finally:
	GPIO.cleanup()

