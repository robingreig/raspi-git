/**
   The MIT License (MIT)

   Copyright (c) 2018 by ThingPulse, Daniel Eichhorn
   Copyright (c) 2018 by Fabrice Weinberg

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

   ThingPulse invests considerable time and money to develop these open source libraries.
   Please support us by buying our products (and not the clones) from
   https://thingpulse.com

  esp8266OLED_Text_PowerLatch01
  Robin Greig
  2025.01.28
  Push button to start esp8266
  Print DS18b20 Temperature on display
  Shut off after interval (5 seconds)
*/

// Include the correct display library

// For a connection via I2C using the Arduino Wire include:
//#include <Wire.h>               // Only needed for Arduino 1.6.5 and earlier
#include "SSD1306Wire.h"        // legacy: #include "SSD1306.h"
// OR #include "SH1106Wire.h"   // legacy: #include "SH1106.h"

#include <OneWire.h>
#include <DallasTemperature.h>

// Initialize the OLED display using Arduino Wire:

SSD1306Wire display(0x3c, 14, 12);  // ADDRESS, SDA, SCL  

// Define power latch pin GPIO 5 / D1
const int powerLatch = 5;

// reset timer every loop
unsigned long previousMillis = 0;

// Length of time before power down
const long interval = 5000;

// Start with ledState = LOW = ON
int ledState = LOW;

// GPIO where the DS18B20 is connected to
const int oneWireBus = 02;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);


void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println();

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  // Define powerLatch pin as an OUTPUT    
  pinMode(powerLatch, OUTPUT);  
  
  // Keeps the circuit on
  digitalWrite(powerLatch, HIGH);
  
  // Initialising the UI will init the display too.
  display.init();

  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);

  // Start the DS18B20 sensor
  sensors.begin();

}


void loop() {
  unsigned long currentMillis = millis();
  
  // clear the display
  display.clear();

  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);
  Serial.print(temperatureC);
  Serial.println("ºC");

  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_16);
  display.drawString(20, 0, "Temperature");
//  display.setFont(ArialMT_Plain_16);
//  display.drawString(0, 10, "Hello world");
  display.setFont(ArialMT_Plain_24);
  display.drawString(10, 26, String(temperatureC) + " ºC");
  
  // write the buffer to the display
  display.display();

  if (ledState == LOW) {
    ledState = HIGH;  // Note that this switches the LED *off*
  } else {
    ledState = LOW;  // Note that this switches the LED *on*
  }
    delay(500);
  digitalWrite(LED_BUILTIN, ledState);
  
  // Turn off at Interval
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      // Turns the power latch circuit off
      digitalWrite(powerLatch, LOW);
      Serial.println("powerLatch = LOW");
  }
}
