#!/usr/bin/python3

import mysql.connector as mariadb

from flask import Flask, render_template, request
app = Flask(__name__)

# Retrieve data from database
def getData():
    mariadb_connection = mariadb.connect(user='robin', password='Micr0s0ft', database='makerspace', host='localhost')
    curs = mariadb_connection.cursor()
    query = ("SELECT * from attendance where saitID = '8329' ORDER BY attendID ASC LIMIT 1")
    curs.execute(query)
    for row in curs:
        attendID = str(row[0])
        saitID = str(row[1])
        dateID = str(row[2])
    curs.close()
    return attendID, saitID, dateID

# Main Route
@app.route('/')
def index():
    attendID, saitID, dateID = getData()
    templateData = {
        'Where': attendID,
        'Who': saitID,
        'When': dateID
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
