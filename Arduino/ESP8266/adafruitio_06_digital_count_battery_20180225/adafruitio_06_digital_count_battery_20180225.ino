// Adafruit IO Digital Input Example
// Tutorial Link: https://learn.adafruit.com/adafruit-io-basics-digital-input
//
// Adafruit invests time and resources providing this open source code.
// Please support Adafruit and open source hardware by purchasing
// products from Adafruit!
//
// Written by Todd Treece for Adafruit Industries
// Copyright (c) 2016 Adafruit Industries
// Licensed under the MIT license.
//
// All text above must be included in any redistribution.

/************************** Configuration ***********************************/

// edit the config.h tab and enter your Adafruit IO credentials
// and any additional configuration needed for WiFi, cellular,
// or ethernet clients.
#include "config.h"

/************************ Example Starts Here *******************************/

// digital pin 4 & 5
#define VOLTAGE_PIN 4
#define DIGITAL_PIN 5

// button state
bool current = false;
bool last = false;
int count = 0;
float battVolt = 0;

// set up the 'digital' feed
AdafruitIO_Feed *door = io.feed("door");
AdafruitIO_Feed *counter = io.feed("counter");
AdafruitIO_Feed *battery = io.feed("battery");

void setup() {

  // set button pin as an input
  pinMode(DIGITAL_PIN, INPUT);
  pinMode(VOLTAGE_PIN, INPUT);
  pinMode(0, OUTPUT);
  pinMode(2, OUTPUT);
  
  // start the serial connection
  Serial.begin(115200);

  // wait for serial monitor to open
  while(! Serial);

  // connect to io.adafruit.com
  Serial.print("Connecting to Adafruit IO\n");
  io.connect();

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print("Still trying to connect to Adafruit IO\n");
    delay(500);
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());
  digitalWrite(0, LOW);
  delay(200);
  digitalWrite(0, HIGH);
  delay(200);
  digitalWrite(0, LOW);
  delay(200);
  digitalWrite(0, HIGH);
  delay(200);
  digitalWrite(0, LOW);
  delay(200);
  digitalWrite(0, HIGH);
}

void loop() {

  // io.run(); is required for all sketches.
  // it should always be present at the top of your loop
  // function. it keeps the client connected to
  // io.adafruit.com, and processes any incoming data.
  io.run();

  // grab the current state of the button.
  // we have to flip the logic because we are
  // using a pullup resistor.
  if(digitalRead(DIGITAL_PIN) == LOW)
    current = false;
  else
    current = true;
  if(digitalRead(VOLTAGE_PIN) == LOW)
    battVolt = 2.5;
  else
    battVolt = 13.8;

  // return if the value hasn't changed
  if(current == last)
    return;

  // save the current state to the 'digital' feed on adafruit io
  Serial.print("sending button -> ");
  Serial.println(current);
  door->save(current);
  counter->save(count);
  battery->save(battVolt);
  count = count +1;
  // blink LED to show data transfer
  digitalWrite(2, LOW);
  delay(200);
  digitalWrite(2, HIGH);
  delay(200);
  digitalWrite(2, LOW);
  delay(200);
  digitalWrite(2, HIGH);
  delay(200);
  digitalWrite(2, LOW);
  delay(200);
  digitalWrite(2, HIGH);
    
  // store last button state
  last = current;

}
