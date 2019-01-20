#!/usr/bin/python3
from tkinter import *
#import tkinter.filedialog
from tkinter import filedialog

root = Tk()
root.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(root.filename)
mainloop()
