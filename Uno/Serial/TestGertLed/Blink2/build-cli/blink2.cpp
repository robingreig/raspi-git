#include <Arduino.h>
/*
  Blink2
  I want to modify the original to blink 2 LED'S  on the gertduino
  LED1 = pin13
  LED2 = pin9
 */

int Led1 = 13;
int Led2 = 9;

void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  pinMode(Led1, OUTPUT);
  pinMode(Led2, OUTPUT);
}

void loop() {
  digitalWrite(Led1, HIGH);   // set LED1 on
  delay(1000);              // wait for a second
  digitalWrite(Led2, HIGH);   // set LED2 on
  delay(1000);              // wait for a second
  digitalWrite(Led1, LOW);    // set LED1 off
  delay(1000);              // wait for a second
  digitalWrite(Led2, LOW);    // set LED2 off
  delay(1000);              // wait for a second
}
