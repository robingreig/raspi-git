import time
import network
from machine import Pin
from umqttsimple import MQTTClient

ssid = 'MakerSpaceTest'
password = 'P@55w0rd'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
rp2.country('CA')
led = machine.Pin("LED", machine.Pin.OUT, value=0)

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
    time.sleep(2)
    machine.reset()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print(wlan.ifconfig())
    led.toggle()
    
    #mqtt config
mqtt_server = '192.168.204.1'
client_id = 'Pico03'
#user_t = 'pico'
#password_t = 'picopassword'
topic_pub = 'Garden/Pump1'

last_message = 0
message_interval = 5

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
    time.sleep(2)
    machine.reset()

while True:
    counter = 3
    try:
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    
    while counter > 0:
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
        print('printed set number %s'%(counter))
        counter -=1
        
    client.disconnect()