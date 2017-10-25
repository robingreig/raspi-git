#Import library and create new REST client
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Get a list of feeds
data = aio.receive('Lamp')

# Print out feed metadata
print('Data Value: {0}'.format(data.value))
