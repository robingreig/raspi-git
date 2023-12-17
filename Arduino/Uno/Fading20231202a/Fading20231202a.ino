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
const int buttonPin = 2; // pushbutton for 50%
int ledPin = 9;    // LED connected to digital pin 9
int buttonState = 0; // set initial button status

void setup() {
  // initialize pushbutton pin as input
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  buttonState = digitalRead(buttonPin); // read the state of the button
  if (buttonState == LOW) { // if button is not pressed
  // fade in from min to 50% in increments of 5 points:
  //for (int fadeValue = 0 ; fadeValue <= 130; fadeValue += 5) {
    // sets the value (range from 0 to 255):
    //analogWrite(ledPin, fadeValue);
    analogWrite(ledPin, 127);
    // wait for 30 milliseconds to see the dimming effect
    //delay(100);
  //} 
  //delay(1000);
  }else {
  // fade out from max to min in increments of 5 points:
  //for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // sets the value (range from 0 to 255):
    //analogWrite(ledPin, fadeValue);
    analogWrite(ledPin, 255);
    // wait for 30 milliseconds to see the dimming effect
    //delay(100);
  //}
  //delay(500);
}
}
