#!/usr/bin/python3

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace')
cursor = mariadb_connection.cursor()

#retrieving information
try:
    cursor.execute("SELECT firstName, lastName from users where firstName= 'Robin'")
except mariadb.Error as error:
    print("Error: {}".format(error))

for firstName, lastName in cursor:
    print("First Name: {} and Last Name: {}" .format(firstName,lastName))

mariadb_connection.close()
