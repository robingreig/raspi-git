import rp2
import time
import network
import ubinascii
from network import WLAN
import machine
from machine import Pin
from umqttsimple import MQTTClient

#ssid = 'Calalta02'
#password = 'Micr0s0ft2018'
ssid = 'TELUS2547'
password = 'g2299sjk6p'

#wlan = network.WLAN(network.STA_IF)
wlan = WLAN(network.STA_IF)
wlan.active(True)
rp2.country('CA')

accessPoints = wlan.scan()
for ap in accessPoints:
    print(ap)
    name = ap[0].decode()
    if name == 'TELUS2547':
        print('SSID = ',name)
        print('Channel = ',ap[2])
        print('RSSI = ',ap[3],'\n')
#    if name == 'Calalta02':
#        print('SSID = ',name)
#        print('Channel = ',ap[2])
#        print('RSSI = ',ap[3])


wlan.connect(ssid, password)
led_onboard = machine.Pin("LED", machine.Pin.OUT, value=0)

# See the MAC address of the Pico
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ',mac)

# Wait for connect or fail
attempts = 20
while attempts > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    attempts -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status1 = wlan.ifconfig()
    print( 'ip = ' + status1[0])
    print( 'Netmask = ' + status1[1])
    print( 'Gateway = ' + status1[2])
    print( 'DNS Server = ' + status1[3])
    led_onboard(1)
    print('WiFi Channel = '+str(wlan.config('channel')))
    print('WiFi ESSID = '+str(wlan.config('essid')))
    print('WiFi TXpower = '+str(wlan.config('txpower')))
    print('wlan.status[0] = '+str(wlan.status()))

