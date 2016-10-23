#!/usr/bin/python

# Import Library & create instance of REST client
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Retrieve the most recent value from 'Outside-Temp'
data = aio.receive('BlockHeat02')
print('Received Value: {0}'.format(data.value))

