#!/usr/bin/python3

import sqlite3

def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

con = sqlite3.connect('/home/robin/makerspace.db')
bck = sqlite3.connect('/home/robin/makerspace_backup.`date +%F`.db')
with bck:
    con.backup(bck, pages=3, progress=progress)
bck.close()
con.close()
