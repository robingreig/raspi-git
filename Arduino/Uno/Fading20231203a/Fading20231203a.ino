/*
  Fading

  This example shows how to fade an LED using the analogWrite() function.

  The circuit:
  - LED attached from digital pin 9 to ground through 220 ohm resistor.

  created 1 Nov 2008
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Fading
*/
const int lowPin = 2; // pushbutton for 50%
const int highPin = 3; // pushbutton for 100%
int fetPin = 9;    // MOSFET connected to digital pin 9
int lowState = 0; // set initial button status
int highState = 0; // set initial button status

void setup() {
  // initialize pushbutton pin as input
  pinMode(lowPin, INPUT_PULLUP);
  pinMode(highPin, INPUT_PULLUP);
}

void loop() {
  lowState = digitalRead(lowPin); // read the state of the low button
  highState = digitalRead(highPin); // read the state of the high button
  if (lowState == LOW) { // if button is pressed
    analogWrite(fetPin, 127);
  } else if (highState == LOW) {
    analogWrite(fetPin, 255);
  } else {
    analogWrite(fetPin, 0);
  }
}
