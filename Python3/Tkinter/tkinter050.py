#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello World!"
        self.button1["background"] = "green"
        self.button1.pack(side=LEFT)

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Off to join the circuis")
        self.button2.configure(background="tan")
        self.button2.pack(side=LEFT)
        
        self.button3 = Button(self.myContainer1)
        self.button3.configure(text="Join Me?", background="cyan")
        self.button3.pack(side=LEFT)
        
        self.button4 = Button(self.myContainer1, text="Goodbye!", background="red")
        self.button4.pack(side=LEFT)
        
root = Tk()

myapp = MyApp(root)

root.mainloop()

	    
