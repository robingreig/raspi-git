import utime
import machine

print("Entering lightsleep")
machine.lightsleep(30000)

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

for _ in range(5):
    (year,month,day,hour,minute,second,wday,yday)=utime.localtime(utime.time())    
    print("%d-%02d-%02d %02d:%02d:%02d %s, day %d of the year" %
         (year,month,day,hour,minute,second,str(days[wday]),yday))
    utime.sleep(1)