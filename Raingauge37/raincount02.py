#!/usr/bin/env python3


import time
import datetime
import sqlite3
import os


# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1

conn = sqlite3.connect('raingauge.db')
c = conn.cursor()

##### Select total count from yesterday
#t = datetime.date.today()
#print(t)
#c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day')")
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime')")
myresult = c.fetchone()
print("myresult is %s" %myresult)
count = sum(myresult) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/Raincount.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()

##### Select count from midnight > 6am = quad1
#c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day') and currenttime between '00:00:01' and '06:00:00'")
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime') and currenttime between '00:00:01' and '06:00:00'")
quad1 = c.fetchone()
print("quad1 is %s" %quad1)
count = sum(quad1) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/quad1.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()

##### Select count from midnight > 6am = quad2
#c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day') and currenttime between '06:00:01' and '12:00:00'")
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime') and currenttime between '06:00:01' and '12:00:00'")
quad2 = c.fetchone()
print("quad2 is %s" %quad2)
count = sum(quad2) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/quad2.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()

##### Select count from midnight > 6am = quad3
#c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day') and currenttime between '12:00:01' and '18:00:00'")
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime') and currenttime between '12:00:01' and '18:00:00'")
quad3 = c.fetchone()
print("quad3 is %s" %quad3)
count = sum(quad3) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/quad3.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()

##### Select count from midnight > 6am = quad4
#c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime','-1 day') and currenttime between '18:00:01' and '23:59:59'")
c.execute("SELECT COUNT(*) from raincount where currentdate = date('now','localtime') and currenttime between '18:00:01' and '23:59:59'")
quad4 = c.fetchone()
print("quad4 is %s" %quad4)
count = sum(quad4) # convert myresult (tuple) to int
print("count = ",count)
print("Count type is: ",type(count))
cht = open("/home/robin/quad4.txt" , "w") # save count to a file
cht.write(str(count))
cht.close()
