#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt


# Open file to read daily steps of rainfall 
# Each step = 0.245mm
file = open("/home/robin/Raincount.txt", "r")
count = file.read()
file.close()
print("Raincount = ", count)
print("count type = ",type(count))
amount = int(count) * 0.245
print("Rain amount = ",amount)

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
client = mqtt.Client("RG37") # create a new instance
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
print("Publishing message to topic, Weather/Raingauge") # Publish daily raingauge amount
client.publish("Weather/Raingauge", amount, qos=2)
time.sleep(2)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
