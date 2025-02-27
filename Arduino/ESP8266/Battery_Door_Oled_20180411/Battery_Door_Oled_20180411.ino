//
// Written by Todd Treece for Adafruit Industries
// Copyright (c) 2016 Adafruit Industries
// Licensed under the MIT license.
//
// All text above must be included in any redistribution.
//
// Battery_Door_Oled_20180401
// Robin Greig
/************************** Configuration ***********************************/

// edit the config.h tab and enter your Adafruit IO credentials
// and any additional configuration needed for WiFi, cellular,
// or ethernet clients.
#include "config.h"

/************************ Example Starts Here *******************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_FeatherOLED.h>

Adafruit_SSD1306 display = Adafruit_SSD1306();

// Digital pin 13 is the door switch
// Digital pins 4 & 5 are i2c lines
#define BUTTON_A 0
#define BUTTON_B 16
#define BUTTON_C 2
#define LED      0
#define BUTTON_PIN 13

// button state
bool current = false;
bool last = false;
int count = 0;
long previousAioMillis = 0;
long previousButtonMillis = 0;
int intervalAio = 10000;
//int intervalAio = 5000;
int intervalButtons = 5000;

// set up the Adafruit IO feeds
AdafruitIO_Feed *door = io.feed("door");
AdafruitIO_Feed *counter = io.feed("counter");
AdafruitIO_Feed *battery = io.feed("battery");

#if (SSD1306_LCDHEIGHT != 32)
 #error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

void setup() {  

  // set button pin as an input with pull up resistor
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(BUTTON_A, INPUT_PULLUP);
  pinMode(BUTTON_B, INPUT_PULLUP);
  pinMode(BUTTON_C, INPUT_PULLUP);

  
  // start the serial connection
//  Serial.begin(9600);
  Serial.begin(115200);

  // wait for serial monitor to open
  while(! Serial);
  delay(500);
  Serial.println("OLED FeatherWing test");
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x32)
  // init done
  Serial.println("OLED begun");

    // connect to io.adafruit.com
  Serial.print("Connecting to Adafruit IO");
  io.connect();

  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.
  display.display();
  delay(1000);

  // Clear the buffer.
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.print("OLED Starting");
  display.display();
  delay(1000);
  
  
  Serial.println("IO test");
  Serial.println("Trying RLG");

  // text display tests
  display.clearDisplay();
  display.setCursor(0,0);
  //display.println("Trying Calalta01");
  display.println("Trying RLG");
  display.display(); // actually display all of the above

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print(".");
//    display.setCursor(0,8);
//    display.print(".");
//    display.display();
    delay(500);
//    yield();
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());
  Serial.println(WiFi.localIP());
  display.setCursor(0,8);
  display.println("Connected!");
  display.println(WiFi.localIP());
  display.display();
}


void loop() {
  // io.run(); is required for all sketches.
  // it should always be present at the top of your loop
  // function. it keeps the client connected to
  // io.adafruit.com, and processes any incoming data.
  io.run();

  unsigned long currentMillis = millis();

  if(currentMillis - previousAioMillis > intervalAio) {
    // Save the last time
    previousAioMillis = currentMillis;
    
    // grab the current state of the button.
    // we have to flip the logic because we are
    // using a pullup resistor.
    if(digitalRead(BUTTON_PIN) == LOW) {
      current = false;
    } else {
    current = true;
    }
    // save the current state to the 'digital' feed on adafruit io
    Serial.print("Sending Button -> ");
    Serial.println(current);
    door->save(current);
    delay(10);
    yield();
    Serial.print("Counter Value -> ");
    Serial.println(count);
    counter->save(count);
    delay(10);
//    yield();
  
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
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("Connected > ");
    display.println(WiFi.SSID());
    display.println(WiFi.localIP());
    display.print("RSSI = ");
    display.println(WiFi.RSSI());
    display.print("Count = ");
    display.println(count);
    display.display();
    count = count +1;
  }
  if (! digitalRead(BUTTON_A)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("A");
  } else if (! digitalRead(BUTTON_B)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("B");
  } else if (! digitalRead(BUTTON_C)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("C");
  }
  delay(10);
//  yield();
  display.display();
}

