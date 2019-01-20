#!/usr/bin/python3
from tkinter import *

win = Tk()
Block = IntVar()

def Block_to_file():
    contents = str(Block.get())
    with open("tkin.txt", 'w') as f:
        f.write(contents)

Entry(win, width=15, textvariable=Block).grid(column=0, row=0, sticky=(N, W, E))
Button(win, text='Write to file', command=Block_to_file).grid(column=0, row=1, sticky=(W, E))

mainloop()
