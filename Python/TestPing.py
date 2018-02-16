#! /usr/bin/python3

import subprocess
import os
DEBUG = 0

ip = ['breadboard10.local', 'aprx11.local', 'battmon12.local', 'adafruitaio14.local', 'raspi15.local', 'blockheat16.local', 'raspi20.local','raspi24.local' ]

for index in range(len(ip)):
  if DEBUG > 0:
    print('Current ip :', ip[index])
  
  status,result = subprocess.getstatusoutput("ping -c1 -w2  " + ip[index])

  if status == 0:
      print ("\nSystem " + ip[index] + " is UP!")
  else:
      print ("\nSystem " + ip[index] + " is DOWN?")


