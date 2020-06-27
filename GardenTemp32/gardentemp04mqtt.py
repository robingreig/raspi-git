#!/usr/bin/env python3

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
        temp_c1 = float(temp_string) / 1000.0
        return temp_c1

def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines2 = read_temp_raw2()
    equals_pos = lines2[1].find('t=')
    if equals_pos != -1:
        temp_string = lines2[1][equals_pos+2:]
        temp_c2 = float(temp_string) / 1000.0
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
print ("Display last row")
for row in cursor.execute("Select currentdate, currentime, insidetemp, outsidetemp from coldframe order by currentdate desc, currentime desc limit 1"):
    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))
print ()
print ("Display temp rows using select *")
for row in cursor.execute("Select * from coldframe order by currentdate desc, currentime desc limit 1"):
    temp1 = row[1]
    print ("temp1 = Black Temp = insidetemp = ",temp1)
    temp2 = row[2]
    print ("temp2 Red Temp = outsidetemp= ",temp2)



db.close()
