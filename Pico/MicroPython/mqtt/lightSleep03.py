import utime
import machine

led_onboard = machine.Pin(25, machine.Pin.OUT)

def gotoSleep():
    machine.lightsleep(10000)

def blinkLED():
    for i in range(10):
        led_onboard.value(1)
        utime.sleep(0.5)
        led_onboard.value(0)
        utime.sleep(0.5)

def calendar():
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in range(10 ):
        (year,month,day,hour,minute,second,wday,yday)=utime.localtime(utime.time())    
        print("%d-%02d-%02d %02d:%02d:%02d %s, day %d of the year" %
         (year,month,day,hour,minute,second,str(days[wday]),yday))
        utime.sleep(1)

while True:
    calendar()
    utime.sleep(1)
    gotoSleep()
    utime.sleep(1)
    blinkLED()
    utime.sleep(1)
                              
