#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()
# To debug program debug > 0
debug = 1
# Time Delay for authorized messages
delay1 = 3
# Time Delay for rejection messages
delay2 = 5
# Did they sign a waiver > 0?
waiverSign = 0

while True:
    # Clear the screen
    os.system('clear')
    waiverSign = 0
    # Scan SAIT Barcode
    sait =  input ("\n\n\nPlease scan your SAIT ID: ")
    if debug > 0:
        print("Your SAIT ID: ",sait)

    #retrieving information
    try:
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(sait))
    except mariadb.Error as error:
        print("Error: {}".format(error))

    for firstName, lastName in cursor:
            print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
            time.sleep(delay1)
            waiverSign = 1
    if waiverSign == 0:
        print("\nI cannot find you in our list? Did you sign the waiver?")
        time.sleep(delay2)
    if waiverSign > 0:
        try:
            if debug > 0:
                print("Your SAIT ID: ",sait)
                time.sleep(delay1)
            cursor.execute("""INSERT into attendance
               (date, timeIN,userID)
               VALUES
               (NOW(),NOW(),'%s');""" % (sait))
        except mariadb.Error as error:
            print("Error: {}".format(error))

        mariadb_connection.commit()
        if debug > 0:
            print ("Database Updated")
            print ("The last inserted ID was: ", cursor.lastrowid)
            time.sleep(delay1)

mariadb_connection.close()

