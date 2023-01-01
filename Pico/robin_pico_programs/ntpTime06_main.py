import network
import socket
import time
import struct

from machine import Pin

#tm_gmtoff is timezone offset for my time,
# MDT 6hr x 3600 seconds = 21600
tm_gmtoff = 21600
NTP_DELTA = 2208988800 + tm_gmtoff

rp2.country('CA')

host = "ca.pool.ntp.org"

led = Pin("LED", Pin.OUT)

ssid = 'Calalta02'
password = 'Micr0s0ft2018'

def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA    
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 60
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
while True:
    led.on()
    set_time()
    print(time.localtime())
    timestring = time.localtime()
    print('timestring = time.localtime()')
    rtc=machine.RTC()
    sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    timestamp=rtc.datetime()
    temperature = 27 - (reading - 0.706)/0.001721
    print('Temperature = ',temperature)
    timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
    print('Timestring = ',timestring)
    file = open("temps.txt", "a")
    file.write(timestring + "," + str(temperature) + "\n")
    file.flush()
    file.close()
    led.off()
    print('Sleeping')
    time.sleep(30)