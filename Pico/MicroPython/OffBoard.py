import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_offboard = machine.Pin(15, machine.Pin.OUT)
led_onboard.value(1)
led_offboard.value(0)
while True:
    led_onboard.toggle()
    led_offboard.toggle()
    utime.sleep(2)