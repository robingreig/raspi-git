#!/usr/bin/python3

from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())
    ID = e.get()
    e.delete(0, END)
    print ("saitID = ",ID)

    
b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()



