#!/usr/bin/python3

import mysql.connector as mariadb

# Retrieve data from database
def getData():
    mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')
    curs = mariadb_connection.cursor()
    query = ("SELECT * from attendance where saitID = '8329' ORDER BY attendID ASC LIMIT 1")
    curs.execute(query)
    for row in curs:
        var1 = str(row[0])
        print("Var1: "+var1)
        var2 = str(row[1])
        print("Var12: "+var2)
        var3 = str(row[2])
        print("Var3: "+var3)
    curs.close()
    return var1, var2, var3

var1, var2, var3 = getData()
print("Variable1: "+var1)
print("Variable2: "+var2)
print("Variable3: "+var3)
