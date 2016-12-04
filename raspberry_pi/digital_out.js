var GpioStream = require('gpio-stream'),
    light = GpioStream.writable(18),
    AIO = require('adafruit-io'),
    button = GpioStream.readable(17);

// replace xxxxxxxxxxx with your Adafruit IO key
var AIO_KEY = '7e01e8b5e56360efc48a27682324fc353e18d14f',
    AIO_USERNAME = 'robingreig';

// aio init
var aio = AIO(AIO_USERNAME, AIO_KEY);

// pipe light data to the powerswitch tail
aio.feeds('lamp').pipe(light);

aio.feeds('lamp').pipe(process.stdout);

// pipe the button presses to the LED
button.pipe(light);

console.log('listening for lamp data...');
