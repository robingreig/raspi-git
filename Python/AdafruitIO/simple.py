#!/usr/bin/python

# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony DiCola

# Import Adafruit IO REST client.
from Adafruit_IO import Client

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = '7e01e8b5e56360efc48a27682324fc353e18d14f'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Send a value to the feed 'Test'.  This will create the feed if it doesn't
# exist already.
aio.send('Test01', 42)

# Send a string value 'bar' to the feed 'Foo', again creating it if it doesn't 
# exist already.
aio.send('Test02', 'bar')

# Now read the most recent value from the feed 'Test'.  Notice that it comes
# back as a string and should be converted to an int if performing calculations
# on it.
data = aio.receive('Test01')
print('Retrieved value from Test has attributes: {0}'.format(data))
print('Latest value from Test: {0}'.format(data.value))

# Finally read the most revent value from feed 'Foo'.
data = aio.receive('Test02')
print('Retrieved value from Test has attributes: {0}'.format(data))
print('Latest value from Test: {0}'.format(data.value))
