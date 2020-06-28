#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt
import battmon24adc02


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

broker_address = "192.168.200.37"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_connect=on_connect # bind callback function

client.loop_start() # start the loop
print("Connecting to broker ",broker_address)
client.connect(broker_address) # connect to broker

while not client.connected_flag:
  print("In Wait Loop")
  time.sleep(1)

print("In Main Loop")
print("Publishing message to topic, SolarBatt") # Solar Batteries are Adc0
client.publish("SolarBatt", Adc0, qos=2)
time.sleep(1)
print("Publishing message to topic, GarageBatt") # Garage Batteries are Adc1
client.publish("GarageBatt", Adc1, qos=2)
time.sleep(1)
print("Publishing message to topic, HamBatt") # Ham Battery is Adc2
client.publish("HamBatt", Adc2, qos=2)
time.sleep(1)
print("Publishing message to topic, SpareBatt") # Spare Battery is Adc3
client.publish("SpareBatt", Adc3, qos=2)
#time.sleep(1)
#print("Publishing message to topic, Batt04") # Batteries are Adc4
#client.publish("SolarBatt", Adc0)
#time.sleep(1)
#print("Publishing message to topic, Batt05") # Batteries are Adc5
#client.publish("SolarBatt", Adc0)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
