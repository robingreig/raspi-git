#include <Arduino.h>
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
  Switch on A2 will turn Led2 on & off 
*/

int Led1 = 13; // D5 connected to pin 13
int Led2 = 9; // D6 connected to pin 9
int val = 0; //variable to store read data
int InPin = A2; // Input on A2

void setup() {                
  // initialize the digital pins.
  pinMode(Led1, OUTPUT);
  pinMode(Led2, OUTPUT);
  pinMode(InPin, INPUT);
}

void loop() {
  digitalWrite(Led1, HIGH);   // set the LED on
  delay(1000);              // wait for a second
  digitalWrite(Led1, LOW);    // set the LED off
  delay(1000);              // wait for a second
  val = digitalRead(InPin);  // Read the input
  digitalWrite(Led2, val);  //sets the LED to the buttons value
}
