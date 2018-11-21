#!/usr/bin/python3
import sys
import time
import RPi.GPIO as gpio
Debug = 0
time.sleep(4)
try:
    while True:
        name = input("\033[5;30;47m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    MakerSpace Key Access System, Please scan or input your ID number (including leading zeros) \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[0;37;40m")
        if Debug > 0:
            print("Your ID number is: "+ name +"!")
            time.sleep(5)
        if name == "000008329":
            print("\n\n\n\n\033[5;30;42m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                          Robin Greig is authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n          \033[0;37;40m")
            time.sleep(5)
        else:
            print("\n\n\n\n\033[5;30;41m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                           "+name+" is NOT authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       \033[0;37;40m")
            time.sleep(5)
except KeyboardInterrupt:
    sys.exit()
