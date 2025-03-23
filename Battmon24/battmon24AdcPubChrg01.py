#!/usr/bin/python3

import os
import time
import paho.mqtt.client as mqtt
# Measure battery voltages and save them to the files
import battmon24adc02
# Publish the voltages from the files to mqtt
import battmon24pub06


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

#### upload temps to mqtt broker
def on_message(client, userdata, message):
    print("Message received = ", str(message.payload.decode("utf-8")))
    print("Message topic = ", message.topic)
    print("Message qos = ", message.qos)
    print("Message retain flag = ", message.retain)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

broker_address = "192.168.200.37"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_message = on_message # attach function to callback
print("Connecting to broker")
client.connect(broker_address) # connect to broker
print("Publishing message to topic, SolarBatt") # Solar Batteries are Adc0
client.publish("SolarBatt", Adc0, qos=1)
time.sleep(20)
print("Publishing message to topic, GarageBatt") # Garage Batteries are Adc1
client.publish("GarageBatt", Adc1, qos=1)
time.sleep(20)
print("Publishing message to topic, HamBatt") # Ham Battery is Adc2
client.publish("HamBatt", Adc2, qos=1)
time.sleep(20)
print("Publishing message to topic, SpareBatt") # Spare Battery is Adc3
client.publish("SpareBatt", Adc3, qos=1)
#print("Publishing message to topic, Batt04") # Batteries are Adc4
#client.publish("SolarBatt", Adc0)
#print("Publishing message to topic, Batt05") # Batteries are Adc5
#client.publish("SolarBatt", Adc0)
