#!/usr/bin/python

import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
   if adcnum > 7 or adcnum< 0:
      return -1
   r= spi.xfer2([1, 8 + adcnum << 4, 0])
   adcout = ((r[1] & 3)<< 8) +r [2]
   return adcout

while True:
   value0 = readadc(0)
   print ("Value0: ",value0)
   value1 = readadc(1)
   print ("Value1: ",value1)
   value2 = readadc(2)
   print ("Value2: ",value2)
   value3 = readadc(3)
   print ("Value3: ",value3)
   value4 = readadc(4)
   print ("Value4: ",value4)
   value4 = readadc(5)
   print ("Value4: ",value4)
   value6 = readadc(6)
   print ("Value6: ",value6)
   value7 = readadc(7)
   print ("Value7: ",value7)
#   volts = (value*3.3)/1024
#   print (value)
#   print (volts)
#   print ("%4d/1023 => %5.3f V " %(value, volts))
#   print (-5.8296*(volts)**3+36.327*(volts)**2-74.48*(volts)+56.733)
   time.sleep(2)
