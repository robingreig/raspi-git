# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('7e01e8b5e56360efc48a27682324fc353e18d14f')

# Send the value 100 to a feed called 'Foo'.
<<<<<<< HEAD
aio.send('basement-temp', 19.5)
=======
aio.send('basement-temp', 19.7)
>>>>>>> 3e2af9f50905d5c19f738ff0d64d834a5661e358

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('basement-temp')
print('Received value: {0}'.format(data.value))
