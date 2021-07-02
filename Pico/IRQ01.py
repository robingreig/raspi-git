import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN)

def button_handler(pin):
    button.irq(handler=None)
    print(pin)
    
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)