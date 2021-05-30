import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    user_name = input ("What is your name\n")
    if user_name == "Robin":
        print("Hi Boss")
    else:
        print("Do I know you?")
        