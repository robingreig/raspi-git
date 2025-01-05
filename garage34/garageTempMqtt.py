#!/usr/bin/env python3

##########
# Author: Robin Greig
# Date: 2021.12.28
# Filenae: /raspi-git/garage34/garageTempMqtt.py
# 1) Check temp stored in mqtt 'Garage/FurnaceHeat'
# 2) GPIO24 connected to relay so when output is high, relay is off
# 3) If FurnaceHeat > GarageTemp then GPIO24 goes low and turns relay on
# 4) And GarageTemp is sent back to mqtt to display
# 5) Need to increase turn off +0.5 degrees and turn on 0.2 degrees to
# minimize cycle time of furnace
##########

import paho.mqtt.client as mqtt
import time
import datetime
import os
import glob
import logging
import RPi.GPIO as GPIO
import warnings

# Add a delay for boot
time.sleep(1)
DEBUG = 0
tempUpRange = 2.0 # how much above & below the set temp to minimize furnace cycling
tempLowRange = 1.0 # how much above & below the set temp to minimize furnace cycling

# Setup GPIO24 as relay output
relay = 24
GPIO.setwarnings(False) # Don't display the warnings
GPIO.setmode(GPIO.BCM) # Numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(relay,GPIO.OUT) # Sets up variable relay as an output
#GPIO.output(relay,GPIO.HIGH) # Turn the relay off so furnace stars OFF
##### Leave GPIO alone in case furnace is running and program runs again

# Assign one wire devices
base_dir = '/sys/bus/w1/devices/'
# Garage Sensor *27c2
device_folder1 = glob.glob(base_dir + '*27c2')[0]
device_file1 = device_folder1 + '/w1_slave'

def read_temp_raw1():
    f = open(device_file1, 'r')
    lines1 = f.readlines()
    f.close()
    return lines1

def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines1 = read_temp_raw1()
    equals_pos = lines1[1].find('t=')
    if equals_pos != -1:
        temp_string = lines1[1][equals_pos+2:]
        temp_c1 = round((float(temp_string) / 1000.0),1)
        return temp_c1

temp1 = read_temp1()

if DEBUG > 0:
  print ("Inside Temp: ", (read_temp1()))
  print ("Inside Temp: ", temp1)
  time.sleep(1)

#### upload temps and check thermostat setting on mqtt broker

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

def on_message(client, userdata, message):
    print("\nmessage received:",str(message.payload.decode("utf-8")),\
          "topic:",message.topic,"qos:", message.qos, "retained:",message.retain)
    if message.retain==1:
        print("This is a retained message")
    global thermostat
    thermostat = str(message.payload.decode("utf-8"))
    print("Garage Thermostat setting is: ",thermostat)

mqtt.Client.connected_flag=False # create flag in class

client = mqtt.Client("G34") # create a new instance for first topic
client.on_log = on_log # display log entries
client.on_connect = on_connect # bind callback function
client.on_disconnect = on_disconnect # bind callback function
client.on_publish = on_publish # bind callback function
client.on_message=on_message # attach function to callback

logging.info("Connecting to broker: "+str(broker_address))
client.connect(broker_address) # connect to broker

client.loop_start() # start the loop

while not client.connected_flag:
  logging.info("In Wait Loop")
  time.sleep(1)

logging.info("In Main Loop\n")
# Publish the Garage Temperature
logging.info("Publishing message to topic, Garage/FurnaceTemp")
ret=client.publish("Garage/FurnaceTemp", temp1, qos=2, retain=True)
logging.info("Published return for Garage/FurnaceTemp:\n "+str(ret))
time.sleep(2)
## Check the thermostat setting
#logging.info("Reading message from topic, Garage/FurnaceTemp")
#client.subscribe("Garage/FurnaceTemp")
#time.sleep(2)
# Check the Garage Temperature was published
logging.info("Reading message from topic, Garage/FurnaceHeat")
client.subscribe("Garage/FurnaceHeat")
time.sleep(2)
# Stopping the Loop
logging.info("Stopping the loop")
client.loop_stop() # stop the loop
client.disconnect() # disconnect
print("*******")
print("Garage Thermostat setting is: ",thermostat)
print("Garage Temperature is: ", temp1)
thermostatFloat = float(thermostat)
print("thermostatFloat: ", thermostatFloat)
thermostatUpper = thermostatFloat + tempUpRange
print("Garage Thermostat upper limit = ",thermostatUpper)
thermostatLower = thermostatFloat - tempLowRange
print("Garage Thermostat lower limit = ",thermostatLower)
if thermostatLower > temp1: # If garage temp < garage thermostat
  GPIO.output(relay,GPIO.LOW) # Output LOW = Furnace On
  print("Turning Furnace on")
elif thermostatUpper < temp1: # if garage temp > garage thermostat
  GPIO.output(relay,GPIO.HIGH) # Output HIGH = Furnace Off
  print("Turning Furnace off")
