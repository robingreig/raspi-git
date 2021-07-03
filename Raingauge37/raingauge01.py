#!/usr/bin/env python3

from time import sleep
import datetime
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False) # Ignore warnings for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0
def button_callback(channel):
    global count
    print("Button was pushed",count)
    count = count + 1

# Setup event on GPIO 23, Falling Edge
GPIO.add_event_detect(21, GPIO.FALLING, callback=button_callback)
#GPIO.add_event_detect(21, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n") # Run until enter pressed

GPIO.cleanup() # Clean Up

# Debug = 0 to stop test messages, Debug = 1 to print
Debug = 1

#while True:
#    try:
#        if GPIO.input(23) == GPIO.HIGH
#            print("Button was pushed")

#        button.wait_for_release()
#        if Debug > 0:
#            print("Door Opened!")
#        os.system("/home/robin/raspi-git/Python3/SMTP/Garage34Door.py")
#        for i in range(Num_Pics):
#            now = datetime.datetime.now()
#            camera.capture('/home/robin/Pictures/image,%s.jpg' % now)
#        for j in range(60):
#            if button.is_pressed:
#                if Debug > 0:
#                    print("Door is closed")
#                break
#            if Debug > 0:
#                print("Waiting for door to close: %s" %j)
#            sleep(Picture_Cycle)
#    except KeyboardInterrupt:
#        break
