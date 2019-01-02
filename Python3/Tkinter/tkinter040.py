#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello World!"
        self.button1["background"] = "green"
        self.button1.pack()

        self.button2 = Button(self.myContainer1)
        self.button1.configure(text="Off to circus!")
        self.button2.configure(background="tan")
        self.button2.pack()

        self.button3 = Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")
        self.button3.pack()

        self.button4 = Button(self.myContainer1, text="Goodbye!", background="red")
        self.button4.pack()

root = Tk()

myapp = MyApp(root)

root.mainloop()

	    
