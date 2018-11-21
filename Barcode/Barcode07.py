#!/usr/bin/python3
import keyboard
import sys
import time
import RPi.GPIO as gpio
Debug = 0
#time.sleep(4)
list1 = ['Robin Greig', 'Cory Wittich']
list2 = ['000008329', '000008322']
try:
    while True:
        name = input("\033[5;30;47m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    MakerSpace Key Access System, Please scan or input your ID number (including leading zeros) \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[0;37;40m")
        keyboard.press_and_release('enter')
        if Debug > 0:
            print("Your ID number is: "+ name +"!")
            time.sleep(5)
        if name in list2:
            test =(list2.index(name))
            print("\n\n\n\n\033[5;30;42m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                         "+list1[test]+" is authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n          \033[0;37;40m")
            time.sleep(5)
        else:
            print("\n\n\n\n\033[5;30;41m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                           "+name+" is NOT authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       \033[0;37;40m")
            time.sleep(5)
except KeyboardInterrupt:
    sys.exit()
