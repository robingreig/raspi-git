#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
import time
#####
def on_message(client, userdata, message):
    print("Message received ", str(message.payload.decode("utf-8")))
    print("Message topic = ", message.topic)
    print("Message qos = ", message.qos)
    print("Message retain flag = ", message.retain)
#####
broker_address = "192.168.200.137"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
client.on_message=on_message # attach function to callback
print("Connecting to broker")
client.connect(broker_address) # connect to broker
client.loop_start() # start the loop
print("Subscribing to topic, OutTemp")
client.subscribe("OutTemp")
print("Publishing message to topic", "OutTemp")
client.publish("OutTemp","25")
time.sleep(4) # wait
client.loop_stop() # stop the loop
