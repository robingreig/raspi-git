#!/usr/bin/python

# Example of using the MQTT client class to subscribe to a feed and print out
# any changes made to the feed.  Edit the variables below to configure the key,
# username, and feed to subscribe to for changes.

# Import standard python modules.
import time
import sys
import RPi.GPIO as GPIO

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = '7e01e8b5e56360efc48a27682324fc353e18d14f'
ADAFRUIT_IO_USERNAME = 'robingreig'  # See https://accounts.adafruit.com

# Set to the ID of the feed to subscribe to for updates.
#FEED_ID = 'Lamp'
FEED_ID1 = 'blockheat01'
FEED_ID2 = 'blockheat02'
FEED_ID3 = 'door'
FEED_ID4 = 'doorstate'

# Setup GPIO
last = 0
inputNum = 23
relay1 = 11
relay2 = 12
relay3 = 13
relay4 = 14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputNum,GPIO.IN)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
GPIO.setup(relay4,GPIO.OUT)
GPIO.output(relay1,GPIO.HIGH)
GPIO.output(relay2,GPIO.HIGH)
GPIO.output(relay3,GPIO.HIGH)
GPIO.output(relay4,GPIO.HIGH)

# Set Debug Varialble, 0 = off & 1 = on
Debug = 1

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    if Debug > 0:
      print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID1)
      print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID2)
      print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID3)
      print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID4)
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe(FEED_ID1)
    client.subscribe(FEED_ID2)
    client.subscribe(FEED_ID3)
    client.subscribe(FEED_ID4)

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    if Debug > 0:
      print 'Feed {0} received new value: {1}'.format(feed_id, payload)
    if feed_id == FEED_ID1:
      if payload == "1":
        GPIO.output(relay1,GPIO.LOW)
        if Debug > 0:
          print ("Relay 1 is ON")
      else:
        GPIO.output(relay1,GPIO.HIGH)
        if Debug > 0:
          print ("Relay 1 is OFF")
    if feed_id == FEED_ID2:
      if payload == "1":
        GPIO.output(relay2,GPIO.LOW)
        if Debug > 0:
          print ("Relay 2 is ON")
      else:
        GPIO.output(relay2,GPIO.HIGH)
        if Debug > 0:
          print ("Relay 2 is OFF")
    if feed_id == FEED_ID3:
      if payload == "1":
        GPIO.output(relay3,GPIO.LOW)
        if Debug > 0:
          print ("Relay 3 is ON")
      else:
        GPIO.output(relay3,GPIO.HIGH)
        if Debug > 0:
          print ("Relay 3 is OFF")
    if feed_id == FEED_ID4:
      if payload == "1":
        GPIO.output(relay4,GPIO.LOW)
        if Debug > 0:
          print ("Relay 4 is ON")
      else:
        GPIO.output(relay4,GPIO.HIGH)
        if Debug > 0:
          print ("Relay 4 is OFF")


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
client.loop_blocking()

# Pump the Light Switch loop
#client.loop_background()
#while True:
#  if (time.time() - last) >= 5:
#    state = GPIO.input(inputNum)
#    if (state):
#      print('Doorstate = 1')
#      client.publish('doorstate',1) 
#    else:
#      print('Doorstate = 0')
#      client.publish('doorstate',0)
#    last = time.time()

