import machine
import utime

led_onboard = machine.Pin("LED", machine.Pin.OUT)
led_offboard = machine.Pin(22, machine.Pin.OUT)

while True:
    led_onboard.value(1)
    led_offboard.value(1)
    utime.sleep(1)
    led_onboard.value(0)
    led_offboard.value(0)
    utime.sleep(1)