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

broker_address = "192.168.200.21"
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
print("Publishing message to topic, BlueOrange") # Adc0 = Blue CAT5 / Orange Wire = Solar Batteries
client.publish("Garage/BlueOrange", Adc0, qos=2)
time.sleep(2)
print("Publishing message to topic, BlueBlue") # Adc1 = Blue CAT5 / Blue Wire = Garage Batteries
client.publish("Garage/BlueBlue", Adc1, qos=2)
time.sleep(2)
print("Publishing message to topic, WhiteBrown") # Adc2 = White CAT5 / Brown Wire = Ham Battery
client.publish("Garage/WhiteBrown", Adc2, qos=2)
time.sleep(2)
print("Publishing message to topic, WhiteOrange") # Adc3 = White CAT5 / Orange Wire = Trailer Batteries
client.publish("Garage/WhiteOrange", Adc3, qos=2)
time.sleep(2)
print("Publishing message to topic, WhiteGreen") # Adc4 = White CAT5 / Green Wire = 
client.publish("Garage/WhiteGreen", Adc4, qos=2)
time.sleep(2)
print("Publishing message to topic, WhiteBlue") # Adc5 = White CAT5 / Blue Wire = 
client.publish("Garage/WhiteBlue", Adc5, qos=2)
print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect
