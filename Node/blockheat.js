var GpioStream = require('gpio-stream'),
    heat01 = GpioStream.writable(15),
    heat02 = GpioStream.writable(18),
    AIO = require('adafruit-io');


// replace xxxxxxxxxxx with your Adafruit IO key
var AIO_KEY = '7e01e8b5e56360efc48a27682324fc353e18d14f',
    AIO_USERNAME = 'robingreig';

// aio init
var aio = AIO(AIO_USERNAME, AIO_KEY);

// pipe light data to the powerswitch tail
aio.feeds('blockheat01').pipe(heat01);
aio.feeds('blockheat02').pipe(heat02);

console.log('listening for lamp data...');
