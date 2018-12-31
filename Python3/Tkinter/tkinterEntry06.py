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



def login(event):
    # Set mariadb connection
    connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
    cursor = connection.cursor()

    #	Check to see if they in the users list?
    usr=user.get()
    entry.delete(0,END)
    try:
        cursor.execute("SELECT firstName, lastName from users where waiver = 1 and saitID = '%s'"%(usr))
        for firstName, lastName in cursor:

            if debug > 0:
                print ("\nWelcome to the MakerSpace ""%s"%firstName + " %s"%lastName+"!")
                print("\nRowcount returned from checking if they are in the system: ", cursor.rowcount)
                print("\nsignIn value: ",signIn)
                time.sleep(delay1)
            waiverSign = 1
        if waiverSign == 0:
            print("\nI cannot find you in our list?    Did you sign the waiver?")
            time.sleep(delay2)
    except mariadb.Error as error:
        print("\nError#1: {}".format(error))
    finally:
        cursor.close()

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
entry.bind("<Return>", login)
entry.pack(pady=10, padx=10)

root.mainloop()
