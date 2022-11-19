import time
import network
import machine
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import binascii

ds = DS18X20(OneWire(Pin(16)))
roms = ds.scan()
sensor = (0x28,0xff,0xa1,0x58,0x74,0x16,0x04,0x24)

while True:
    try:
# convert temp in DS18B20
        ds.convert_temp()
# have to wait at least 750mS after conver
        time.sleep_ms(1000)
# read temp from the sensor
        temp1 = ds.read_temp(sensor)
        print('sensor temp1 = ',temp1)
        time.sleep(2)
# format the value to 2 decimal places
        temp1 = "%3.2f" % temp1
        print('Formatted temp1 = ',temp1)
        time.sleep(2)
# roms is ds.scan()
        for rom in roms:
            print('rom = ',rom)
# convert from bytearray to bytes
            str1 = bytes(rom)
            print('Type of str1 = ',(type(str1)))
            print('str1 = ',str1)
# convert from bytes to hex string
            str2 = binascii.hexlify(rom)
            print('Type of str2 = ',(type(str2)))
            print('str2 = ',str2)
# remove the b'
            str3 = str2.decode()
            print('Type of str3 = ',(type(str3)))
            print('str3 = ',str3)
# Read the temp from the sensor
            temp2 = (ds.read_temp(rom))
            print('temp2 = ',temp2)
            temp2 = "%3.2f" % temp2
            print('Formatted temp2 = ',temp2)
            time.sleep(2)
            pass
    except:
        print('Jumped out of Try loop')
        break
