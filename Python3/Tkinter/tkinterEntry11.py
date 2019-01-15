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

def inNotOut(signIn):
    # Have they signed in earlier today, but not signed out? numberRows will indicate number of times
    try:
        connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
        cursor = connection.cursor()
        cursor.execute("SELECT * from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
        results = cursor.fetchone()
    except mariadb.Error as error:
        print("\nError#2: {}".format(error))
    finally:
        numberRows = cursor.rowcount
        if numberRows == 1:
            signIn = 1
        #if debug > 0:
        print("\nRowcount returned from checking entries today: ", numberRows, "\n")
        print("\nIf number of rows < 1, SignIn value should be 0 > ",signIn,"\n")
        print("\nFirst Name: ",firstName)
        print("\nLast Name: ",lastName)
        time.sleep(delay2)
        while results is not None:
            print("\nResults: ",results)
            results = cursor.fetchone()
            time.sleep(delay2)

        cursor.close()
        connection.close()
        print("\nsignIn from within inNotOut funtion = ",signIn)
        return signIn

def login(event):
    # set local variables
    waiverSign = 0
    if debug > 0:
        print("Beginning of login loop waiverSign= "+str(waiverSign))
        print("Beginning of login loop signIn= "+str(signIn))
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
            cursor.close()
            inNotOut(signIn)
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
        print("End of login loop waiverSign= "+str(waiverSign))
        print("End of login loop signIn= "+str(signIn))
    connection.commit()
    connection.close()

# Add check out timeOUT to last entry for user
if waiverSign > 0 and signIn == 1:
# Select the record that has the timeIN entry
    try:
        connection = mariadb.connect(host='localhost', user='robin', password='Micr0s0ft', database='makerspace')
        cursor = connection.cursor()
        if debug > 0:
            print("\nSelect the record with the timeIN entry")
        cursor.execute("SELECT attendID from attendance where timeOUT IS NULL and date = curdate() and saitID = '%s'"%(sait))
        results = cursor.fetchone()
        numberRows = cursor.rowcount
        if debug > 0:
            print("\nRowcount from Select the record with the timeIN entry: ", numberRows, "\n")
            time.sleep(delay1)
            if results is not None:
                print("\nEntry number found: ",results,"\n")
                time.sleep(delay1)
    except mariadb.Error as error:
        print("\nError#2: {}".format(error))
    finally:
        cursor.close()

# Update the record that was selected previously
    try:
        cursor = mariadb_connection.cursor()
        if debug > 0:
            print("\nUpdate the record that was previously selected")
        cursor.execute("UPDATE attendance set timeOUT = NOW() where attendID = '%s'"%(results))
        mariadb_connection.commit()
        print("\n",firstName,lastName," Thanks for signing OUT of the MakerSpace today!")
        time.sleep(delay2)
        signIn = 0
        if debug > 0:
            print ("\nDatabase Updated")
            print ("\nThe last inserted ID was: ", cursor.lastrowid)
            print ("\nSignIn value: ",signIn)
            time.sleep(delay1)
    except mariadb.Error as error:
        print("\nError#2: {}".format(error))
        mariadb_connection.rollback()
    finally:
        cursor.close()
        signIn = 2

#	If they haven't signed in today, then add an entry to the database timeIN
if waiverSign == 1 and signIn == 0:
    try:
        if debug > 0:
            print("\nYour SAIT ID: ",sait)
            time.sleep(delay1)
        cursor = mariadb_connection.cursor()
        cursor.execute("""INSERT into attendance
           (date, timeIN, saitID)
           VALUES
           (NOW(),NOW(),'%s');""" % (sait))
        mariadb_connection.commit()
        print("\n",firstName,lastName," Thanks for signing IN to the MakerSpace today!")
        time.sleep(delay2)
        if debug > 0:
            print ("\nDatabase Updated")
            print ("\nThe last inserted ID was: ", cursor.lastrowid)
            time.sleep(delay1)
    except mariadb.Error as error:
       print("Error: {}".format(error))
       mariadb_connection.rollback()
    finally:
        cursor.close()
        connection.close()
#mariadb_connection.close()


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
