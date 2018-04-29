#!/usr/bin/env python3

###############################
# RelaysCycle.py
# Robin Greig
# 28 April 2018
# Test program to cycle all 8 relays on board
###############################

# Import modules
import time
import os
import RPi.GPIO as GPIO

# Setup variables
relay1 = 11
relay2 = 12
relay3 = 13
relay4 = 14
relay5 = 15
relay6 = 16
relay7 = 17
relay8 = 18
timeDelay = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(relay1,GPIO.OUT) #Setup relay1 as an output
GPIO.setup(relay2,GPIO.OUT) #Setup relay2 as an output
GPIO.setup(relay3,GPIO.OUT) #Setup relay3 as an output
GPIO.setup(relay4,GPIO.OUT) #Setup relay4 as an output
GPIO.setup(relay5,GPIO.OUT) #Setup relay5 as an output
GPIO.setup(relay6,GPIO.OUT) #Setup relay6 as an output
GPIO.setup(relay7,GPIO.OUT) #Setup relay7 as an output
GPIO.setup(relay8,GPIO.OUT) #Setup relay8 as an output
print("GPIO Pin 11 is Low, Relay 1 is on")
GPIO.output(relay1,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 11 is High, Relay 1 is off")
GPIO.output(relay1,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 12 is Low, Relay 2 is on")
GPIO.output(relay2,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 12 is High, Relay 2 is off")
GPIO.output(relay2,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 13 is Low, Relay 3 is on")
GPIO.output(relay3,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 13 is High, Relay 3 is off")
GPIO.output(relay3,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 14 is Low, Relay 4 is on")
GPIO.output(relay4,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 14 is High, Relay 4 is off")
GPIO.output(relay4,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 15 is Low, Relay 5 is on")
GPIO.output(relay5,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 15 is High, Relay 5 is off")
GPIO.output(relay5,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 16 is Low, Relay 6 is on")
GPIO.output(relay6,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 16 is High, Relay 6 is off")
GPIO.output(relay6,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 17 is Low, Relay 7 is on")
GPIO.output(relay7,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 17 is High, Relay 7 is off")
GPIO.output(relay7,GPIO.HIGH)
time.sleep(timeDelay)
print("GPIO Pin 18 is Low, Relay 8 is on")
GPIO.output(relay8,GPIO.LOW)
time.sleep(timeDelay)
print("GPIO Pin 18 is High, Relay 8 is off")
GPIO.output(relay8,GPIO.HIGH)
time.sleep(timeDelay)
GPIO.cleanup
