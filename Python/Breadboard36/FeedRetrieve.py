#Import library and create new REST client
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Get a list of feeds
feeds = aio.feeds()

# Print out feed names
for f in feeds:
    print('Feed: {0}'.format(f.name))
