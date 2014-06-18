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
dbc = MySQLdb.connect(host= "localhost",
	user= "robin",
	passwd= "raspberry",
	db= "dms_stats")

# Prepare a cursor
cursor = dbc.cursor()

# ===========================================================================
# Insert into table
# ===========================================================================
warnings.filterwarnings('ignore', category=MySQLdb.Warning)

try:
    cursor.execute("""INSERT INTO dms_temp (date, time, dms_temp, E119_temp) VALUES (NOW(),NOW(),'18.5','19.5');""")

    dbc.commit()
except:
    dbc.rollback()


# ==========================================================================
# Show Table
# ==========================================================================

#cursor.execute("""SELECT * from garage_temp;""")
#print cursor.fetchall()

dbc.close()
