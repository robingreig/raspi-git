#!/usr/bin/python3

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()

solderAllow = 0

sait =  input ("Please scan your SAIT ID")
print("Your SAIT ID: ",sait)

#retrieving information
try:
#    cursor.execute("SELECT firstName from users where solder = 1 and saitID = '%s'"%(sait))
    cursor.execute("SELECT firstName from users where area7 = 1 and saitID = '%s'"%(sait))
except mariadb.Error as error:
    print("Error: {}".format(error))

for firstName in cursor:
    print("{}  You can Solder!".format(firstName))
    print("{}".format(firstName))
    solderAllow = 1
    print("Solder Alllow if found: ",solderAllow)

print("Solder Allow before close: ",solderAllow)
mariadb_connection.close()
