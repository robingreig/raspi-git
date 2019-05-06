#! /usr/bin/python3

import paho.mqtt.subscribe as subscribe
msg = subscribe.simple("esp32/temperature", hostname="localhost")
print("%s, %s" % (msg.topic, msg.payload))
