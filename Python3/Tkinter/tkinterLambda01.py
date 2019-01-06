#!/usr/bin/python3
from tkinter import *

root = Tk()

myContainer01 = Frame(root)
myContainer01.pack()

def callback(number):
	print ("Button: ", number)
	
button1 = Button(myContainer01, text="1", command=lambda: callback(1)).pack(side=LEFT)
button2 = Button(myContainer01, text="2", command=lambda: callback(2)).pack(side=LEFT)
button1 = Button(myContainer01, text="3", command=lambda: callback(3)).pack(side=LEFT)

root.mainloop()

	    
