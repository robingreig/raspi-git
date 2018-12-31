#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
            
        #----- constants for controlling layout -----
        button_width = 6
        button_padx = "2m"
        button_pady = "1m"
        
        buttons_frame_padx = "3m"
        buttons_frame_pady = "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        #----- end constants ------
            
        self.myParent = master ### Remember master = root
        self.buttons_frame = Frame(master)
        
        self.buttons_frame.pack(
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady
            )

        self.button1 = Button(self.buttons_frame, command=self.button1Click)
        self.button1.configure(text="OK", background="green")
        self.button1.focus_force()
        self.button1.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
            )
        self.button1.pack(side=LEFT)
        self.button1.bind("<Return>", self.button1Click_a)
        
        self.button2 = Button(self.buttons_frame, command=self.button2Click)
        self.button2.configure(text="CANCEL", background="red")
        self.button2.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
            )
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Return>", self.button2Click_a)
        
    def button1Click(self):
        print ("button1Click Event Handler")
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
        
    def button2Click(self):
        print ("button2Click Event Handler")
        self.myParent.destroy()

    def button1Click_a(self, event):
        print ("button1Click_a Event Handler Wrapper")
        self.button1Click()

    def button2Click_a(self, event):
        print("button2Click_a Event Handler Wrapper")
        self.button2Click()

print ("\n"*100) # A simple way to clear the screen
print ("Starting....")            
root = Tk()
myapp = MyApp(root)
root.mainloop()
print ("....Done!")

	    
