var GpioStream = require('gpio-stream'),
    button = GpioStream.readable(17);
    led = GpioStream.writable(18);

// pipe the button press to stdout
button.pipe(process.stdout);
button.pipe(led);

