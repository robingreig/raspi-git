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

  esp8266OLED_Temp
  Robin Greig
  2025.12.30
  Print DS18b20 Temperature on display
  ***** Cannot use GPIO 12 - 15 since they are used for OLED
*/

// Include the correct display library

// For a connection via I2C using the Arduino Wire include:
//#include <Wire.h>               // Only needed for Arduino 1.6.5 and earlier
#include "SSD1306Wire.h"        // legacy: #include "SSD1306.h"
// OR #include "SH1106Wire.h"   // legacy: #include "SH1106.h"

#include <OneWire.h>
#include <DallasTemperature.h>

// Define Analogue Pin
//#define analogPin A0  // ESP8266 Analog Pin ADC0 = A0

// Initialize the OLED display using Arduino Wire:

SSD1306Wire display(0x3c, 14, 12);  // ADDRESS, SDA, SCL  

// GPIO where the DS18B20 is connected to
const int oneWireBus = 02;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

int DEBUG = 1; //0 = no serial printing

void readTemp(){
  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);
  if (DEBUG > 0){
    Serial.print(temperatureC);
    Serial.println("ºC");
  }
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_16);
  display.drawString(20, 0, "Temperature");
//  display.setFont(ArialMT_Plain_16);
//  display.drawString(0, 10, "Hello world");
  display.setFont(ArialMT_Plain_24);
  display.drawString(10, 26, String(temperatureC) + " ºC");
}

void setup() {
  if (DEBUG > 0){
    Serial.begin(115200);
    Serial.println();
    Serial.println();
  }

  // Initialising the UI will init the display too.
  display.init();

  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);

  // Start the DS18B20 sensor
  sensors.begin();
}

void loop() {

    // clear the display
    display.clear();

    // display the temperature
    readTemp();
  
    // write the buffer to the display
    display.display();

    delay(5000);

}
