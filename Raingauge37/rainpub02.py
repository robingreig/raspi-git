#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt


# Open file to read daily steps of rainfall 
# Each step = 0.245mm
# Each step = 0.375mm (8 steps / 2.8mm 20240518)
##### Total Rainfall for previous day
file = open("/home/robin/Raincount.txt", "r")
count = file.read()
file.close()
print("Raincount = ", count)
print("count type = ",type(count))
#amount = round((int(count) * 0.245),2)
amount = round((int(count) * 0.35),2)
print("Rain amount = ",amount)

##### Total rainfall for first quad today (midnight > 6am)
file = open("/home/robin/quad1.txt", "r")
count = file.read()
file.close()
print("Raincount quad1 = ", count)
print("count type = ",type(count))
#quad1amount = round((int(count) * 0.245),2)
quad1amount = round((int(count) * 0.35),2)
print("Rain amount quad 1 = ",quad1amount)

file = open("/home/robin/quad2.txt", "r")
count = file.read()
file.close()
print("Raincount quad2 = ", count)
print("count type = ",type(count))
#quad2amount = round((int(count) * 0.245),2)
quad2amount = round((int(count) * 0.35),2)
print("Rain amount quad2 = ",quad2amount)

file = open("/home/robin/quad3.txt", "r")
count = file.read()
file.close()
print("Raincount quad3 = ", count)
print("count type = ",type(count))
#quad3amount = round((int(count) * 0.245),2)
quad3amount = round((int(count) * 0.35),2)
print("Rain amount quad3 = ",quad3amount)

file = open("/home/robin/quad4.txt", "r")
count = file.read()
file.close()
print("Raincount quad4 = ", count)
print("count type = ",type(count))
#quad4amount = round((int(count) * 0.245),2)
quad4amount = round((int(count) * 0.35),2)
print("Rain amount quad4 = ",quad4amount)

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
print("Publishing message to topic, Weather/Quad1") # Publish 12am > 6am raingauge amount
client.publish("Weather/Quad1", quad1amount, qos=2)
time.sleep(2)
print("Publishing message to topic, Weather/Quad2") # Publish 6am > 12pm raingauge amount
client.publish("Weather/Quad2", quad2amount, qos=2)
time.sleep(2)
print("Publishing message to topic, Weather/Quad3") # Publish 12pm > 18pm raingauge amount
client.publish("Weather/Quad3", quad3amount, qos=2)
time.sleep(2)
print("Publishing message to topic, Weather/Quad4") # Publish 18pm > 24pm raingauge amount
client.publish("Weather/Quad4", quad4amount, qos=2)
time.sleep(2)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
