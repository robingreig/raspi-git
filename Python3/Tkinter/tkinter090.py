#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myParent = master ### Remember master = root
        
        # Our topmost frame is called myContainer1
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()
                    
        #----- constants for controlling layout -----
        button_width = 6
        button_padx = "2m"
        button_pady = "1m"
        
        buttons_frame_padx = "3m"
        buttons_frame_pady = "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        #----- end constants ------
            
        ### We will use VERTICAL (top/bottom) orientation inside myContainer1
        ### Inside myContainer1, first we will create buttons_frame
        ### Then we will create top_frame and bottom_frame
        ### These will be our demonstration frames
        
        # buttons_frame
        self.buttons_frame = Frame(self.myContainer1)
        self.buttons_frame.pack(
            side=TOP,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady
            )
            
        # top_frame
        self.top_frame = Frame(self.myContainer1)
        self.top_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES
            )
        
        # bottom_frame
        self.bottom_frame = Frame(self.myContainer1,
            borderwidth=5, relief=RIDGE,
            height=50,
            background="white"
            )
        self.bottom_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES
            )
        
        ### Now we will put two more frames, left_frame and right_frame
        ### inside top_frame. We will use HORIZONTAL (left/right)
        ### orientation within top_frame
        
        # left_frame
        self.left_frame = Frame(self.top_frame, background="red",
            borderwidth=5, relief=RIDGE,
            height=250,
            width=50
            )
        self.left_frame.pack(side=LEFT,
            fill=BOTH,
            expand=YES
            )
        
        # right_frame
        self.right_frame = Frame(self.top_frame, background="tan",
            borderwidth=5, relief=RIDGE,
            width=250
            )
        self.right_frame.pack(side=RIGHT,
            fill=BOTH,
            expand=YES
            )
            
        # Now we add the buttons to the buttons_frame
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

	    
