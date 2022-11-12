import rp2
import time
import network
import machine
from umqttsimple import MQTTClient
from secrets_home import secrets
#from secrets_work import secrets

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'],secrets['pw'])
rp2.country('CA')
led_wifi_connect = machine.Pin("LED", machine.Pin.OUT, value=0)
led_machine_reset = machine.Pin(12, machine.Pin.OUT, value=0)
led_mqtt_connect = machine.Pin(13, machine.Pin.OUT, value=0)
led_wifi_connecting = machine.Pin(14, machine.Pin.OUT, value=0)
led_Pump1_status = machine.Pin(15, machine.Pin.OUT, value=0)


# Wait for connect or fail
while True:
    attempts = 30
    while attempts > 0:
        led_wifi_connecting(1)
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        attempts -= 1
        print('waiting for connection...')
        time.sleep(1)
        led_wifi_connecting.toggle
        time.sleep(1)
    if wlan.status() < 0 or wlan.status() >=3:
        break
    led_machine_reset(1)
    time.sleep(5)
    machine.reset()

# Handle connection error
if wlan.status() != 3:
# when the RuntimeError is rasied, program just stops
# And doesn't proceed to the next step, so it won't reset
    machine.reset()
#    raise RuntimeError('network connection failed')
#    led_machine_reset(1)
#    machine.reset()
else:
    print('connected')
    status = wlan.ifconfig()
    txpower = wlan.config('txpower')
    print( 'ip = ' + status[0] )
    print(wlan.ifconfig())
    print('txpower = '+ str(txpower))
    led_wifi_connecting(0)
    led_wifi_connect(1)

#MQTT topics
topic_sub1 = (secrets['pubTopic01'])

def sub_cb(topic_sub1, msg):
    print('Received Message %s from topic %s', (msg, topic_sub1))
    print(msg)
    if msg == b'0':
        led_Pump1_status(0)
    if msg == b'1':
        led_Pump1_status(1)

#MQTT connect
def mqtt_connect_sub():
    client = MQTTClient(secrets['client_id'], secrets['broker'], keepalive=600)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(secrets['pubTopic01'])
    print('Subscribed to %s MQTT Broker'%(secrets['broker']))
    led_mqtt_connect(1)
    return client

#reconnect & reset
def reconnect():
    print('Failed to connected to MQTT Broker. Reconnecting...')
    led_mqtt_connect(0)
    time.sleep(5)
    led_machine_reset(1)
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
