#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
broker_address = "192.168.200.21"
print("Creating new instance")
client = mqtt.Client("G34") # create a new instance
print("Connecting to broker")
client.connect(broker_address) # connect to broker
print("Subscribing to topic, Garage/FurnaceHeat")
client.subscribe("Garage/FurnaceHeat")
print("Publishing message to topic", "Garage/FurnaceHeat")
client.publish("Garage/FurnaceHeat","23")
