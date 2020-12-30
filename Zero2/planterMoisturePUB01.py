#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt

time.sleep(1)
ch0 = open("/home/robin/CurrentADC0", "r")
Adc0 = ch0.read()
ch0.close()
print("ADC0 = ", Adc0)

#### upload temps to mqtt broker
def on_message(client, userdata, message):
    print("Message received = ", str(message.payload.decode("utf-8")))
    print("Message topic = ", message.topic)
    print("Message qos = ", message.qos)
    print("Message retain flag = ", message.retain)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

broker_address = "mqtt37.local"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_message = on_message # attach function to callback
print("Connecting to broker")
client.connect(broker_address) # connect to broker
print("Publishing message to topic, gardenWater/Planter01") # First Planter is Adc0
client.publish("gardenWater/Planter01", Adc0)
