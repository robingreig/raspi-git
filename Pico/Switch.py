import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_offboard = machine.Pin(15, machine.Pin.OUT)
switch = machine.Pin(14, machine.Pin.IN)
led_onboard.value(0)
led_offboard.value(1)
while True:
    if switch.value() == 1:
        led_onboard.value(1)
        utime.sleep(3)
        led_onboard.value(0)
    led_offboard.toggle()
    utime.sleep(5)