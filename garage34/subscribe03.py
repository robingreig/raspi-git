#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
import time
#####
def on_message(client, userdata, message):
    print("Message received ", str(message.payload.decode("utf-8")),"topic = ", message.topic,"qos = ", message.qos,"retained  = ", message.retain)
    if message.retain==1:
        print("This is a retained message")
#    print("Message received ", str(message.payload.decode("utf-8")))
#    print("Message topic = ", message.topic)
#    print("Message qos = ", message.qos)
#    print("Message retain flag = ", message.retain)
#####
broker_address = "192.168.200.21"
print("Creating new instance")
client = mqtt.Client("G34") # create a new instance
client.on_message=on_message # attach function to callback
print("Connecting to broker")
client.connect(broker_address) # connect to broker
client.loop_start() # start the loop
print("Subscribing to topic, Garage/FurnaceTemp")
client.subscribe("Garage/FurnaceTemp")
#print("Publishing message to topic", "Garage/FurnaceTemp")
#client.publish("Garage/FurnaceTemp","23",qos=1,retain=True)
print("Subscribing to topic, Garage/FurnaceHeat")
client.subscribe("Garage/FurnaceHeat")
#print("Publishing message to topic", "Garage/FurnaceHeat")
#client.publish("Garage/FurnaceHeat","22",qos=1,retain=True)
time.sleep(2) # wait
client.loop_stop() # stop the loop
