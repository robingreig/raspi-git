#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = ('Goran Poprzen')
__license__ = 'Private'
__version__ = '2015.12.26'

import MySQLdb
import temperature

# =============================================================================
# database: thermodb
# =============================================================================
# table: sensors
# -------------------------------------------------------------------
# id, int(11) Auto Increment, primary
# sernum, varchar(32)
#       sensor's serial number, e.g. '28-0000034d0840'
# name, varchar(255)
#       sensor's name, may denote placement, e.g. 'Garage' or 'Top floor'
# active, tinyint(4)
#       0 if sensor's not active
# =============================================================================
# table: templog
# -------------------------------------------------------------------
# id, int(11) Auto Increment, primary
# sensor_id, int(11), index, foreign key target: sensors(id)
# date, date
# time, time
# temperature, double
# =============================================================================

devices_path = '/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves'

dbconn = MySQLdb.connect(host="localhost", user="thermousr", passwd="temperature", db="thermodb")

dbcur = dbconn.cursor()

if __name__ == "__main__":
    # read list of devices from /sys/...
    sensors_list = temperature.read_lines(devices_path)
    # for each device
    for sensor in sensors_list:
        # read from /sys/.../28-000.../w1_slave
        result = temperature.read(sensor)
        print result
        # check if this sensor is in database
        sqlquery = "SELECT * FROM sensors WHERE sernum = '" + sensor + "'"
        sensrow = dbcur.execute(sqlquery)
        # if crc_good == YES
        if result[0] == "YES":
            # if sensor exists in db
            if sensrow != 0:
                # update sensor's active = true
                sql_update = "UPDATE sensors SET active = 1 WHERE sernum = '" + sensor + "'"
                try:
                    dbcur.execute(sql_update)
                    dbconn.commit()
                except:
                    dbconn.rollback()
            else:
                # new sensor - insert into sensors 'device, etc.'
                sql_insert = "INSERT INTO sensors (sernum, name, active) VALUES ('" + sensor + "', 'default name', 1)"
                try:
                    dbcur.execute(sql_insert)
                    dbconn.commit()
                except:
                    dbconn.rollback()
        # crc not good
        if result[0] == "NO":
            # sensor was in db
            if sensrow != 0:
                # deactivate - update active = false
                sql_update = "UPDATE sensors SET active = 0 WHERE sernum = '" + sensor + "'"
                try:
                    dbcur.execute(sql_update)
                    dbconn.commit()
                except:
                    dbconn.rollback()
                
        
    dbcur.close()
    dbconn.close()
