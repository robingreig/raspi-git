#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt # import the client

######
def on_message(client, userdata, message):
  print("message received ", str(message.payload.decode("utf-8")))
  print("message topic: ",message.topic)
  print("message qos: ",message.qos)
  print("message retain flag: ",message.retain)
#####
broker_address="192.168.200.37"
print("creating new instance")
client=mqtt.Client("Zero3") # create new instance
client.on_message=on_message # attach function to callback
print("connecting to broker")
client.connect(broker_address) # connect to broker
client.loop_start() # start the loop
print("Subscribing to topic", "LED01")
client.subscribe("LED01")
#print("Publishing a message to topic: ","LED01")
#client.publish("Irricana/StoveFan","on") # publish
#client.publish("LED01","false") # publish
#time.sleep(5)
client.loop_stop() #stop the loop
client.loop_start() # start the loop
print("Subscribing to topic", "LED01")
client.subscribe("LED01")
#print("Publishing a message to topic: ","LED01")
#client.publish("Irricana/StoveFan","on") # publish
#client.publish("LED01","true") # publish
#time.sleep(5)
client.loop_stop() #stop the loop
