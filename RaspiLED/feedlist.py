#!/usr/bin/env python3

# Import library and create instance of REST client
from Adafruit_IO import Client
aio = Client('ve6rbn', 'e69155097ffa4624ae09d57213e200ed')

# Get list of feeds
feeds = aio.feeds()

# print out the feed names:
for f in feeds:
    print('Feed: {0}'.format(f.name))


