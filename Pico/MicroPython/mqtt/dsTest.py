import time
import machine
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from secrets_home import secrets
import binascii

# read the value from the DS18B20 connected to pin 16
ds = DS18X20(OneWire(Pin(16)))

# scan if more than 1 DS18B20
roms = ds.scan()
DEBUG = 0

try:
# Convert temp in DS18B20
    ds.convert_temp()
# need at least 750mS after convert before you can read
    time.sleep_ms(1000)
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
        print('\n\n***This is the hex value for this sensor***\n\n',result2,'\n\n')
# convert from string to tuple
        result3 = eval(result2)
        pass
    temp1 = ds.read_temp(result3)
    print('sensor temp1 = ',temp1)
    temp1 = "%3.2f" % temp1
    print('Formatted Temp1 = ',temp1,'\n')
except:
    print('SOMETHING WRONG? Jumped out of Try loop')
