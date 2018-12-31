#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myParent = master ### Remember master = root
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1, command=self.button1Click)
        self.button1.bind("<Return>", self.button1Click_a)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()

        self.button2 = Button(self.myContainer1, command=self.button2Click)
        self.button2.bind("<Return>", self.button2Click_a)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=RIGHT)

        
    def button1Click(self):
        print ("button1Click Event Handler")
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
        
    def button2Click(self):
        print("button2Click Event Handler")
        self.myParent.destroy()

    def button1Click_a(self, event):
        print("button1Click_a Event Handler(a wrapper)")
        self.button1Click()

    def button2Click_a(self, event):
        print("button2Click_a Event Handler (a wrapper)")
        self.button2Click()

            
root = Tk()
myapp = MyApp(root)
root.mainloop()

	    
