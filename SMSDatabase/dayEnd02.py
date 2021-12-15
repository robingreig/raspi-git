#!/usr/bin/python3

import sqlite3
import time
import os
import datetime as dt

# Establish sqlite3 database connection to 'makerSpace.db'
dbc = sqlite3.connect('/home/robin/makerspace.db')

# To debug program debug > 0
debug = 0

# Short Delay
delay1 = 2
# Long Delay
delay2 = 5

count = 1

while count > 0:
#####	Have they signed in earlier today, but not signed out? numberRows will indicate number of times
        try:
            cursor = dbc.cursor()
            cursor.execute("SELECT rowid, timeIN from attendance where timeOUT IS NULL and date = date('now','localtime')")
            results = cursor.fetchone()
            if results is not None:
                if debug > 0:
                    print('if results is not None has returned a found value')
                    time.sleep(delay1)
                    print("\nthis is the output of both Results: ",results)
                    time.sleep(delay1)
                    print("\nthis is the output of the first Results: ",results[0])
                    time.sleep(delay1)
                    print("\nthis is the output of the second Results: ",results[1])
                    time.sleep(delay1)
##### Found on the internet & works, but I don't fully understand it?
###                diff = timedelta() # Initialize diff = 0
###                def parse_ts(ts: str) -> timedelta:
###                   h, m, s = ts.split(':')
###                   return timedelta(hours=int(h), minutes=int(m), seconds=int(s))
###                timestamps = [('06:33:11', '02:00:00')]
###                timestamps = [(results[1], '02:00:00')]
###                for start, end in timestamps:
###                   diff += parse_ts(start) + parse_ts(end)
###                print("Difference in time = ",diff)

##### Convert result[1] (timeIN) to datetime format, then add 2 hours (timedelta) and then return only time portion
#               Convert results[1] to datetime format
                newResult1 = dt.datetime.strptime(results[1],'%H:%M:%S')
                if debug > 0:
                    print("\nnewResult = ",newResult1)
#               Add 2 hours to the newResult1
                newResult2 = newResult1 + dt.timedelta(hours=2)
                if debug > 0:
                    print("\nnewResult2 = ",newResult2)
                    time.sleep(delay1)
#               Strip off year/month/day from newTime
                newTime = dt.datetime.strftime(newResult2,'%H:%M:%S')
                if debug > 0:
                    print("\nnewTime = Time Only = ",newTime)
                    time.sleep(delay1)
                if debug > 0:
                    print("\nUpdate the record that was previously selected")
                    time.sleep(delay1)
###                cursor.execute("UPDATE attendance set timeOUT = time('now','localtime') where rowid = ?", (results))
###                cursor.execute("UPDATE attendance set timeOUT = newTime where rowid = ?", (results[0]))
                cursor.execute("UPDATE attendance set timeOUT = ? where rowid = ?", (newTime,results[0]))
                if debug > 0:
                    print ("\nDatabase Updated with Update command")
                    time.sleep(delay2)
                dbc.commit()
                if debug > 0:
                    print ("\nDatabase Committed")
                    time.sleep(delay2)
            else:
              count = 0
        except sqlite3.Error as error:
            print("\nError#2: {}".format(error))
            dbc.rollback()
        finally:
            cursor.close()

dbc.close()

