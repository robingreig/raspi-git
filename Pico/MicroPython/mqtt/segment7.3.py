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

def allClear():
    led_A.high()
    led_B.high()
    led_C.high()
    led_D.high()
    led_E.high()
    led_F.high()
    led_G.high()
    led_P.high()


for b in range(10):
# Number 0
    led_A.toggle()
    led_B.toggle()
    led_C.toggle()
    led_D.toggle()
    led_E.toggle()
    led_F.toggle()
    time.sleep(1)
    allClear()
# Number 1
    led_B.low()
    led_C.low()
    time.sleep(1)
    allClear()
# Number 2
    led_A.toggle()
    led_B.toggle()
    led_G.toggle()
    led_E.toggle()
    led_D.toggle()
    time.sleep(1)
    allClear()
# Number 3
    led_A.toggle()
    led_B.toggle()
    led_G.toggle()
    led_C.toggle()
    led_D.toggle()
    time.sleep(1)
    allClear()
# Number 4
    led_F.toggle()
    led_G.toggle()
    led_B.toggle()
    led_C.toggle()
    time.sleep(1)
    allClear()
# Number 5
    led_A.toggle()
    led_F.toggle()
    led_G.toggle()
    led_C.toggle()
    led_D.toggle()
    time.sleep(1)
    allClear()
# Number 6
    led_A.toggle()
    led_F.toggle()
    led_E.toggle()
    led_D.toggle()
    led_C.toggle()
    led_G.toggle()
    time.sleep(1)
    allClear()
# Number 7
    led_A.toggle()
    led_B.toggle()
    led_C.toggle()
    time.sleep(1)
    allClear()
# Number 8
    led_A.toggle()
    led_B.toggle()
    led_C.toggle()
    led_D.toggle()
    led_E.toggle()
    led_F.toggle()
    led_G.toggle()
    time.sleep(1)
    allClear()
# Number 9
    led_A.toggle()
    led_B.toggle()
    led_G.toggle()
    led_C.toggle()
    led_F.toggle()
    time.sleep(1)
    allClear()


