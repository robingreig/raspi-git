#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')
# To debug program debug > 0
debug = 1

# Check to see if the barcode scan is a valid user?
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

# Have they signed in earlier today, but not signed out? numberRows will indicate number of times
# signIn = 0 for not signed in today (or signed in & out)
# signIn = 1 for signed in today, but not signed out
def check_signin_today(waiverSign, saitID, debug):
        try:
            # Set local variables, delay1 & signIn
            delay1 = 2
            signIn = 0
            cursor = mariadb_connection.cursor()
            if debug > 0:
                print("\nsaitID inside signin_today funciton is: ",saitID)
            cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(saitID))
            results = cursor.fetchone()
            if results is not None:
                signIn = 1
                if debug > 0:
                    print("\nresults: ",results)
                    print("\nresults[1]: ",results[0])
                    print("\nsignIn from results: ",signIn)
            cursor.close()

            # signIn = 0, then sign them in today
            if signIn == 0:
                try:
                    if debug > 0:
                        print("\nAdding new entry for today")
                    cursor = mariadb_connection.cursor()
                    cursor.execute("""INSERT into attendance
                      (date, timeIN, saitID)
                      VALUES
                      (NOW(),NOW(),'%s');""" %(saitID))
                    mariadb_connection.commit()
                except mariadb.Error as error:
                    print("Error: {}".format(error))
                finally:
                    cursor.close()

            # signIn > 0 then sign them out for today
            if signIn > 0:
                try:
                    if debug > 0:
                        print("\nUpdating record that was previously selected")
                        print("\nresults: ",results)
                        print("\nresults[0} should be attendID: ",results[0])
                    attendIDresults = results[0]
                    cursor = mariadb_connection.cursor()
                    cursor.execute("UPDATE attendance set timeOUT = NOW() where attendID = '%s'"%(attendIDresults))
                    mariadb_connection.commit()
                    signIn = 0
#            numberRows = cursor.rowcount
#            if numberRows == 1:
#                signIn = 1
#            if debug > 0:
#                print("\nnumberRows = rowcount value: ",numberRows)
#                print("\nSignIn value should match Rowcount value: ",signIn)
                except mariadb.Error as error:
                    print("\nError#2: {}".format(error))
                finally:
                    cursor.close()
        except mariadb.Error as error:
            print("\nError#2: {}".format(error))
        finally:
            cursor.close()
            return{'signIn':signIn}

# scan SAIT Barcode
sait =  input("\n\n\nPlease scan your SAIT ID: ")
if debug > 0:
    print("\nYour SAIT ID: ",sait)

# run valid_user function & return variables to dictionary dict1
dict1 = valid_user(sait, debug)
if debug > 0:
    print("\nAll of dict1 is: ",dict1)
# Assign variables to dictionary values
waiverSign = dict1['waiverSign']
saitID = dict1['saitID']

# if they are a valid user, (waiverSign = 1) run signin_today to check if they have signed in today
# if so, then sign them out *OR* if not, then sign them in today
if waiverSign > 0:
    dict2 = check_signin_today(waiverSign, saitID, debug)
    signIn=dict2['signIn']
    if debug > 0:
        print("\nAll of dict2 is: ",dict2)
        print("\nsaitID = ",saitID)
        print("\nwaiverSign = ",waiverSign)
        print("\nsignIn = ",signIn)


