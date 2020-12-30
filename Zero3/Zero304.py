#! /usr/bin/python3

import paho.mqtt.client as mqtt # import the client 1
import time

#####
def on_message(client, userdata, message):
    print("Message received ", str(message.payload.decode("utf-8")))
    if str(message.payload.decode("utf-8")) == "true":
      print("********** Fan is off")
    if str(message.payload.decode("utf-8")) == "false":
      print("********** Fan is on")
    print("Message topic = ", message.topic)
    print("Message qos = ", message.qos)
    print("Message retain flag = ", message.retain)
#####

def on_log(client, userdata, level, buf):
    print("log: ",buf)
#####

broker_address = "192.168.200.37"
print("Creating new instance")
client = mqtt.Client("Z3") # create a new instance
client.on_log=on_log
client.on_message=on_message # attach function to callback
print("Connecting to broker")
client.connect(broker_address) # connect to broker
#client.loop_start() # start the loop
print("Subscribing to topic, LED01")
client.subscribe("LED01", qos = 2)
time.sleep(1)
#client.loop_stop() # stop the loop
client.loop_forever() # start the loop
