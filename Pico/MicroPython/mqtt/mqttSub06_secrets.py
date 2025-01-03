import machine
import time
import network
import rp2
from machine import Pin, WDT
from umqttsimple import MQTTClient
from secrets_home import secrets'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'], secrets['pw'])
rp2.country('CA')
led_wifi_connect = machine.Pin("LED", machine.Pin.OUT, value=0)
led_machine_reset = machine.Pin(12, machine.Pin.OUT, value=0)
led_mqtt_connect = machine.Pin(13, machine.Pin.OUT, value=0)
led_wifi_connecting = machine.Pin(14, machine.Pin.OUT, value=0)
led_Pump1_status = machine.Pin(15, machine.Pin.OUT, value=0)

# enable WDT with a timeout of 5s
###wdt = WDT(timeout=8000)

# Wait for connect or fail
while True:
    max_wait = 10
    while max_wait > 0:
        led_wifi_connecting(1)
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)
        led_wifi_connecting(0)
        time.sleep(1)
        ###wdt.feed()
    if wlan.status() < 0 or wlan.status() >=3:
        break
    led_machine_reset(1)
    time.sleep(5)
    machine.reset()

# Handle connection error
if wlan.status() != 3:
#    raise RuntimeError('network connection failed')
    print('network connection failed, resetting in 5 sec')
    led_machine_reset(1)
    time.sleep(5)
    machine.reset()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print(wlan.ifconfig())
    led_wifi_connecting(0)
    led_wifi_connect(1)
    ###wdt.feed()

    #mqtt config
topic_sub = 'Garden/Pump1'

last_message = 0
message_interval = 5
counter = 0

def sub_cb(topic_sub, msg):
    print('Received Message %s from topic %s', (msg, topic_sub))
    print(msg)
    if msg == b'0':
        led_Pump1_status(0)
    if msg == b'1':
        led_Pump1_status(1)

#MQTT connect
def mqtt_connect_sub():
    client = MQTTClient(secrets['client_id'],secrets['broker'])
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(secrets['pubtopicTemp'])
    print('Subscribed to %s MQTT Broker'%(mqtt_server))
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
        ###wdt.feed()
    except OSError as e:
        reconnect()
    
    while True:
        try:
            new_msg = client.check_msg()
            ###wdt.feed()
        except OSError as e:
            reconnect()
