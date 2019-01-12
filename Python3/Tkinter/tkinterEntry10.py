#!/usr/bin/python3

from tkinter import *
import tkinter.font as font
import mysql.connector as mariadb
import time

# Set Variables
debug = 0
delay1 = 1
delay2 = 2
signIn = 0
seconds = 5
# waiverSign, signed=1, not signed=0
waiverSign = 0

def login(event):
    # set local variables
    waiverSign = 0
    print("Beginning of login loop: "+str(waiverSign))
    #label1.configure(text="Please scan your SAIT ID: ")
    # Set mariadb connection
    connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
    cursor = connection.cursor()
    # Check to see if they are in the users list?
    usr=user.get()
    entry.delete(0,END)
    try:
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(usr))
        for firstName, lastName in cursor:
            # refresh_res1 funcion updates the display (label1) to read Please Scan or Welcome 
            def refresh_res1():
                global seconds
                seconds -=1
                label1.configure(text = "Welcome to the SAIT MakerSpace ""%s"%firstName +" %s"%lastName)
                if seconds > 0:
                    res.after(1000, refresh_res1)
                else:
                    label1.configure(text="Please scan your SAIT ID: ")
                    seconds = 5
                print("Seconds: "+str(seconds))
            res.after(100, refresh_res1)
            waiverSign = 1
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
    print("End of login loop: "+str(waiverSign))
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

#Label(root, text="Please scan your SAIT ID: ").pack()
entry = Entry(root, textvariable=user)
entry.focus_set()
entry.bind("<Return>", login)
entry.pack(pady=10, padx=10)

res = Label(root)
res.pack()

root.mainloop()
