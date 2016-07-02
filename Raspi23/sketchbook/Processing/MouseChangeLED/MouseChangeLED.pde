import processing.io.*; // use the GPIO library

// store the desired state of the LED in a variable
boolean ledOn = false; 

void setup() {
  // set pin 17 as an output:
  GPIO.pinMode(17, GPIO.OUTPUT);  
}

void draw() {
  if (ledOn == true) { // If the desired state is on, then:

    // turn the LED on:
    GPIO.digitalWrite(17, GPIO.HIGH);

    // and set the background red:
    background(255, 0, 0);
  }

  else { // otherwise:

    // turn the LED off:
    GPIO.digitalWrite(17, GPIO.LOW);

    // and set the background black:
    background(0, 0, 0);
  }
}

void mouseClicked() {
  // When the mouse is clicked, store the opposite of 
  // ledOn into ledOn, which toggles ledOn:
  ledOn = !ledOn;
}