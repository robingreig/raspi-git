#!/usr/bin/python3

import time
import RPi.GPIO as gpio

while True:
    name = input("What's your ID number?")
    print("Your ID number is: "+ name +"!")
    if name == "000008329":
        print("You are authorized")
        time.sleep(5)
    else:
        print("You are NOT authorized")
        time.sleep(5)
