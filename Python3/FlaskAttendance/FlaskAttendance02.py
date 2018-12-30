#!/usr/bin/python3

import mysql.connector as mariadb
import time
import os

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')

cursor = mariadb_connection.cursor()
print ("\nEntire Attendance Database\n")
query = ("SELECT firstName, lastName from users where waiver = 1")
cursor.execute(query)
for (firstName, lastName) in cursor:
    print("{}, {} has waiver signed".format(firstName, lastName))

cursor.close()

mariadb_connection.close()

