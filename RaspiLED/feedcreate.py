# Import library and create instance of REST client
from Adafruit_IO import Client, Feed
aio = Client('e69155097ffa4624ae09d57213e200ed')

# Create Feed object with name 'Foo'
feed = Feed(name='Foo')

# Send the Feed to IO to create
# The returned object will contain all of the details about the feed
result = aio.create_feed(feed)
