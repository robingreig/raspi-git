#!/usr/bin/python3

import sqlite3

Debug = 1

# ===========================================================================
# Open Database Connection
# ===========================================================================

# Database
dbc = sqlite3.connect('makerSpace.db')
if Debug > 0:
    print ('Opened database successfully')
    print('dbc.total_changes: ',dbc.total_changes)

# ==========================================================================
# Insert into table - variable
# ==========================================================================

# Continuously append data
rows = dbc.execute("SELECT * from attendance").fetchall()
print(rows)

"""
while(True):

  try:

    dbc.execute("INSERT INTO all_temps (date, outside_temp, desk_temp, ceiling_temp, attic_temp, house_temp, office_temp, other_temp)
	VALUES \
	(DATETIME('now', 'localtime'),?,?,?,?,?,?,?)", \
	[(round(read_OutsideTemp(),1)), (round(read_DeskTemp(),1)), (round(read_CeilingTemp(),1)), (round(read_AtticTemp(),1)), \
	(round(read_HouseTemp(),1)), (round(read_OfficeTemp(),1)), (round(read_CarefreeTemp(),1))])

    dbc.commit()
    if Debug > 0:
      print "Wrote a new row to the database"

  except:
    dbc.rollback()
    if Debug > 0:
      print "Failed to write a new row to the database"

  break
"""
dbc.close()
