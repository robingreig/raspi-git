import machine
import utime
wdt = machine.WDT(timeout=2000)
led = machine.Pin(15, machine.Pin.OUT)
led.value(0)

while True:
    wdt.feed()
    led.value(1)
    print("Delay 500ms")
    utime.sleep(0.5)
    wdt.feed()
    led.toggle()
    print("Delay 500ms")
    utime.sleep(0.5)
    wdt.feed()
    led.toggle()
    wdt.feed()
    print("Delay 1.5s")
    utime.sleep(1.5)
    wdt.feed()
    print("Delay 2s")
    utime.sleep(20)