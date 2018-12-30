#!/usr/bin/python3

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')

curs = mariadb_connection.cursor()

print ("\nEntire Attendance Database\n")

#query = ("SELECT attendID, saitID from attendance where attendID > 65")

#query = ("SELECT attendID, saitID from attendance ORDER BY attendID ASC LIMIT 2")

#query = ("SELECT attendID, saitID from attendance where saitID = '8329' ORDER BY attendID ASC LIMIT 2")

query = ("SELECT * from attendance where saitID = '8329' ORDER BY attendID ASC LIMIT 2")

curs.execute(query)
#for (saitID) in cursor:
#    print("{}, was the 74th".format(saitID))
#cursor.execute(query)
for row in curs:
    print (row)
#    print ("Entry Number: "+str(row[0])+" and saitID: "+str(row[1]))
    print ("Entry Number: "+str(row[0])+" and saitID: "+str(row[1])+" and Date: "+str(row[2])+" and timeIN: "+str(row[3]))

curs.close()

mariadb_connection.close()

