import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
print("running")
led_onboard(1)
utime.sleep(0.5)
led_onboard.toggle()
utime.sleep(0.5)
led_onboard.toggle()
utime.sleep(0.5)
led_onboard.toggle()
utime.sleep(0.5)

while True:
    led_onboard(1)
    utime.sleep(1)
    led_onboard.toggle()
    machine.lightsleep(5000)
    led_onboard(1)
    utime.sleep(1)
    led_onboard.toggle()
    machine.deepsleep(5000)
