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

// digital pin 5
#define BUTTON_PIN 5

// button state
bool current = false;
bool last = false;
int count = 0;

// set up the 'digital' feed
AdafruitIO_Feed *door = io.feed("door");
AdafruitIO_Feed *counter = io.feed("counter");

void setup() {

  // set button pin as an input
  pinMode(BUTTON_PIN, INPUT);
  pinMode(0,OUTPUT);
  
  // start the serial connection
  Serial.begin(115200);

  // wait for serial monitor to open
  while(! Serial);

    // connect to io.adafruit.com
  Serial.print("Connecting to Adafruit IO");
  io.connect();

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());

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
  if(digitalRead(BUTTON_PIN) == LOW)
  {
    current = false;
//    count = 0;
    digitalWrite(0,HIGH);
//    return;
  }
//  else
  {
    current = true;
  }
  // save the current state to the 'digital' feed on adafruit io
  digitalWrite(0,LOW);
  delay(500);
  digitalWrite(0,HIGH);
  Serial.print("Sending Button -> ");
  Serial.println(current);
  door->save(current);
  counter->save(count);
  Serial.print("Counter Value -> ");
  Serial.println(count);
  delay(9500);
  count = count +1;

}
