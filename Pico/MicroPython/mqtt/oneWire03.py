from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import time

#sensor = (0x28,0x04,0x16,0x74,0x58,0xa1,0xff)
#ds = DS18X20(OneWire(machine.Pin(16)))
#ds.convert_temp()
#time.sleep(1)
#ds.read_temp(sensor))

ds = DS18X20(OneWire(Pin(16)))
roms = ds.scan()
while True:
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
#        print(ds.read_temp(rom))
        a = (ds.read_temp(rom))
        print('a = ',a)
        time.sleep(1)
