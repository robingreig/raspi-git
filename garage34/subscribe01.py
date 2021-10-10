#! /usr/bin/python3

import paho.mqtt.subscribe as subscribe

for i in range(6):
  #  msg = subscribe.simple("esp32/temperature", hostname="localhost")
    msg = subscribe.simple("Garage/FurnaceHeat", hostname="mqtt21.local")
    print("%s, %s" % (msg.topic, msg.payload))
    print("Message Payload: ",(msg.payload))
    text = str(msg.payload, 'utf-8', 'ignore')
    print("Text: ",(text))
