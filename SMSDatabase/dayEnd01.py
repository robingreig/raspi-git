#!/usr/bin/python3

import sqlite3
import time
import os

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
            cursor.execute("SELECT rowid from attendance where timeOUT IS NULL and date = date('now','localtime')")
            results = cursor.fetchone()
            if results is not None:
                if debug > 0:
                    print('if results is not None has returned a found value')
                    time.sleep(delay1)
                    print("\nthis is the output of Results first time: ",results)
                    time.sleep(delay2)
                    print("\nUpdate the record that was previously selected")
                    time.sleep(delay1)
                cursor.execute("UPDATE attendance set timeOUT = time('now','localtime') where rowid = ?", (results))
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

