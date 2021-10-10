#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
broker_address = "192.168.200.137"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
print("Connecting to broker")
client.connect(broker_address) # connect to broker
print("Subscribing to topic, OutTemp")
client.subscribe("OutTemp")
print("Publishing message to topic", "OutTemp")
client.publish("OutTemp","28")
