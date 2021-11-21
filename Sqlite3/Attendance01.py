#!/usr/bin/python3

import sqlite3
import time
import os

# Establish sqlite3 database connection to 'makerSpace.db'
dbc = sqlite3.connect('makerSpace.db')

# To debug program debug > 0
debug = 0

# Short Delay
delay1 = 2
# Long Delay
delay2 = 5

# Did they sign a waiver? waiverSign == 1
waiverSign = 0

# Did they sign in today?
#  0 = Not signed in
#  1 = Signed in but not signed out
#  2 = Signed in and signed out
signIn = 0

while True:
#	 Clear the screen
    if debug == 0:
        os.system('clear')
    waiverSign = 0
    signIn = 0
#	 Scan SAIT Barcode
    sait =  input("\n\n\nPlease scan your SAIT ID: ")
    if debug > 0:
        print("\nYour SAIT ID: ",sait)
        time.sleep(delay1)

#####	Check to see if they in the users list?
    try:
        cursor = dbc.cursor()
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
        for firstName, lastName in cursor:
            if debug > 0:
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nsignIn value: ",signIn)
                print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!\n")
                time.sleep(delay1)
            waiverSign = 1
        if waiverSign == 0:
            print("\nI cannot find you in our list?    Did you sign the waiver?")
            time.sleep(delay1)
    except sqlite3.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()

#####	Have they signed in earlier today, but not signed out? numberRows will indicate number of times
    if waiverSign > 0:
        try:
            cursor = dbc.cursor()
#            cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
            cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = CURRENT_DATE and saitID = '%s'"%(sait))
            results = cursor.fetchone()
#            numberRows = cursor.rowcount
#            if numberRows == 1:
#                signIn = 1
            if results is not None:
                if debug > 0:
                    print('if results is not None has returned a found value')
                signIn = 1
            if debug > 0:
#                print("\nRowcount returned from checking entries today: ", numberRows, "\n")
                print("\nSignIn value should be > 0: ",signIn,"\n")
                print("\nFirst Name: ",firstName)
                print("\nLast Name: ",lastName)
                time.sleep(delay2)
                while results is not None:
                    print("\nResults: ",results)
                    results = cursor.fetchone()
                time.sleep(delay1)
        except sqlite3.Error as error:
            print("\nError#2: {}".format(error))
        finally:
            cursor.close()

#####	Add check out timeOUT to last entry for user
    if waiverSign > 0 and signIn == 1:
#####   Select the record that has the timeIN entry
        try:
            cursor = dbc.cursor()
            if debug > 0:
                print("\nSelect the record with the timeIN entry")
            cursor.execute("SELECT attendID from attendance where timeOUT IS NULL and date = CURRENT_DATE and saitID = '%s'"%(sait))
            results = cursor.fetchone()
            if debug > 0:
                time.sleep(delay1)
                if results is not None:
                    print("\nEntry number found: ",results,"\n")
                    time.sleep(delay1)
        except sqlite3.Error as error:
            print("\nError#2: {}".format(error))
        finally:
            cursor.close()

#####	Update the record that was selected previously
        try:
            cursor = dbc.cursor()
            if debug > 0:
                print("\nUpdate the record that was previously selected")
            cursor.execute("UPDATE attendance set timeOUT = CURRENT_TIME where attendID = '%s'"%(results))
            dbc.commit()
            print("\n",firstName,lastName," Thanks for signing OUT of the MakerSpace today!")
            time.sleep(delay2)
            signIn = 0
            if debug > 0:
                print ("\nDatabase Updated")
                print ("\nThe last inserted ID was: ", cursor.lastrowid)
                print ("\nSignIn value: ",signIn)
                time.sleep(delay1)
        except sqlite3.Error as error:
            print("\nError#2: {}".format(error))
            dbc.rollback()
        finally:
            cursor.close()
            signIn = 2

#####	If they haven't signed in today, then add an entry to the database timeIN
    if waiverSign == 1 and signIn == 0:
        try:
            if debug > 0:
                print("\nYour SAIT ID: ",sait)
                time.sleep(delay1)
            cursor = dbc.cursor()
            cursor.execute("""INSERT into attendance
               (date, timeIN, saitID)
               VALUES
               (CURRENT_DATE,CURRENT_TIME,'%s');""" % (sait))
            dbc.commit()
            print("\n",firstName,lastName," Thanks for signing IN to the MakerSpace today!")
            time.sleep(delay2)
            if debug > 0:
                print ("\nDatabase Updated")
                print ("\nThe last inserted ID was: ", cursor.lastrowid)
                time.sleep(delay1)
        except sqlite3.Error as error:
           print("Error: {}".format(error))
           dbc.rollback()
        finally:
            cursor.close()
dbc.close()

