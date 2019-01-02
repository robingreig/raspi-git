#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        #========================= Button 01 ======================================
        button_name = "OK"
        
        # command binding
        self.button1 = Button(self.myContainer1,
            command= lambda
            arg1=button_name, arg2=1, arg3="Good Stuff" :
            self.buttonHandler(arg1, arg2, arg3)
            )
            
        # event binding
        self.button1.bind("<Return>",
            lambda
            event, arg1=button_name, arg2=1, arg3="Good Stuff!":
            self.buttonHandler_a(event, arg1, arg2, arg3)
            )
        self.button1.configure(text=button_name, background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()  # Put keyboard focus on button1

        #===============================Button 02 ============================
        button_name = "Cancel"

        # command binding
        self.button2 = Button(self.myContainer1,
            command= lambda
            arg1=button_name, arg2=2, arg3="Bad Stuff":
            self.buttonHandler(arg1, arg2, arg3)
            )

        # event binding
        self.button2.bind("<Return>",
            lambda
            event, arg1=button_name, arg2=2, arg3="Bad stuff!" :
            self.buttonHandler(arg1, arg2, arg3)
            )
            
        self.button2.configure(text=button_name, background="red")
        self.button2.pack(side=LEFT)

    def buttonHandler(self, arg1, arg2, arg3):
        print ("    buttonHandler routine received arguments:", arg1.ljust(8), arg2, arg3)

    def buttonHandler_a(self, event, arg1, arg2, arg3):
        print ("buttonHandler_a received event", event)
        self.buttonHandler(arg1, arg2, arg3)

print ("\n"*100) # clear the screen
print ("Starting program tt077.")
root = Tk()
myapp = MyApp(root)
print ("Ready to start executing the event loop.")
root.mainloop()
