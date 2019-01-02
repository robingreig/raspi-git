#!/usr/bin/python3

from tkinter import *

class MyApp:
	def __init__(self, myParent):
		self.myContainer1 = Frame(myParent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1["text"]= "Hello, World!"
		self.button1["background"] = "green"
		self.button1.pack()
		
root = Tk()
myapp = MyApp(root)
root.mainloop()

	    
