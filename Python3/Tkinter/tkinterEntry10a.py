#!/usr/bin/python3

from tkinter import *
import tkinter.font as font
import mysql.connector as mariadb
import time

# Set Variables
debug = 1
delay1 = 1
delay2 = 2
signIn = 0
seconds = 5
# waiverSign, signed=1, not signed=0
waiverSign = 0

def login(event):
    # set global variables
    global waiverSign, debug, seconds
    if debug > 0:
        print("waiverSign at beginning of login loop: "+str(waiverSign))
        print("debug variable at beginning of login loop: "+str(debug))
    # Set mariadb connection
    connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
    cursor = connection.cursor()
    # Check to see if they are in the users list?
    usr=user.get()
    entry.delete(0,END)
    try:
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(usr))
        for firstName, lastName in cursor:
            # refresh_res1 funcion updates the display (label1) to read Please Scan or Welcome to the MakerSpace
            print("Seconds before the refresh_res1 function definition= "+str(seconds))
            def refresh_res1(seconds):
#                global seconds
                seconds -=1
                label1.configure(text = "Welcome to the SAIT MakerSpace ""%s"%firstName +" %s"%lastName)
                if seconds > 0:
                    label1.after(1000, refresh_res1)
                else:
                    label1.configure(text="Please scan your SAIT ID: ")
                    seconds = 5
                print("Seconds: "+str(seconds))
            label1.after(100, refresh_res1)
            waiverSign = 1
            print("waiverSign inside refresh_res1= "+str(waiverSign))
        if waiverSign == 0:
            # refresh_res2 function updates the display (label1) to read Please Scan or Didn't find you
            def refresh_res2():
                global seconds
                seconds -=1
                label1.configure(text="I cannot find you in our list?    Did you sign the waiver?")
                if seconds > 0:
                    res.after(1000, refresh_res2)
                else:
                    label1.configure(text="Please scan your SAIT ID: ")
                    seconds = 5
                print("Seconds: "+str(seconds))
            res.after(100, refresh_res2)
    except mariadb.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()
    if debug > 0:
        print("waiverSign at end of login loop: "+str(waiverSign))
        print("debug at end of login loop: "+str(debug))
    return waiverSign
    connection.commit()
    connection.close()

root=Tk()
font.nametofont('TkDefaultFont').configure(size=24)
root.title("Login to SAIT MakerSpace"), 
root.geometry('600x300')
user = StringVar()

label1 = Label(root)
label1.configure(text="Please scan your SAIT ID: ")
label1.pack()

entry = Entry(root, textvariable=user)
entry.focus_set()
entry.bind("<Return>", login)
entry.pack(pady=10, padx=10)

root.mainloop()
