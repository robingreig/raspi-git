/*
  Program Name: Blink02
  Author: Robin Greig & Arduino
  Date: 2019.04.27
  Turns an LED on for one second, then off for one second, repeatedly.
  Testing with pin 13 for ESP32 rather than LED_BUILTIN
  This example code is in the public domain.
  http://www.arduino.cc/en/Tutorial/Blink
*/
int ledPin = 13;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  Serial.println("Hello, world!");
  digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(2000);                       // wait for a second
  digitalWrite(ledPin, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
}
