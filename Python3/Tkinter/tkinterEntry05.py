#!/usr/bin/python3

from tkinter import *
import tkinter.font as font

root = Tk()

font.nametofont('TkDefaultFont').configure(size=48)

root.title("tkinterEntry04.py")
root.geometry('400x300')
#root.geometry('600x400')
#root.geometry('1200x1000')

def evaluate(event):
    print(str(entry.get()))
    ID = (str(entry.get()))
#    print(str(eval(entry.get())))
#    ID = (str(eval(entry.get())))
    entry.delete(0,END)
    print ("ID: ",ID)

Label(root, text="Your SAIT ID").pack()
entry = Entry(root)
entry.focus_set()
entry.bind("<Return>", evaluate)
entry.pack(pady=10, padx=10)

root.mainloop()



