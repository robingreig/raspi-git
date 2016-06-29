#include <Arduino.h>
/*
  Blink2
  I want to modify the original to blink 2 LED'S  on the gertduino
  Led1 = port 13
  Led2 = port 9
  Led3 = port 10
 */

int Led1 = 13;
int Led2 = 9;
int Led3 = 10;

void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  pinMode(Led1, OUTPUT);
  pinMode(Led2, OUTPUT);
  pinMode(Led3, OUTPUT);
}

void loop() {
  digitalWrite(Led1, HIGH);   // set LED1 on
  delay(1000);              // wait for a second
  digitalWrite(Led2, HIGH);   // set LED2 on
  delay(1000);              // wait for a second
  digitalWrite(Led3, HIGH);   // set LED2 on
  delay(1000);              // wait for a second
  digitalWrite(Led1, LOW);    // set LED1 off
  delay(1000);              // wait for a second
  digitalWrite(Led2, LOW);    // set LED2 off
  delay(1000);              // wait for a second
  digitalWrite(Led3, LOW);    // set LED2 off
  delay(1000);              // wait for a second
}
