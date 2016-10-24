#!/usr/bin/python

import paho.mqtt.publish as publish
import time

print("Sending 0...")
publish.single("ledStatus", "0", hostname="raspi13")
time.sleep(1)
print("Sending 1...")
publish.single("ledStatus", "1", hostname="raspi13")
