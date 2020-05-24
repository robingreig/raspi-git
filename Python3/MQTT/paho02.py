#! /usr/bin/python3

import paho.mqtt.subscribe as subscribe
#msg = subscribe.simple("esp32/temperature", hostname="localhost")
msg = subscribe.simple("OutTemp", hostname="localhost")
print("%s, %s" % (msg.topic, msg.payload))
print("Message Payload: ",(msg.payload))
text = str(msg.payload, 'utf-8', 'ignore')
print("Text: ",(text))
