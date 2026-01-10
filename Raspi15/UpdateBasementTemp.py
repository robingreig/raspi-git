#!/usr/bin/python3

import os
import glob
import time
import warnings
from Adafruit_IO import Client
import paho.mqtt.client as mqtt #import the client1

# Run DEBUG parts of program when DEBUG > 0
DEBUG = 0

def on_message(client, userdata, message):
    if DEBUG > 0:
      print("message received " ,str(message.payload.decode("utf-8")))
    global BasementTemp
    BasementTemp = str(message.payload.decode("utf-8"))
    if DEBUG > 0:
      print ("Basement Temp sent to aio: ", BasementTemp)
      print("message topic=",message.topic)
      print("message qos=",message.qos)
      print("message retain flag=",message.retain)

while(True):

  broker_address="192.168.200.143"
  if DEBUG > 0:
    print("creating new instance")
  client = mqtt.Client("Rpi15") #create new instance
  client.on_message=on_message #attach function to callback
  if DEBUG > 0:
    print("connecting to broker")
  client.connect(broker_address) #connect to broker
  client.loop_start() #start the loop
  if DEBUG > 0:
    print("Subscribing to topic","esp8266/18/temp")
  client.subscribe("esp8266/18/temp")
#   print("Publishing message to topic","house/bulbs/bulb1")
#   client.publish("house/bulbs/bulb1","OFF")
  time.sleep(4) # wait
  client.loop_stop() #stop the loop

  if DEBUG > 0:
    print ("Basement Temp outside of function: ", BasementTemp)

  cht = open("/home/robin/CurrentBasementTemp", "w")
  cht.write (str(BasementTemp))
  cht.close()

  aio = Client('robingreig', 'd0c57dc7661d4b2e8a1868133f9e162c')
  aio.send('basement-temp', BasementTemp)
# Retrieve the most recent value from the feed 'basement-temp'
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
  if DEBUG > 0:
    data = aio.receive('basement-temp')
    print('Received value: {0}'.format(data.value))

  break
