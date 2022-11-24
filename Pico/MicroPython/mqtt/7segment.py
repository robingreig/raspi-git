import time
import machine
from machine import Pin

DEBUG = 0

led_wifi_connect = machine.Pin("LED", machine.Pin.OUT, value=0)
led_A = Pin(2, machine.Pin.OUT, value=0)


