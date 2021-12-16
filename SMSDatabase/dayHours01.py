#!/usr/bin/python3

import sqlite3
import time
import os
import datetime as dt

# Establish sqlite3 database connection to 'makerSpace.db'
dbc = sqlite3.connect('/home/robin/makerspace.db')

# To debug program debug > 0
debug = 1

# Short Delay
delay1 = 2
# Long Delay
delay2 = 5

diffTotal = dt.datetime.strptime('00:00:00', '%H:%M:%S')

while True:

#####	Have they signed in earlier today, but not signed out? numberRows will indicate number of times
    try:
        cursor = dbc.cursor()
        cursor.execute("SELECT timeIN, timeOUT from attendance where date = date('now','localtime')")
        results = cursor.fetchall()
        if results is not None:
            if debug > 0:
                print("\nResults: ",results)
#                time.sleep(delay1)
            print("results[0] = ",results[0])
            print("results[1] = ",results[1])
            for i in results:
                if debug > 0:
                    print("All of i = ",i)
                    print("First part of i[0] = ", i[0])
                    print("Second part of i[1] = ",i[1])
#               Strip off year/month/day from newTime
                newTime0 = dt.datetime.strptime(i[0],'%H:%M:%S')
                if debug > 0:
                    print("newTime0 = ",newTime0)
                newTime1 = dt.datetime.strptime(i[1],'%H:%M:%S')
                if debug > 0:
                    print("newTime1 = ",newTime1)
                diff = newTime1 - newTime0
                if debug > 0:
                    print("Difference = ",diff)
#                diffStr = dt.datetime.strftime(diff)
                diffTotal = diffTotal + diff
                if debug > 0:
                    totalTime = dt.datetime.strftime(diffTotal,'%H:%M:%S')
                    print("diffTotal = ",diffTotal)
                    print("totalTime = ",totalTime)
        else:
            if debug > 0:
                print("Didn't find any results")
            break
    except sqlite3.Error as error:
        print("\nError#2: {}".format(error))
    finally:
        cursor.close()
    time.sleep(delay1)
dbc.close()

