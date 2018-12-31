#!/usr/bin/python3
from tkinter import *

root = Tk()

myContainer01 = Frame(root)
myContainer01.pack()

button1 = Button(myContainer01)
button1["text"] = "Hello, World!"
button1["background"] = "green"
button1.pack()

root.mainloop()

	    
