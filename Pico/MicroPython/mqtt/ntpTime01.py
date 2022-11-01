from mpython import *
import ntptime

mywifi=wifi()
mywifi.connectWiFi('tang','tang123456')

print("Local time before synchronization：%s" %str(time.localtime()))
ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime()))