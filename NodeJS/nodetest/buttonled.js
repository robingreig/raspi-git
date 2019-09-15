var Gpio = require('onoff').Gpio; // include onoff to interact with the GPIO
var LED = new Gpio(4,'out'); // use GPIO pin 4 and specify that it is an output
var pushButton = new Gpio(17, 'in', 'both'); // use Gpio pin 17 as inputer, an'both' button presse and releases should be handled

pushButton.watch(function(err, value) { // Watch for hardware interrupts on pushButton GPIO, speciy callback function
  if (err) { //if an error
    console.error('There was an error', err); // output error message to console
  return;
  }
  LED.writeSync(value); // turn LED on or off depending o the button state (0 or 1)
});


function unexportOnClose() { // function to run when exiting program
  LED.writeSync(0); // Turn LED off
  LED.unexport(); // Unexport GPIO to free resources
  pushButton.unexport(); // Unexprt Button GPIO to free resources
}

process.on('SIGINT', unexportOnClose);  // function to run when user closes using ctrl_c

