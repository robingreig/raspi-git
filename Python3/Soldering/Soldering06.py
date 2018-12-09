#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()
# To debug make value > 0
debug = 0
# Which solderStation to turn on
solderStation = 0
# Does the user have authorization to solder (>1)
solderAllow = 0
# Time Sleep Delay 1 for solderStation message
delay1 = 2
# Time Sleep for rejection messages
delay2 = 4

while True:
    # Clear the screen
    os.system('clear')
    # Scan SAIT ID Barcode
    sait =  input ("\n\nPlease scan your SAIT ID: ")
    if debug > 0:
        print("Your SAIT ID: ",sait)

    # Check to see if they can use the soldering stations
    try:
        cursor.execute("SELECT firstName from users where solder = 1 and saitID = '%s'"%(sait))
    except mariadb.Error as error:
        print("Error: {}".format(error))

    for firstName in cursor:
        print ("\n%s"%firstName + " You are authorized to use the Solder Stations\n")
        solderAllow = 1
        time.sleep(delay1)
        if debug > 0:
            print("Solder Alllow if found: ",solderAllow)

    if solderAllow == 0:
        print ("\nYou are not authorized to Solder\n")
        time.sleep(delay2)
        if debug > 0:
            print("Solder Allow before close: ",solderAllow)

    # Scan the barcode of the soldering station
    stationCount = 0
    while solderAllow > 0:
        solderStation = input("Please scan the Barcode on the soldering station: ")
        if debug > 0:
            print("solder variable = ",solderStation)
        if solderStation == str(110000001):
            print("\nSoldering Station 1 will be activated for 30 minutes\n")
            stationCount = 4
            time.sleep(delay1)
        elif solderStation == str(110000002):
            print("\nSoldering Station 2 will be activated for 30 minutes\n")
            stationCount = 4
            time.sleep(delay1)
        elif solderStation == str(110000003):
            print("\nSoldering Station 3 will be activated for 30 minutes\n")
            stationCount = 4
            time.sleep(delay1)
        elif solderStation == str(110000004):
            print("\nSoldering Station 4 will be activated for 30 minutes\n")
            stationCount = 4
            time.sleep(delay1)
        else:
            print("\nI did not read an valid barcode?\n")
            stationCount = stationCount +1
            time.sleep(delay1)
        if stationCount > 3:
            print("\nReturning to main menu\n")
            time.sleep(delay2)
            break

mariadb_connection.close()

