#!/usr/bin/env python3


import time
import datetime
import sqlite3
import os


# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1

conn = sqlite3.connect('raingauge.db')
c = conn.cursor()

#t = datetime.date.today()
#print(t)
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day')")
#c.execute("SELECT COUNT(*) from raincount where currentdate = %s" %(t))
#c.execute("SELECT COUNT(*) from raincount where currentdate = '2021-08-19'")
myresult = c.fetchone()
print("myresult is %s" %myresult)
count = sum(myresult) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/Raincount.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()
