#!/usr/bin/python3

from tkinter import *

def login():
    usr=user.get()
    pas=password.get()
    connection = pymysql.connect(host='localhost', user='root', password='', db='login')
    cursor = connection.cursor()
    q=("select username from user where username=%s")


    q1 = ("select pass from user where pass=%s")
    if cursor.execute(q,usr) and cursor.execute(q1, pas):
        postlogin()
    else:
        print("Try again")

    connection.commit()
    connection.close()
root=Tk()
user=StringVar()
password=StringVar()
sec=StringVar()
name=StringVar()
regno=StringVar()
att=StringVar()
tp=Frame(root,width=800,height=600)
tp.pack()
l1=Label(tp,text="Username")
l1.grid(row=0,column=0)
e1=Entry(tp,textvariable=user).grid(row=0,column=1,columnspan=4)

l2=Label(tp,text="Password")
l2.grid(row=1,column=0)
e2=Entry(tp,textvariable=password).grid(row=1,column=1,columnspan=4)

submit=Button(tp,text="Login",command=login).grid(row=2,column=2)

root.mainloop()
