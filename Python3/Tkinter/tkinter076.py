#!/usr/bin/python3
from tkinter import *

class MyApp:
    def __init__(self, master):
        self.myLastButtonInvoked = None
            
        self.myParent = master ### Remember master = root
        self.myContainer1 = Frame(master)
        self.myContainer1.pack()

        self.yellowButton = Button(self.myContainer1, command=self.yellowButtonClick)
        self.yellowButton.configure(text="YELLOW", background="yellow")
        self.yellowButton.pack(side=LEFT)
        self.yellowButton.focus_force()

        self.greenButton = Button(self.myContainer1, command=self.greenButtonClick)
        self.greenButton.configure(text="GREEN", background="green")
        self.greenButton.pack(side=LEFT)
        self.greenButton.focus_force()

        self.quitButton = Button(self.myContainer1, command=self.quitButtonClick)
        self.quitButton.bind("<Return>", self.quitButtonClick_a)
        self.quitButton.configure(text="Cancel", background="red")
        self.quitButton.pack(side=RIGHT)

        
    def yellowButtonClick(self):
        print ("Yellow button clicked. Previous button was: ", self.myLastButtonInvoked)
        self.myLastButtonInvoked = "YELLOW"
        
    def greenButtonClick(self):
        print("Green button clicked. Previous button was: ", self.myLastButtonInvoked)
        self.myLastButtonInvoked = "GREEN"

    def quitButtonClick(self):
        print("Quit Button Selected via Mouse")
        self.myParent.destroy()

    def quitButtonClick_a(self, event):
        print("Quit Button Selected via Return")
        self.quitButtonClick()

print ("\n"*100) # A simple way to clear the screen
print ("Starting....")            
root = Tk()
myapp = MyApp(root)
root.mainloop()
print ("....Done!")

	    
