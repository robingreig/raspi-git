#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import MySQLdb
import os
import glob
import warnings

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Hostname, User, Password, Database
dbc = MySQLdb.connect(host= "192.168.200.13",
	user= "robin",
	passwd= "Micr0s0ft",
	db= "house_stats")

# Prepare a cursor
cursor = dbc.cursor()

# Filter Warnings
#warnings.filterwarnings('ignore', category=MySQLdb.Warning)


# ==========================================================================
# Insert into table - variable
# ==========================================================================
a = 3.1
b = 4.1
c = 5.1
d = 6.1
e = 7.1

try:
    cursor.execute("""INSERT INTO garage_temp 
        (date, time, outside_temp, desk_temp, ceiling_temp, attic_temp, back_temp) 
	VALUES 
	(NOW(),NOW(),%s,%s,%s,%s,%s);""",
	(a, b, c, d, e))

    dbc.commit()
except:
    dbc.rollback()



dbc.close()
