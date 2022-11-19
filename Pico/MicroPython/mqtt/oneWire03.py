import time
import machine
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import binascii

ds = DS18X20(OneWire(Pin(16)))
roms = ds.scan()
red = (0x28,0xff,0xa1,0x58,0x74,0x16,0x04,0x24)
sensor = red

try:
    ds.convert_temp()
    time.sleep_ms(1000)
    print('Type of sensor = ',(type(sensor)))
    print('sensor = ',sensor)
    for rom in roms:
        print('rom = ',rom)
        str1 = bytes(rom)
        print('Type of str1 = ',(type(str1)))
        print('str1 = ',str1)
        str2 = binascii.hexlify(rom)
        print('Type of str2 = ',(type(str2)))
        print('str2 = ',str2)
        str3 = str2.decode()
        print('Type of str3 = ',(type(str3)))
        print('str3 = ',str3)
        list1 = [(str3[i:i+2]) for i in range(0, len(str3), 2)]
        print('Type of List1 = ',(type(list1)))
        print('List1 = ',list1)
        result1 = (',0x'.join(list1))
        print('Type of Result1 = ',(type(result1)))
        print('Result1 = ',result1)
        result2 = ('(0x'+result1+')')
        print('Type of Result2 = ',(type(result2)))
        print('Result2 = ',result2)
        result3 = eval(result2)
        print('Type of Result3 = ',(type(result3)))
        print('Result3 = ',result3)
        pass
    temp1 = ds.read_temp(result3)
    print('sensor temp1 = ',temp1)
    temp1 = "%3.2f" % temp1
    print('Formatted temp1 = ',temp1)
except:
    print('Jumped out of Try loop')
