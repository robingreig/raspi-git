import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
pott = machine.ADC(26)

while True:
    led_onboard.toggle()
    print(pott.read_u16())
    utime.sleep(1)