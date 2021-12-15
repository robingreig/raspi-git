#!/usr/bin/python3

import sqlite3
import time
import os

# Establish sqlite3 database connection to 'makerSpace.db'
dbc = sqlite3.connect('makerspace.db')

# To debug program debug > 0
debug = 0

# Short Delay
delay1 = 2
# Long Delay
delay2 = 5

# Did they sign a waiver? waiverSign == 1
waiverSign = 0

while True:
####	 Clear the screen
    if debug == 0:
        os.system('clear')
    waiverSign = 0
    signIn = 0
####	 Scan SAIT Barcode
    sait =  input("\n\n\nPlease scan the SAIT ID: ")
    if debug > 0:
        print("\nThe SAIT ID: ",sait)
        time.sleep(delay1)

#####	Check to see if they are in the users table?
    try:
        cursor = dbc.cursor()
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
        for firstName, lastName in cursor:
            if debug > 0:
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nsignIn value: ",signIn)
                print ("\n", firstName, lastName, "You are in our Database!!\n")
                time.sleep(delay1)
            waiverSign = 1
        if waiverSign == 0:
            print("\nI cannot find this saitID in our list")
            time.sleep(delay1)
        else:
            print("\n", firstName, lastName, "You are ALREADY in our Database!!\n")
            time.sleep(delay1)
    except sqlite3.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()

#####	If they haven't signed in add an entry to the database
    if waiverSign == 0:
        try:
            name1 = input("\n Please enter your first name: ")
            name2 = input("\n Please enter your last name: ")
            phoneNum = input("\n Please enter your phone number: ")
            saitEmail = input("\n Please enter your SAIT email address: ")
            otherEmail = input("\n Please enter your personal email address (optional): ")
            saitSchool = input("\n Please enter the SAIT School (Hospitality, Business, Construction, M&A, Energy, etc): ")
            saitCourse = input("\n Please enter the 3 or 4 letter designation for your SAIT Course (AELP, EET, MET, etc): ")
            cursor = dbc.cursor()

            cursor.execute("INSERT into users (date,  saitID, firstName, lastName, phone, email1, email2, school, program, active, waiver, mentor) VALUES (date('now', 'localtime'),?,?,?,?,?,?,?,?,1,1,0)", (sait, name1, name2, phoneNum, saitEmail, otherEmail, saitSchool, saitCourse))
            dbc.commit()
            print("\n",name1,name2," Thanks for signing IN to the MakerSpace today!")
            time.sleep(delay2)
            waiverSign = 1
            if debug > 0:
                print ("\nDatabase Updated")
                print ("\nThe last inserted ID was: ", cursor.lastrowid)
                time.sleep(delay1)
        except sqlite3.Error as error:
           print("Error: {}".format(error))
           dbc.rollback()
           print("***** Entry was cancelled and going back to the main screen *****")
           time.sleep(delay1)
        finally:
            cursor.close()
dbc.close()

