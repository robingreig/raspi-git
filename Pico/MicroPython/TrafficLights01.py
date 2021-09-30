import machine
import utime

# Setup output pins
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

# Default value on start
led_red.value(0)
led_amber.value(0)
led_amber.value(0)

while True:
    led_red.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_green.value(1)
    utime.sleep(2)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(2)
    led_amber.value(0)
    
    