/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led0 = 13;
int led1 = 9;
int led2 = 10;
int led3 = 3;
int led4 = 5;
int led5 = 6;
// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(led0, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // convoluted but simple way of running the LED's
  digitalWrite(led0, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                 // wait a while
  digitalWrite(led0, LOW);    // turn the LED off by making the voltage LOW
    // wait for a second
  digitalWrite(led1, HIGH);
  delay(100);
  digitalWrite(led1, LOW);

  digitalWrite(led2, HIGH);
  delay(100);
  digitalWrite(led2, LOW);

  digitalWrite(led3, HIGH);
  delay(100);
  digitalWrite(led3, LOW);

  digitalWrite(led4, HIGH);
  delay(100);
  digitalWrite(led4, LOW);

  digitalWrite(led5, HIGH);
  delay(100);
  digitalWrite(led5, LOW);

  digitalWrite(led4, HIGH);
  delay(100);
  digitalWrite(led4, LOW);

  digitalWrite(led3, HIGH);
  delay(100);
  digitalWrite(led3, LOW);

  digitalWrite(led2, HIGH);
  delay(100);
  digitalWrite(led2, LOW);

  digitalWrite(led1, HIGH);
  delay(100);
  digitalWrite(led1, LOW);
}
