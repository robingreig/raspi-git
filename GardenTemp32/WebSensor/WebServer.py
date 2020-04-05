#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDhtWebServer.py
#  
#  Created by MJRoBot.org 
#  10Jan18

'''
	RPi Web Server for Dallas captured data  
'''

from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

# Retrieve data from database
def getData():
	conn=sqlite3.connect('/home/robin/gardentemp.db')
	curs=conn.cursor()

	for row in curs.execute("SELECT * FROM coldframe ORDER BY currentime DESC LIMIT 1"):
		time = str(row[4])
		temp1 = str(row[1])
		temp2 = str(row[2])
	conn.close()
	return time, temp1, temp2

# main route 
@app.route("/")
def index():
	
	time, temp1, temp2 = getData()
	templateData = {
	  'time'	: time,
      'temp1'	: temp1,
      'temp2'		: temp2
	}
	return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)

