#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import datetime
import os
import glob
import logging

# Add a delay for boot
time.sleep(1)
DEBUG = 1

# Assign one wire devices
base_dir = '/sys/bus/w1/devices/'
# Inside Sensor *72f1
device_folder1 = glob.glob(base_dir + '*72f1')[0]
device_file1 = device_folder1 + '/w1_slave'
# Outside Sensor #a085
device_folder2 = glob.glob(base_dir + '*a085')[0]
device_file2 = device_folder2 + '/w1_slave'
   
def read_temp_raw1():
    f = open(device_file1, 'r')
    lines1 = f.readlines()
    f.close()
    return lines1

def read_temp_raw2():
    f = open(device_file2, 'r')
    lines2 = f.readlines()
    f.close()
    return lines2

def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines1 = read_temp_raw1()
    equals_pos = lines1[1].find('t=')
    if equals_pos != -1:
        temp_string = lines1[1][equals_pos+2:]
        temp_c1 = round((float(temp_string) / 1000.0),2)
        return temp_c1

def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines2 = read_temp_raw2()
    equals_pos = lines2[1].find('t=')
    if equals_pos != -1:
        temp_string = lines2[1][equals_pos+2:]
        temp_c2 = round((float(temp_string) / 1000.0),2)
        return temp_c2
temp1 = read_temp1()
temp2 = read_temp2()
if DEBUG > 0:
  print ("Inside Temp: ", (read_temp1()))
  print ("Inside Temp: ", temp1)
  print ("Outside Temp: ", (read_temp2()))
  print ("Outside Temp: ", temp2)

# store outside temp to monitor with coldStart.py
cht = open("/home/robin/outsideTemp", "w")
cht.write (str(temp2))
cht.close()

if  DEBUG > 0:
    if temp1 < -18:
        print("temp1 < -18")
    else:
        print("temp1 > -18")

time.sleep(1)

#### upload temps to mqtt broker

#broker_address = "mqtt21.local"
broker_address = "192.168.200.21"
print("Creating new instance & starting logging")
logging.basicConfig(level=logging.INFO) # use DEBUG, INFO, WARNING

def on_log(client, userdata, level, buf):
  logging.info(buf)

def on_connect(client, userdata, flags, rc):
  if rc==0:
    client.connected_flag=True # set flag
    logging.info("connected OK")
  else:
    logging.info("Bad Connection Returned Code = "+str(rc))
    client.loop_stop()

def on_disconnect(client, userdata, rc):
  logging.info("client disconnected OK")

def on_publish(client, userdata, mid):
  logging.info("In on_pub callback mid = " +str(mid))

mqtt.Client.connected_flag=False # create flag in class

client = mqtt.Client("P1") # create a new instance for first topic
client.on_log = on_log # display log entries
client.on_connect = on_connect # bind callback function
client.on_disconnect = on_disconnect # bind callback function
client.on_publish = on_publish # bind callback function

logging.info("Connecting to broker: "+str(broker_address))
client.connect(broker_address) # connect to broker

client.loop_start() # start the loop

while not client.connected_flag:
  logging.info("In Wait Loop")
  time.sleep(1)

logging.info("In Main Loop")
logging.info("Publishing message to topic, BlockHeat/BlockInTemp")
ret=client.publish("BlockHeat/BlockInTemp", temp1, qos=2)
logging.info("Published return: "+str(ret))
time.sleep(2)
logging.info("Publishing message to topic, BlockHeat/BlockOutTemp")
ret=client.publish("BlockHeat/BlockOutTemp", temp2, qos=2)
logging.info("Published return:"+str(ret))
time.sleep(2)
logging.info("Stopping the loop")
client.loop_stop() # stop the loop
client.disconnect() # disconnect
