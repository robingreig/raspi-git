#!/usr/bin/env python3

import time

# Subscribe to a topic
import paho.mqtt.client as mqtt # import the client
broker_address="192.168.200.37"
client=mqtt.Client("Zero3") # create new instance
client.connect(broker_address) # connect to broker
#client.publish("Irricana/StoveFan","on") # publish
client.publish("LED01","on") # publish
time.sleep(5)
client.publish("LED01","off") #publish
