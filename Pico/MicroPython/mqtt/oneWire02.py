import time
#import network
import machine
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import binascii

# read the value from the DS18B20 from pin 18
ds = DS18X20(OneWire(Pin(16)))
roms = ds.scan()
sensor = (0x28,0xff,0xa1,0x58,0x74,0x16,0x04,0x24)
n = 2
x = '0x'

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
        print('str3[0&1] = ',str3[0:2])
        out = [(str3[i:i+n]) for i in range(0, len(str3), n)]
        print('Type of out = ',(type(out)))
        print('out = ',out)
        result1 = x.join(out)
        print('Type of Result1 = ',(type(result1)))
        print('Result1 = ',result1)
        result2 = (",0x".join(out))
        print('Type of Result2 = ',(type(result2)))
        print('Result2 = ',result2)
        result3 = ('0x'+result2)
        print('Type of Result3 = ',(type(result3)))
        print('Result3 = ',result3)
        result4 = ('('+result3+')')
        print('Type of Result4 = ',(type(result4)))
        print('Result4 = ',result4)
        result5 = eval(result4)
        print('Type of Result5 = ',(type(result5)))
        print('Result5 = ',result5)
        pass
#    temp1 = ds.read_temp(sensor)
    temp1 = ds.read_temp(result5)
    print('sensor temp1 = ',temp1)
    temp1 = "%3.2f" % temp1
    print('Formatted temp1 = ',temp1)
except:
    print('Jumped out of Try loop')
