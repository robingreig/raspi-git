import time
import network
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
led_onboard = machine.Pin("LED", machine.Pin.OUT, value=0)
led_offboard = machine.Pin(22, machine.Pin.OUT, value=0)


# Wait for connect or fail
max_wait = 100
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    machine.reset()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print(wlan.ifconfig())
    led_onboard(1)
    
    #mqtt config
mqtt_server = '192.168.204.1'
client_id = 'Pico3'
#user_t = 'pico'
#password_t = 'picopassword'
topic_sub = 'Garden/Pump1'

last_message = 0
message_interval = 5
counter = 0

def sub_cb(topic_sub, msg):
    print('Received Message %s from topic %s', (msg, topic_sub))
    print(msg)
    if msg == b'0':
        print ('value is 0')
        led_offboard(0)
    if msg == b'1':
        print ('value is 1')
        led_offboard(1)

#MQTT connect
def mqtt_connect_sub():
#    client = MQTTClient(client_id, mqtt_server, user=user_t, password=password_t, keepalive=60)
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Subscribed to %s MQTT Broker'%(mqtt_server))
    return client

#reconnect & reset
def reconnect():
    print('Failed to connected to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

while True:
    try:
        client = mqtt_connect_sub()
    except OSError as e:
        reconnect()
    
    while True:
        try:
            new_msg = client.check_msg()
        except OSError as e:
            reconnect()
