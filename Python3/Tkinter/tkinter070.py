#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myParent = master ### Remember master = root
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()
        self.button1.bind("<Button-1>", self.button1Click)
        self.button1.bind("<Return>", self.button1Click)

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Button-1>", self.button2Click)
        self.button2.bind("<Return>", self.button2Click)

        
    def button1Click(self, event):
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
        
    def button2Click(self, event):
        self.myParent.destroy()
            
def report_event(event):
    """Print a description of an event based on its attributes"""
    event_name = {"2": "Keypress", "4": "ButtonPress"}
    print ("Time: "+str(event.time))
    print ("EventType: "+str(event.type), \
        event_name[str(event.type)], \
        "EventWidgetId=" + str(event.widget), \
        "EventKeySymbol=" + str(event.keysym))

root = Tk()

myapp = MyApp(root)

root.mainloop()

	    
