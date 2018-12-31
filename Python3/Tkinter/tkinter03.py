#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button1 = Button(frame, text = "Quit", fg="red", command=frame.quit)
        self.button1.pack(side=LEFT)

root = Tk()

myapp = MyApp(root)

root.mainloop()

	    
