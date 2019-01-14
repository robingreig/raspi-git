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
seconds = 6
# waiverSign, signed=1, not signed=0
waiverSign = 0

def login(event):
    # set local variables
    waiverSign = 0
    print("Beginning of login loop: "+str(waiverSign))
    # Set mariadb connection
    connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
    cursor = connection.cursor()
    #	Check to see if they are in the users list?
    usr=user.get()
    entry.delete(0,END)
    try:
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(usr))
        for firstName, lastName in cursor:
            def refresh_res1():
                global seconds
                seconds -=1
                res.configure(text = "Welcome to the SAIT MakerSpace ""%s"%firstName +" %s"%lastName)
                if seconds < 3:
                    res.configure(text=())
                if seconds > 2:
                    res.after(1000, refresh_res1)
                else:
                    seconds = 6
                print("Seconds: "+str(seconds))
            res.after(1000, refresh_res1)
            if debug > 0:
                print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nsignIn value: ",signIn)
                time.sleep(delay1)
            waiverSign = 1
        if waiverSign == 0:
            def refresh_res2():
                global seconds
                seconds -=1
                res.configure(text="\nI cannot find you in our list?    Did you sign the waiver?")
                if seconds < 3:
                    res.configure(text=())
                if seconds > 2:
                    res.after(1000, refresh_res2)
                else:
                    seconds = 6
                print("Seconds: "+str(seconds))
            res.after(1000, refresh_res2)
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

Label(root, text="Please scan your SAIT ID: ").pack()
entry = Entry(root, textvariable=user)
entry.focus_set()
print("WaiverSign before entry.bind: "+str(waiverSign))
entry.bind("<Return>", login)
print("WaiverSign after entry.bind: "+str(waiverSign))
entry.pack(pady=10, padx=10)

res = Label(root)
res.pack()

root.mainloop()
