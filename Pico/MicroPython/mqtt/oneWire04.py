import time
import machine
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from secrets_home import secrets
import binascii

DEBUG = 0

# read the value from the DS18B20 connected to pin 16
ds = DS18X20(OneWire(Pin(16)))

# scan if more than 1 DS18B20
roms = ds.scan()

#red = (0x28,0xff,0xa1,0x58,0x74,0x16,0x04,0x24)
sensor = secrets['oldRed']

try:
# Convert temp in DS18B20
    ds.convert_temp()
# need at least 750mS after convert before you can read
    time.sleep_ms(1000)
# convert sensor variable from string to tuple
    sensor = (eval(sensor))
    if DEBUG > 0:
        print('Type of sensor = ',(type(sensor)))
        print('sensor = ',sensor)
    for rom in roms:
        if DEBUG > 0:
            print('rom = ',rom)
# convert from bytearray to bytes
        str1 = bytes(rom)
        if DEBUG > 0:
            print('Type of str1 = ',(type(str1)))
            print('str1 = ',str1)
# convert from bytes to hex string
        str2 = binascii.hexlify(rom)
        if DEBUG > 0:
            print('Type of str2 = ',(type(str2)))
            print('str2 = ',str2)
# remove the b' from the string
        str3 = str2.decode()
        if DEBUG > 0:
            print('Type of str3 = ',(type(str3)))
            print('str3 = ',str3)
# break the string into segments of 2
        list1 = [(str3[i:i+2]) for i in range(0, len(str3), 2)]
        if DEBUG > 0:
            print('Type of List1 = ',(type(list1)))
            print('List1 = ',list1)
# add 0x between each segment
        result1 = (',0x'.join(list1))
        if DEBUG > 0:
            print('Type of Result1 = ',(type(result1)))
            print('Result1 = ',result1)
# put brackets around all and add first 0x
        result2 = ('(0x'+result1+')')
        if DEBUG > 0:
            print('Type of Result2 = ',(type(result2)))
            print('Result2 = ',result2)
# convert from string to tuple
        result3 = eval(result2)
        if DEBUG > 0:
            print('Type of Result3 = ',(type(result3)))
            print('Result3 = ',result3)
        pass
    temp1 = ds.read_temp(result3)
    print('\nsensor temp1 = ',temp1)
    temp1 = "%3.2f" % temp1
    print('Formatted Temp1 = ',temp1,'\n')
    temp2 = ds.read_temp(sensor)
    print('Secret sensor temp = ',temp2)
    temp2 = "%3.2f" % temp2
    print('Formatted Secret sensor temp = ',temp2)
except:
    print('Jumped out of Try loop')
