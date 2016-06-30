#include <Arduino.h>
int Led1 = 13; // Led1 Port 13
int inPin = 8; // Switch Port
int val = 0; // Variable to store the read value

void setup() {
  pinMode(Led1, OUTPUT); // Set digital pin 13 as output
  pinMode(inPin, INPUT_PULLUP); // Set digital pin 12 as input
}

void loop() {
  val = digitalRead(inPin); // Read the input pin
  digitalWrite(Led1, val); // Set the LED to input value
}
