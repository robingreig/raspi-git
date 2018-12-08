#!/usr/bin/python3

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()

debug = 0
solderAllow = 0

sait =  input ("Please scan your SAIT ID")
if debug > 0:
    print("Your SAIT ID: ",sait)

#retrieving information
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

if solderAllow == 0:
    print ("You are not authorized to Solder")
    if debug > 0:
        print("Solder Allow before close: ",solderAllow)

mariadb_connection.close()
