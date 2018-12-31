#!/usr/bin/python3

from tkinter import *

#import mysql.connector as mariadb

root = Tk()

w = Label(root, text="Hello World!")
w.pack()

root.mainloop()

#mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')

#curs = mariadb_connection.cursor()

#query = ("SELECT * from attendance where saitID = '8329' ORDER BY attendID ASC LIMIT 2")

#curs.execute(query)

#for row in curs:
#    print ("Entry Number: "+str(row[0])+" and saitID: "+str(row[1])+" and Date: "+str(row[2])+" and timeIN: "+str(row[3]))
#    variable1 = str(row[0])
#    print ("Variable1 = "+variable1)
#curs.close()

#mariadb_connection.close()

