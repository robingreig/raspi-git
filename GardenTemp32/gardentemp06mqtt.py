#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import datetime
import sqlite3
import os
import glob

# ===========================================================================
# Open Database Connection
# ===========================================================================

db = sqlite3.connect('/home/robin/gardentemp.db')

# Prepare a cursor
cursor = db.cursor()

# ==========================================================================
# Insert into table - variable
# ==========================================================================

# Add a delay for boot
time.sleep(1)

# Assign one wire devices
base_dir = '/sys/bus/w1/devices/'
device_folder1 = glob.glob(base_dir + '*2902')[0]
device_file1 = device_folder1 + '/w1_slave'
device_folder2 = glob.glob(base_dir + '*4478')[0]
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

print ("Black Temp: ", (read_temp1()))
print ("Red Temp: ", (read_temp2()))
  	
time.sleep(1)
  
try:
  cursor.execute('''INSERT INTO coldframe(insidetemp, outsidetemp, currentdate, currentime)
	VALUES(?,?,date('now'), time('now'))''', (read_temp1(), read_temp2()))
  db.commit()
except:
  db.rollback()

print ("Wrote a new row to the database")
for row in cursor:
    # row[0] returns the first column in the query = currentdate?, row[1] returns currentime?.
    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))

print ()
print ("Display last row using select individual columns")
for row in cursor.execute("Select currentdate, currentime, insidetemp, outsidetemp from coldframe order by currentdate desc, currentime desc limit 1"):
    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))
print ()
print ("Display temp rows using select *")
for row in cursor.execute("Select * from coldframe order by currentdate desc, currentime desc limit 1"):
    temp1 = row[1]
    print ("temp1 = Black Temp = insidetemp = ",temp1)
    temp2 = row[2]
    print ("temp2 = Red Temp = outsidetemp= ",temp2)
    curr1 = row[4]
    print ("Time= ",curr1)
    curr2 = row[3]
    print ("Date= ",curr2)

#### upload temps to mqtt broker


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)


def on_log(client, userdata, level, buf):
    print("log: ",buf)

mqtt.Client.connected_flag=False # create flag in class

broker_address = "mqtt37.local"
print("Creating new instance")
client = mqtt.Client("P1") # create a new instance
print("Display log entries")
client.on_log = on_log # display log entries
client.on_connect = on_connect # bind callback function

client.loop_start() # start the loop
print("Connecting to broker:",broker_address)
client.connect(broker_address) # connect to broker

while not client.connected_flag:
  print("In Wait Loop")
  time.sleep(1)

print("In Main Loop")
print("Publishing message to topic, OutTemp")
client.publish("OutTemp", temp2, qos=2)
time.sleep(1)
print("Publishing message to topic, InTemp")
client.publish("InTemp", temp1, qos=2)

print("Stopping the loop")
client.loop_stop() # stop the loop
print("Disconnecting")
client.disconnect() # disconnect

db.close()
