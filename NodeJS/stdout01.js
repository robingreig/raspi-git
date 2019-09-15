var GpioStream = require('gpio-stream'),
    button = GpioStream.readable(17);

// pipe the button press to stdout
button.pipe(process.stdout);

