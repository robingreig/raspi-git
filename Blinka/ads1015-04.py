#!/usr/bin/python3
import board
import busio
import os
import time
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c)
while True:
    chan = AnalogIn(ads, ADS.P3)
    print(chan.value, chan.voltage)
    num = round(chan.voltage,3)
    print(num)
    cht = open("/home/robin/ads1015-1", "w")
    cht.write(str(num))
    cht.close()
    time.sleep(1)
