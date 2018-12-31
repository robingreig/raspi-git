#!/usr/bin/python3

from tkinter import *

class MyApp:
    def __init__(self, root, use_geometry, show_buttons):
        fm = Frame(root, width=300, height=200, bg="blue")
        fm.pack(side=TOP, expand=NO, fill=NONE)
        
        if use_geometry:
            root.geometry("600x400")
        
        if show_buttons:
            Button(fm, text="Button 1", width=10).pack(side=LEFT)
            Button(fm, text="Button 2", width=10).pack(side=LEFT)
            Button(fm, text="Button 3", width=10).pack(side=LEFT)

case = 0
for use_geometry in (0,1):
    for show_buttons in (0,1):
        case = case +1
        root = Tk()
        root.wm_title("Case " + str(case))
        display = MyApp(root, use_geometry, show_buttons)
        root.mainloop()
        
