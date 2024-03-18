#!/usr/bin/env python3


import time
import datetime
import RPi.GPIO as GPIO
import sqlite3
import os

GPIO.setwarnings(False) # Ignore warnings for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1
# Reset counter to one for raingauge count
count = 1

#conn = sqlite3.connect('rainguage.db')
#c = conn.cursor()

def button_callback(channel):
    global count
    conn = sqlite3.connect('raingauge.db')
    c = conn.cursor()
    print("Button was pushed",count)
    count = count + 1
    d = time.strftime("%Y-%m-%d")
    t = time.strftime("%H:%M:%S")
    c.execute("INSERT INTO raincount(currentdate, currenttime) VALUES (?, ?)", (d, t))
#    c.execute("INSERT INTO raincount(currentdate, currenttime) VALUES (date('now'), time('now'))")
    conn.commit()
    time.sleep(0.5)
# Setup event on GPIO 23, Falling Edge
GPIO.add_event_detect(21, GPIO.FALLING, callback=button_callback)
while True:
    time.sleep(0.5)
#GPIO.add_event_detect(21, GPIO.RISING, callback=button_callback)

# raingauge03 has this line, commented out in raingauge04
#message = input("Press enter to quit\n\n") # Run until enter pressed

GPIO.cleanup() # Clean Up


#while True:
#    try:
#    except KeyboardInterrupt:
#        break
