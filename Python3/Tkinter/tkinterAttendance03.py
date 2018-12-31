#!/usr/bin/python3
from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
	
		





#import mysql.connector as mariadb

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

