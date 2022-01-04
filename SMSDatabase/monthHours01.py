#!/usr/bin/python3

import sqlite3
import time
import os
import datetime as dt

# Establish sqlite3 database connection to 'makerSpace.db'
dbc = sqlite3.connect('/home/robin/makerspace.db')

# To TURN OFF debug program debug = 0
#debug = 0
# To TURN ON debug, will break without results, debug = 1
debug = 1

# Short Delay
delay1 = 2


diffTotal = dt.datetime.strptime('00:00:00', '%H:%M:%S')

####	Total number of member hours per day
try:
    cursor = dbc.cursor()
### cursor.execute +2 days to test WITHOUT data!
    cursor.execute("SELECT timeIN, timeOUT from attendance where date like '2021-12%'")
#    cursor.execute("SELECT timeIN, timeOUT from attendance where date = date('now','localtime','-1 days')")
#    cursor.execute("SELECT timeIN, timeOUT from attendance where date = date('now','localtime')")
    results = cursor.fetchall()
    if results is not None:
#    if results != None:
        print("All results = :",results)
        for i in results:
            if debug > 0:
                print("All of i = ",i)
                print("First part of i[0] = ", i[0])
                print("Second part of i[1] = ",i[1])
#                time.sleep(delay1)
#            Strip off year/month/day from newTime0 string
            newTime0 = dt.datetime.strptime(i[0],'%H:%M:%S')
            if debug > 0:
                print("newTime0 = ",newTime0)
#                time.sleep(delay1)
#            Strip off year/month/day from newTime1 string
            newTime1 = dt.datetime.strptime(i[1],'%H:%M:%S')
            if debug > 0:
                print("newTime1 = ",newTime1)
#                time.sleep(delay1)
            diff = newTime1 - newTime0
            if debug > 0:
                print("Difference = ",diff)
#                time.sleep(delay1)
            diffTotal = diffTotal + diff
#            Strip off year/month/day from totalTime datetime.timedelta
            totalTime = dt.datetime.strftime(diffTotal,'%H:%M:%S')
            if debug > 0:
                print("diffTotal = ",diffTotal)
#                time.sleep(delay1)
        if debug > 0:
            print("totalTime = ",totalTime)
#            time.sleep(delay1)
except sqlite3.Error as error:
    print("\nError#2: {}".format(error))
finally:
    cursor.close()
dbc.close()

