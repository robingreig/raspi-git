#!/usr/bin/python3

from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myParent = master
        self.entry1 = Entry(master)
#        e = Entry(master)
        self.entry1.pack()
#        e.pack()
        self.entry1.focus_set()
#        e.focus_set()

        def callback():
            print (self.entry1.get())
#            print (e.get())
            ID = self.entry1.get()
#            ID = e.get()
            self.entry1.delete(0, END)
#            e.delete(0, END)
            print ("saitID = ",ID)

        self.button1 = Button(self.myParent, text="Input", command=callback)
        self.button1.pack()
        
#        b = Button(master, text="get", width=10, command=callback)
#        b.pack()

root = Tk()
myapp = MyApp(root)
root.mainloop()



