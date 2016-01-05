#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = ('Goran Poprzen')
__license__ = 'Private'
__version__ = '2015.12.27'


import MySQLdb
import temperature

dbconn = MySQLdb.connect(host="localhost", user="thermousr", passwd="temperature", db="thermodb")

dbcur = dbconn.cursor()


# get list of sensors and their ids from the db
sql_show_all = "SELECT id, sernum, name FROM sensors WHERE active != 0"
dbcur.execute(sql_show_all)
dbsensors = dbcur.fetchall()

# get current date/time
curr_date = temperature.current_date()
curr_time = temperature.current_time()

# for each sensor, measure temperature
for sensor_row in dbsensors:
    sensor_id = sensor_row[0]
    sensor_serial = sensor_row[1]
    sensor_name = sensor_row[2]
    
    result = temperature.read(sensor_serial)
    good_reading = result[0]
    curr_temp = result[1]

    if good_reading == 'YES':
        # insert new record with sensor_id, date, time, temperature
        sql_insert = "INSERT INTO templog (sensor_id, date, time, temperature) VALUES (" + str(sensor_id) + ", '" + str(curr_date) + "', '" + str(curr_time) + "', " + str(curr_temp) + ")"
        try:
            dbcur.execute(sql_insert)
            dbconn.commit()
            print "Successful record:", sensor_id, curr_date, curr_time, curr_temp
        except:
            dbconn.rollback()
            print "Rolling back ..."
    elif good_reading == 'NO':
        print "Wrong checksum!", sensor_id, curr_date, curr_time, curr_temp
        
