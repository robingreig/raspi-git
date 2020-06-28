#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
import time
#####
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

#####
def on_log(client, userdata, level, buf):
    print("log: ",buf)
#####
mqtt.Client.connected_flag=False # create flag in class

broker = "192.168.200.37"

print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
client.on_log=on_log
client.on_connect=on_connect # bind callback function

client.loop_start() # start the loop
print("Connecting to broker ",broker)
client.connect(broker) # connect to broker
while not client.connected_flag: # wait in loop
  print("In wait loop")
  time.sleep(1)
print("in Main Loop")
print("Publishing message to topic", "TestTemp")
client.publish("TestTemp","26", qos = 2)
print("Publishing message to topic", "SolarBatt")
client.publish("SolarBatt","26.1", qos = 2)
print("Publishing message to topic", "GarageBatt")
client.publish("GarageBatt","25.06", qos = 2)
print("Publishing message to topic", "HamBatt")
client.publish("HamBatt","13.72", qos = 2)
print("Publishing message to topic", "SpareBatt")
client.publish("SpareBatt","13.62", qos = 2)
time.sleep(4) # wait
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
