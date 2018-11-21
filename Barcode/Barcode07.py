#!/usr/bin/python3
import sys
import time
import RPi.GPIO as gpio
Debug = 0
#time.sleep(4)
list1 = ['000008329','Robin Greig','000008322','Cory Wittich','000747019','Ethan McNeill','000734719','Chit Tun','000684050','Nicholas Panos','000666984','Connor Goodfellow','000454716','Jordan Persson','000797716','Kyle Lam','000726298','Christopher Wilson','000808791','Trevor Praud','000364585','Viero Di Gregorio','000608299','George Ager','000625348','Bryce Shirley','000785068','Junyeob Suk','000785923','Arran Woodruff','000612786','Kevin Sieswerda','000790888','Mihir Pankhania','000062194','Chris Chung']
try:
    while True:
        name = input("\033[5;30;47m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    MakerSpace Key Access System, Please scan or input your ID number (including leading zeros) \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[0;37;40m")
        if Debug > 0:
            print("Your ID number is: "+ name +"!")
            time.sleep(5)
        if name in list1:
            test1 =(list1.index(name))
            test2 = test1 + 1
            print("\n\n\n\n\033[5;30;42m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                         "+list1[test2]+" is authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n          \033[0;37;40m")
            time.sleep(5)
        else:
            print("\n\n\n\n\033[5;30;41m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                           "+name+" is NOT authorized to sign out the key \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       \033[0;37;40m")
            time.sleep(5)
except KeyboardInterrupt:
    sys.exit()
