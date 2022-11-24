import time
from machine import Pin

DEBUG = 0

anode = Pin(15, Pin.OUT, value=1)
led_A = Pin(14, Pin.OUT, value=1)
led_B = Pin(13, Pin.OUT, value=1)
led_C = Pin(12, Pin.OUT, value=1)
led_D = Pin(11, Pin.OUT, value=1)
led_E = Pin(10,Pin.OUT,value=1)
led_F = Pin(9, Pin.OUT, value=1)
led_G = Pin(8, Pin.OUT, value=1)
led_P = Pin(7, Pin.OUT, value=1)

for i in range(4):
    led_A.toggle()
    time.sleep(1)
    led_B.toggle()
    time.sleep(1)
    led_C.toggle()
    time.sleep(1)
    led_D.toggle()
    time.sleep(1)
    led_E.toggle()
    time.sleep(1)
    led_F.toggle()
    time.sleep(1)
    led_G.toggle()
    time.sleep(1)
    led_P.toggle()
    time.sleep(1)


