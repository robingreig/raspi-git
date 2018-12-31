#!/usr/bin/python3

from tkinter import *

class App:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		
		self.button = Button(
			frame, text="Quit", fg="red", command=frame.quit
			)
		self.button.pack(side=LEFT)
		
		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)
		
		def say_hi(self):
			print ("Hi There Everyone!")
root = Tk()

app = App(root)

root.mainloop()

root.destroy()
	
		





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

