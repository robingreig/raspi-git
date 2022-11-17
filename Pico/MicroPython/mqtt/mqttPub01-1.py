import rp2
import time
import network
import machine
from machine import Pin
from umqttsimple import MQTTClient

#ssid = 'Calalta02'
#password = 'Micr0s0ft2018'
ssid = 'MakerSpaceTest'
password = 'P@55w0rd'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
rp2.country('CA')
led = machine.Pin("LED", machine.Pin.OUT, value=0)

# Wait for connect or fail
attempts = 30
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
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print(wlan.ifconfig())
    led.toggle()
    
    #mqtt config
#mqtt_server = '192.168.200.21'
mqtt_server = '192.168.204.1'
client_id = 'Pico0'
#user_t = 'pico'
#password_t = 'picopassword'
topic_pub = 'Garden/Pump1'

last_message = 0
message_interval = 5
counter = 0

#MQTT connect
def mqtt_connect():
#    client = MQTTClient(client_id, mqtt_server, user=user_t, password=password_t, keepalive=60)
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

#reconnect & reset
def reconnect():
    print('Failed to connected to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

while True:
    try:
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    
    while True:
        try:
            client.publish(topic_pub, msg='0')
            print('published 0')
            time.sleep(5)
            client.publish(topic_pub, msg='1')
            print('published 1')
            time.sleep(5)
        except:
            reconnect()
            pass
        print('Printed first set')
        try:
            client.publish(topic_pub, msg='0')
            print('published 0')
            time.sleep(5)
            client.publish(topic_pub, msg='1')
            print('published 1')
            time.sleep(5)
        except:
            reconnect()
            pass
        print('Printed second set')
        
        try:
            client.set_callback(gotMessage)
            client.subscribe(b"Garden/Pump1")
            print('subscribed to')
            client.wait_msg()
        except:
            reconnect()
            pass
        client.disconnect()
