import utime
import machine

led_onboard = machine.Pin(25, machine.Pin.OUT)


machine.lightsleep(30000)

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

for _ in range(5):
    (year,month,day,hour,minute,second,wday,yday)=utime.localtime(utime.time())    
    print("%d-%02d-%02d %02d:%02d:%02d %s, day %d of the year" %
         (year,month,day,hour,minute,second,str(days[wday]),yday))
    utime.sleep(1)

while True:
    led_onboard.value(1)
    utime.sleep(0.5)
    led_onboard.value(0)
    utime.sleep(0.5)