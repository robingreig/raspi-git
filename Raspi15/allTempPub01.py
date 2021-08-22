#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt

ch0 = open("/home/robin/CurrentAtticTemp", "r")
Attic = ch0.read()
ch0.close()
ch1 = open("/home/robin/CurrentCeilingTemp", "r")
Ceiling = ch1.read()
ch1.close()
ch2 = open("/home/robin/CurrentGarageTemp", "r")
Desk = ch2.read()
ch2.close()
ch3 = open("/home/robin/CurrentOutsideTemp", "r")
Outside = ch3.read()
ch3.close()

#### upload voltages to mqtt broker

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False # create flag in class

broker_address = "192.168.200.21"
#broker_address = "mqtt21.local"
print("Creating new instance")
client = mqtt.Client("RP15") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_connect=on_connect # bind callback function

print("Connecting to broker ",broker_address)
client.connect(broker_address) # connect to broker

client.loop_start() # start the loop

while not client.connected_flag:
  print("In Wait Loop")
  time.sleep(1)

print("In Main Loop")
print("Publishing message to topic, AtticTemp") # Garage Attic Temp
client.publish("Garage/AtticTemp", Attic, qos=2)
time.sleep(2)
print("Publishing message to topic, CeilingTemp") # Garage Ceiling Temp
client.publish("Garage/CeilingTemp", Ceiling, qos=2)
time.sleep(2)
print("Publishing message to topic, DeskTemp") # Garage Desk Temp
client.publish("Garage/DeskTemp", Desk, qos=2)
time.sleep(2)
print("Publishing message to topic, OutsideTemp") # Outside Temp
client.publish("Garage/OutsideTemp", Outside, qos=2)
time.sleep(2)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
