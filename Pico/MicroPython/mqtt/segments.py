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

def zero():
    led_A.low()
    led_B.low()
    led_C.low()
    led_D.low()
    led_E.low()
    led_F.low()

def one():
    led_B.low()
    led_C.low()

def two():
    led_A.low()
    led_B.low()
    led_G.low()
    led_E.low()
    led_D.low()

def three():
    led_A.low()
    led_B.low()
    led_G.low()
    led_C.low()
    led_D.low()

def four():
    led_F.low()
    led_G.low()
    led_B.low()
    led_C.low()

def five():
    led_A.low()
    led_F.low()
    led_G.low()
    led_C.low()
    led_D.low()

def six():
    led_A.low()
    led_F.low()
    led_E.low()
    led_D.low()
    led_C.low()
    led_G.low()

def seven():
    led_A.low()
    led_B.low()
    led_C.low()

def eight():
    led_A.low()
    led_B.low()
    led_C.low()
    led_D.low()
    led_E.low()
    led_F.low()
    led_G.low()

def nine():
    led_A.low()
    led_B.low()
    led_G.low()
    led_C.low()
    led_F.low()


