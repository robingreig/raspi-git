#!/usr/bin/python3
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c)

chan = AnalogIn(ads, ADS.P0)
print(chan.value, chan.voltage)
chan = AnalogIn(ads, ADS.P1)
print(chan.value, chan.voltage)
chan = AnalogIn(ads, ADS.P2)
print(chan.value, chan.voltage)
chan = AnalogIn(ads, ADS.P3)
print(chan.value, chan.voltage)

