#!/usr/bin/python3
# battmon24AdcPubChrg02.py
# 2025.03.23
# Adding GPIO17 & 27 as outputs to control both 120V Battery chargers

import os
import time
import paho.mqtt.client as mqtt

# Measure battery voltages and save them to the files
#import battmon24adc02

# Publish the voltages from the files to mqtt
#import battmon24pub06

# gpiozero sets up GPIO 
from gpiozero import LED

# setup pin 17 as output 1 for battery charger
chrg1 = LED(17)

# setup pin 27 as output 2 for battery charger
chrg2 = LED(27)

# Print messages if DEBUG > 0
DEBUG = 0

ch0 = open("/home/robin/CurrentAdc0Volts", "r")
Adc0 = ch0.read()
ch0.close()
print("ADC0 = ", Adc0)
ch1 = open("/home/robin/CurrentAdc1Volts", "r")
Adc1 = ch1.read()
ch1.close()
print("ADC1 = ", Adc1)
ch2 = open("/home/robin/CurrentAdc2Volts", "r")
Adc2 = ch2.read()
ch2.close()
print("ADC2 = ", Adc2)
ch3 = open("/home/robin/CurrentAdc3Volts", "r")
Adc3 = ch3.read()
ch3.close()
print("ADC3 = ", Adc3)
ch4 = open("/home/robin/CurrentAdc4Volts", "r")
Adc4 = ch4.read()
ch4.close()
print("ADC4 = ", Adc4)
ch5 = open("/home/robin/CurrentAdc5Volts", "r")
Adc5 = ch5.read()
ch5.close()
print("ADC5 = ", Adc5)

#### upload voltages to mqtt broker

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False # create flag in class

broker_address = "192.168.200.143"
#broker_address = "192.168.200.21"
#broker_address = "mqtt21.local"
print("Creating new instance")
client = mqtt.Client("BM24") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_connect=on_connect # bind callback function

print("Connecting to broker ",broker_address)
client.connect(broker_address) # connect to broker

client.loop_start() # start the loop

while not client.connected_flag:
    print("In Wait Loop")
    time.sleep(1)

print("In Main Loop")
Adc0 = float(Adc0)
if Adc0 < 24.0:
    print("Input 0: ",Adc0,"V")
    print("Publishing message to topic, esp8266/22/relay1") # Relay 1 =  Solar Batteries
    print("chrg1 is ON")
    client.publish("esp8266/22/relay1", "on", qos=2)
    chrg1.on()
else:
    print("Publishing message to topic, esp8266/22/relay1") # Relay 1 =  Solar Batteries
    client.publish("esp8266/22/relay1", "off", qos=2)
    print("chrg1 is OFF")
    chrg1.off()
time.sleep(1)
Adc1 = float(Adc1)
if Adc1 < 24.0:
    print("Input 1: ",Adc1,"V")
    print("Publishing message to topic, esp8266/22/relay2") # Relay 2 =  Garage Batteries
    print("chrg2 is ON")
    client.publish("esp8266/22/relay2", "on", qos=2)
    chrg2.on()
else:
    print("Publishing message to topic, esp8266/22/relay2") # Relay 2 =  Garage Batteries
    print("chrg2 is OFF")
    client.publish("esp8266/22/relay2", "off", qos=2)
    chrg2.off()
time.sleep(1)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
