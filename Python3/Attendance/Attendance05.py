#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
# To debug program debug > 0
debug = 1
# Time Delay for authorized messages
delay1 = 3
# Time Delay for rejection messages
delay2 = 5
# Did they sign a waiver > 0?
waiverSign = 0
# Did they already sign in today?
signIn = 0

while True:
#	 Clear the screen
    if debug == 0:
        os.system('clear')
    waiverSign = 0

#	 Scan SAIT Barcode
    sait =  input ("\n\n\nPlease scan your SAIT ID: ")
    if debug > 0:
        print("\nYour SAIT ID: ",sait)
    user = sait

#	Check to see if they in the users list?
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
        for firstName, lastName in cursor:
            print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
            if debug > 0:
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                time.sleep(delay1)
            time.sleep(delay1)
            waiverSign = 1
        if waiverSign == 0:
            print("\nI cannot find you in our list? Did you sign the waiver?")
            time.sleep(delay2)
        cursor.close()
    except mariadb.Error as error:
        print("\nError#1: {}".format(error))

#	Have they signed in earlier today? numberRows will indicate number of times
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute("SELECT * from attendance where date = curdate() and saitID = '%s'"%(user))
        results = cursor.fetchall()
        numberRows = cursor.rowcount
        if debug > 0:
            print("\nRowcount returned from checking entries today: ", numberRows, "\n")
            time.sleep(delay1)
            for row in results:
                print(row)
        cursor.close()
    except mariadb.Error as error:
        print("\nError#2: {}".format(error))

#	Odd number of rows then they must be checking out?
    if ((numberRows%2==0) & debug > 0):
        signIn = 0
        print("\nScanned times are even")
        print("\nsignIn: ",signIn)
    else:
        signIn = 1
        print("\nScanned times are odd")
        print("\nsignIn: ",signIn)

#	Add check out time timeOUT to last entry for user
    if waiverSign > 0 & signIn > 0:
        try:
            cursor = mariadb_connection.cursor()
            cursor.execute("SELECT * from attendance where date = curdate() and saitID = '%s'"%(user))
            results = cursor.fetchone()
            numberRows = cursor.rowcount
            if debug > 0:
                print("\nRowcount returned from checking entries today: ", numberRows, "\n")
                time.sleep(delay1)
                while results is not None:
                    print("\nOdd number of entries, want to update login entry")
                    print(results)
                    results = results.fetchone()
                    time.sleep(delay1)
            cursor.close()
        except mariadb.Error as error:
            print("\nError#2: {}".format(error))

#	If they haven't signed in today, then add an entry to the database timeIN
#    if waiverSign > 0 & signIn < 1:
#        try:
#            if debug > 0:
#                print("\nYour SAIT ID: ",sait)
#                time.sleep(delay1)
#            cursor = mariadb_connection.cursor()
#            cursor.execute("""INSERT into attendance
#               (date, timeIN, saitID)
#               VALUES
#               (NOW(),NOW(),'%s');""" % (sait))
#            mariadb_connection.commit()
#            if debug > 0:
#                print ("Database Updated")
#                print ("The last inserted ID was: ", cursor.lastrowid)
#                time.sleep(delay1)
#            cursor.close()
##        except mariadb.Error as error:
#           print("Error: {}".format(error))
#           mariadb_connection.rollback()

mariadb_connection.close()

