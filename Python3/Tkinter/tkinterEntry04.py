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

#        def callback():
#            print (self.entry1.get())
#            print (e.get())
#            ID = self.entry1.get()
#            ID = e.get()
#            self.entry1.delete(0, END)
#            e.delete(0, END)
#            print ("saitID = ",ID)

#        self.button1 = Button(self.myParent, text="Input", command=callback)
        self.button1 = Button(self.myParent, text="Input", command=self.button1Click)
        self.button1.bind("<Return>", self.return1Click)
        self.button1.pack()
        
    def button1Click(self):
        print ("Callback Called by button")
        print (self.entry1.get())
        ID = self.entry1.get()
        self.entry1.delete(0, END)
        print ("saitID: ",ID)
        
    def return1Click(self, event):
        print ("button activated by return")
        self.button1Click()
        
                
#        b = Button(master, text="get", width=10, command=callback)
#        b.pack()

root = Tk()
myapp = MyApp(root)
root.mainloop()



