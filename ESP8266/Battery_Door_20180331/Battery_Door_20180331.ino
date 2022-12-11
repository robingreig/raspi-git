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

// digital pin 5 is door switch
#define BUTTON_PIN 5
#define Battery_Interval 5
#define Sleep_Length 3

// button state
bool current = false;
bool last = false;
int count = 0;

// set up the Adafruit IO feeds
AdafruitIO_Feed *door = io.feed("door");
AdafruitIO_Feed *counter = io.feed("counter");
AdafruitIO_Feed *battery = io.feed("battery");

void setup() {

  // set button pin as an input with pull up resistor
  pinMode(BUTTON_PIN, INPUT_PULLUP);
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
  else
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
  delay(100);
  Serial.print("Counter Value -> ");
  Serial.println(count);
  counter->save(count);
  delay(100);
  
  // read the battery level from the ESP8266 analog in pin.
  // analog read level is 10 bit 0-1023 (0V-1V).
  // our 1M & 220K voltage divider takes the max
  // lipo value of 4.2V and drops it to 0.758V max.
  // this means our min analog read value should be 580 (3.14V)
  // and the max analog read value should be 774 (4.2V).
  int level = analogRead(A0);

  // convert battery level to percent
  //  level = map(level, 580, 774, 0, 100);
  level = map(level, 580, 810, 0, 100);
  Serial.print("Battery level: "); Serial.print(level); Serial.println("%");
  
  // send battery level to AIO
  battery->save(level);
  
  delay(9300);
  //delay(60000);  

  count = count +1;

}

