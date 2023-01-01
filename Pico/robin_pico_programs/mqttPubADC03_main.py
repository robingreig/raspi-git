# mqttPubADC03_main.py is for Pico1 solar battery monitoring
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
conversion_factor = 3.34 / (65535)
# sleep_time between voltage measurements
sleep_time = 60

# Wait for connect or fail
max_wait = 600
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
    led.toggle()
    
    #mqtt config
mqtt_server = '192.168.200.21'
client_id = 'Pico1'
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
        voltage1 = potentiometer.read_u16() * conversion_factor
        print("Voltage 1 = ",voltage1)
        time.sleep(2)
        voltage2 = potentiometer.read_u16() * conversion_factor
        print("Voltage 2 = ",voltage2)
        time.sleep(2)
        voltage3 = potentiometer.read_u16() * conversion_factor
        print("Voltage 3 = ",voltage3)
        time.sleep(2)
        voltage = (voltage1 + voltage2 + voltage3)/3
        print('Average voltage = ',voltage)
        voltage = voltage * 4.5454545454
        print('Actual voltage = ',voltage)
        voltage = round(voltage,2)
        print('Float Voltage = ',voltage)
        voltage = str(voltage)
        print('String Voltage = ',voltage)
        client.publish(topic_pub2, voltage)
        print('published VOLTAGE!!!')
        time.sleep(sleep_time)
    except:
        reconnect()
        pass
    client.disconnect()