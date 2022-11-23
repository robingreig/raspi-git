import rp2
import time
import network
import machine
from machine import Pin
from umqttsimple import MQTTClient
#from secrets_home import secrets
from secrets_work import secrets
from onewire import OneWire
from ds18x20 import DS18X20

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'],secrets['pw'])
rp2.country('CA')
led_wifi_connect = machine.Pin("LED", machine.Pin.OUT, value=0)
led_machine_reset = machine.Pin(12, machine.Pin.OUT, value=0)
led_mqtt_connect = machine.Pin(13, machine.Pin.OUT, value=0)
led_wifi_connecting = machine.Pin(14, machine.Pin.OUT, value=0)
led_Pump1_status = machine.Pin(15, machine.Pin.OUT, value=0)

#VARIABLES
ds = DS18X20(OneWire(Pin(16)))
DEBUG = 0
topic_pub = (secrets['pubTopic03'])
sensor = (secrets['red'])



# Wait for connect or fail
while True:
    attempts = 10
    while attempts > 0:
        led_wifi_connecting(1)
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        attempts -= 1
        if DEBUG > 0:
            print('waiting for connection...')
        time.sleep(1)
        led_wifi_connecting.toggle
        time.sleep(1)
    if wlan.status() != 3:
        machine.reset()
    else:
        if DEBUG > 0:
            print('connected')
            status = wlan.ifconfig()
            txpower = wlan.config('txpower')
            print( 'ip = ' + status[0] +',', 'netmask = ' + status[1] )
            print( 'gateway = ' + status[2] +',', 'dns server = '+status[3] )
#            print(wlan.ifconfig())
            print('txpower = '+ str(txpower))
        led_wifi_connecting(0)
        led_wifi_connect(1)
        break

#MQTT connect
def mqtt_connect():
    client = MQTTClient(secrets['client_id'], secrets['broker'], keepalive=600)
    client.connect()
    if DEBUG > 0:
        print('Connected to %s MQTT Broker'%(secrets['broker']))
    return client

#lose mqtt connection & reset
def reconnect():
    if DEBUG > 0:
        print('Failed to stay connected to MQTT Broker. Reconnecting....')
    client = mqtt_connect()
#    machine.reset()


while True:
    try:
        if DEBUG > 0:
            print('Client Connecting...')
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    try:
        ds.convert_temp()
        time.sleep_ms(750)
        if DEBUG > 0:
            print('sensor value = ',sensor)
            print('sensor type = ',(type(sensor)))
        sensor1 = eval(sensor)
        if DEBUG > 0:
            print('sensor1 value after eval = ',sensor1)
            print('sensor1 type = ',(type(sensor1)))
        temp = (ds.read_temp(sensor1))
        if DEBUG > 0:
            print('Published Topic = ',topic_pub)
            time.sleep(2)
            print('temp = ',temp)
            time.sleep(2)
            print('publishing temp')
        temp = "%3.2f" % temp
        if DEBUG > 0:
            print('Formatted temp = ',temp)
#            client.publish(topic_pub, temp)
        client.publish(topic_pub, temp, retain=True)
        if DEBUG > 0:
            print('published TEMPERATURE!!!')
        time.sleep(60)
    except:
        reconnect()
    if DEBUG > 0:
        print('Client Disconnecting....')
        time.sleep(2)
    client.disconnect()
