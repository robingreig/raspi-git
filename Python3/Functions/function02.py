#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')
# To debug program debug > 0
debug = 1

#
def valid_user(sait, debug):
    if debug > 0:
        print("\nSAIT ID from insdie function2 block: ",sait)
    # Set variables
    delay1 = 2 # Delay Time
    waiverSign = 0 # Did user sign a waiver?

    # Check to see if they in the users list (waiverSign =1)
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
        for firstName, lastName in cursor:
            print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
            if debug > 0:
                print ("\nwaiverSign after Welcome message: ",waiverSign)
            waiverSign = 1
            if debug > 0:
                print ("\nwaiverSign after changing it?: ",waiverSign)
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nwaiverSign in debug: ",waiverSign)
        if waiverSign == 0:
            print("\nI cannot find you in our list?    Did you sign the waiver?")
            time.sleep(delay1)
    except mariadb.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()
        saitID = sait
        return{'waiverSign':waiverSign, 'saitID':saitID}

# scan SAIT Barcode
sait =  input("\n\n\nPlease scan your SAIT ID: ")
if debug > 0:
    print("\nYour SAIT ID: ",sait)

# run valid_user function & return variables to dictionary dict1
dict1 = valid_user(sait, debug)
print("\nAll of d is: ",dict1)
if debug > 0:
    print("\nwaiverSign: ",dict1['waiverSign'])
    print("\nsaitID: ",dict1['saitID'])

##	Have they signed in earlier today, but not signed out? numberRows will indicate number of times
#    if waiverSign > 0:
#        try:
#            cursor = mariadb_connection.cursor()
#            cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
#            results = cursor.fetchone()
#            numberRows = cursor.rowcount
#            if numberRows == 1:
#                signIn = 1
#            if debug > 0:
#                print("\nRowcount returned from checking entries today: ", numberRows, "\n")
#                print("\nIf number of rows < 1, SignIn value should be 0 > ",signIn,"\n")
#                print("\nFirst Name: ",firstName)
#                print("\nLast Name: ",lastName)
#                time.sleep(delay2)
#                while results is not None:
#                    print("\nResults: ",results)
#                    results = cursor.fetchone()
#                time.sleep(delay2)
#        except mariadb.Error as error:
#            print("\nError#2: {}".format(error))
#        finally:
#            cursor.close()
#
##	Add check out timeOUT to last entry for user
#    if waiverSign > 0 and signIn == 1:
##       Select the record that has the timeIN entry
#        try:
#            cursor = mariadb_connection.cursor()
#            if debug > 0:
#                print("\nSelect the record with the timeIN entry")
#            cursor.execute("SELECT attendID from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
#            results = cursor.fetchone()
#            numberRows = cursor.rowcount
#            if debug > 0:
#                print("\nRowcount from Select the record with the timeIN entry: ", numberRows, "\n")
#                time.sleep(delay1)
#                if results is not None:
#                    print("\nEntry number found: ",results,"\n")
#                    time.sleep(delay1)
#        except mariadb.Error as error:
#            print("\nError#2: {}".format(error))
#        finally:
#            cursor.close()
#    connection.close()

