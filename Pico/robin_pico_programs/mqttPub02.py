import time
import network
from machine import Pin
from umqttsimple import MQTTClient

ssid = 'Calalta02'
password = 'Micr0s0ft2018'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
rp2.country('CA')
led = machine.Pin("LED", machine.Pin.OUT, value=0)
potentiometer = machine.ADC(26)
#conversion_factor = 3.3 / (65535)
conversion_factor = 3.3 / (61300)
sleep_time = 5

# Wait for connect or fail
max_wait = 60
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
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
mqtt_server = '192.168.200.21'
client_id = 'Pico0'
#user_t = 'pico'
#password_t = 'picopassword'
topic_pub1 = 'Garden/Pump1'
topic_pub2 = 'Garden/Pump2'

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
    client = mqtt_connect()
#    machine.reset()

while True:
    try:
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    try:
        voltage = potentiometer.read_u16() * conversion_factor
        print("Voltage raw= ",voltage)
        time.sleep(sleep_time)
        print('publishing str(voltage)')
        voltage = voltage * 4.5454545454
        voltage = str(voltage)
        print('voltage string = ',voltage)
        client.publish(topic_pub2, voltage)
        print('published VOLTAGE!!!')
        time.sleep(sleep_time)
    except:
        reconnect()
        pass
    client.disconnect()