#!/usr/bin/python3
from tkinter import *
import tkinter.filedialog

root = Tk()
root.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Select File"
mainloop()
