import machine
import utime
import _thread

# Setup GPIO pins
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN)

# Default value on start
led_red.value(0)
led_amber.value(0)
led_amber.value(0)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
            utime.sleep(0.5)

_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        print("Button Pressed")
        global button_pressed
        button_pressed = False
        print("Button Released")
        utime.sleep(10)
    led_red.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_green.value(1)
    utime.sleep(2)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(2)
    led_amber.value(0)
    
    