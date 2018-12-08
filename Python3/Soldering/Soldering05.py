#!/usr/bin/python3

import mysql.connector as mariadb
import time

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()

debug = 1
solderStation = 0
solderAllow = 0

while True:
    # Scan SAIT ID Barcode
    sait =  input ("Please scan your SAIT ID")
    if debug > 0:
        print("Your SAIT ID: ",sait)

    # Check to see if they can use the soldering stations
    try:
        cursor.execute("SELECT firstName from users where solder = 1 and saitID = '%s'"%(sait))
    #    cursor.execute("SELECT firstName from users where area7 = 1 and saitID = '%s'"%(sait))
    except mariadb.Error as error:
        print("Error: {}".format(error))

    for firstName in cursor:
        print ("%s"%firstName + " You can Solder")
        solderAllow = 1
        if debug > 0:
            print("Solder Alllow if found: ",solderAllow)

    # Scan the barcode of the soldering station
    solderStation = input("Please scan the Barcode on the soldering station: ")
    if debug > 0:
        print("solder variable = ",solderStation)
    if solderStation == str(110000001):
        print("Soldering Station 1 will be activated for 30 minutes")
        time.sleep(5)
    elif solderStation == str(110000002):
        print("Soldering Station 2 will be activated for 30 minutes")
        time.sleep(5)
    elif solderStation == str(110000003):
        print("Soldering Station 3 will be activated for 30 minutes")
        time.sleep(5)
    elif solderStation == str(110000004):
        print("Soldering Station 4 will be activated for 30 minutes")
        time.sleep(5)
    else:
        print("Could not read the barcode")
        time.sleep(5)

    if solderAllow == 0:
        print ("You are not authorized to Solder")
        time.sleep(5)
        if debug > 0:
            print("Solder Allow before close: ",solderAllow)

mariadb_connection.close()

