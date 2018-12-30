#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')
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

#	Check to see if they in the users list?
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
        for firstName, lastName in cursor:
#            print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
#            time.sleep(delay1)
            if debug > 0:
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nsignIn value: ",signIn)
                time.sleep(delay2)
            waiverSign = 1
        if waiverSign == 0:
            print("\nI cannot find you in our list?    Did you sign the waiver?")
            time.sleep(delay2)
    except mariadb.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()

#	Have they signed in earlier today, but not signed out? numberRows will indicate number of times
    if waiverSign > 0:
        try:
            cursor = mariadb_connection.cursor()
#            cursor.execute("SELECT * from attendance where date = curdate() and saitID = '%s'"%(sait))
            cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
            results = cursor.fetchone()
            numberRows = cursor.rowcount
            if numberRows == 1:
                signIn = 1
            if debug > 0:
                print("\nRowcount returned from checking entries today: ", numberRows, "\n")
                print("\nIf number of rows < 1, SignIn value should be 0 > ",signIn,"\n")
                print("\nFirst Name: ",firstName)
                print("\nLast Name: ",lastName)
                time.sleep(delay2)
                while results is not None:
                    print("\nResults: ",results)
                    results = cursor.fetchone()
                time.sleep(delay2)
        except mariadb.Error as error:
            print("\nError#2: {}".format(error))
        finally:
            cursor.close()

#	Add check out timeOUT to last entry for user
    if waiverSign > 0 and signIn == 1:
#       Select the record that has the timeIN entry
        try:
            cursor = mariadb_connection.cursor()
            if debug > 0:
                print("\nSelect the record with the timeIN entry")
            cursor.execute("SELECT attendID from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
            results = cursor.fetchone()
            numberRows = cursor.rowcount
            if debug > 0:
                print("\nRowcount from Select the record with the timeIN entry: ", numberRows, "\n")
                time.sleep(delay1)
                if results is not None:
                    print("\nEntry number found: ",results,"\n")
                    time.sleep(delay1)
        except mariadb.Error as error:
            print("\nError#2: {}".format(error))
        finally:
            cursor.close()

#	Update the record that was selected previously
        try:
            cursor = mariadb_connection.cursor()
            if debug > 0:
                print("\nUpdate the record that was previously selected")
            cursor.execute("UPDATE attendance set timeOUT = NOW() where attendID = '%s'"%(results))
            mariadb_connection.commit()
            print("\n",firstName,lastName," Thanks for signing OUT of the MakerSpace today!")
            time.sleep(delay2)
            signIn = 0
            if debug > 0:
                print ("\nDatabase Updated")
                print ("\nThe last inserted ID was: ", cursor.lastrowid)
                print ("\nSignIn value: ",signIn)
                time.sleep(delay1)
        except mariadb.Error as error:
            print("\nError#2: {}".format(error))
            mariadb_connection.rollback()
        finally:
            cursor.close()
            signIn = 2

#	If they haven't signed in today, then add an entry to the database timeIN
    if waiverSign == 1 and signIn == 0:
        try:
            if debug > 0:
                print("\nYour SAIT ID: ",sait)
                time.sleep(delay1)
            cursor = mariadb_connection.cursor()
            cursor.execute("""INSERT into attendance
               (date, timeIN, saitID)
               VALUES
               (NOW(),NOW(),'%s');""" % (sait))
            mariadb_connection.commit()
            print("\n",firstName,lastName," Thanks for signing IN to the MakerSpace today!")
            time.sleep(delay2)
            if debug > 0:
                print ("\nDatabase Updated")
                print ("\nThe last inserted ID was: ", cursor.lastrowid)
                time.sleep(delay1)
        except mariadb.Error as error:
           print("Error: {}".format(error))
           mariadb_connection.rollback()
        finally:
            cursor.close()

mariadb_connection.close()

