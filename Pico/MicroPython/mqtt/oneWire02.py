from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import time


ds = DS18X20(OneWire(Pin(16)))
sensor = (0x28,0x04,0x16,0x74,0x58,0xa1,0xff,0x00)
ds.convert_temp()
time.sleep_ms(750)
ds.read_temp(sensor)

#roms = ds.scan()
#count = 10
#while count> 0:
#    ds.convert_temp()
#    time.sleep_ms(750)
#    for rom in roms:
#        print(ds.read_temp(rom))
#        time.sleep(1)
#    count -= 1
