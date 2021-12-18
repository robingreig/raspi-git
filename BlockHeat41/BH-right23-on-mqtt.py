#!/usr/bin/env python3

import time
import os
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


pinNum = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output

GPIO.output(pinNum,GPIO.LOW) # turn GPIO 23 off
#GPIO.cleanup()

import datetime
import os
import glob
import logging

# Add a delay for boot
time.sleep(1)
DEBUG = 1

#### upload status to mqtt broker

#broker_address = "mqtt21.local"
broker_address = "192.168.200.21"
print("Creating new instance & starting logging")
logging.basicConfig(level=logging.INFO) # use DEBUG, INFO, WARNING

def on_log(client, userdata, level, buf):
  logging.info(buf)

def on_connect(client, userdata, flags, rc):
  if rc==0:
    client.connected_flag=True # set flag
    logging.info("connected OK")
  else:
    logging.info("Bad Connection Returned Code = "+str(rc))
    client.loop_stop()

def on_disconnect(client, userdata, rc):
  logging.info("client disconnected OK")

def on_publish(client, userdata, mid):
  logging.info("In on_pub callback mid = " +str(mid))

mqtt.Client.connected_flag=False # create flag in class

client = mqtt.Client("BH1") # create a new instance for first topic
client.on_log = on_log # display log entries
client.on_connect = on_connect # bind callback function
client.on_disconnect = on_disconnect # bind callback function
client.on_publish = on_publish # bind callback function

logging.info("Connecting to broker: "+str(broker_address))
client.connect(broker_address) # connect to broker

client.loop_start() # start the loop

while not client.connected_flag:
  logging.info("In Wait Loop")
  time.sleep(1)

logging.info("In Main Loop")
logging.info("Publishing message to topic, BlockHeat/right23")
ret=client.publish("BlockHeat/right23", False, qos=2)
logging.info("Published return: "+str(ret))
time.sleep(2)
logging.info("Stopping the loop")
client.loop_stop() # stop the loop
client.disconnect() # disconnect
