#!/usr/bin/python3

from tkinter import *

root = Tk()

myContainer1 = Frame(root)
myContainer1.pack()

button1 = Button(myContainer1)
button1["text"]= "Hello, World!"
button1["background"] = "green"
button1.pack()

w = Label(root, text="hello tkinter!")
w.pack()

root.mainloop()

	    
