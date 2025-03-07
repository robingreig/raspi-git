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

  esp8266OLED_Voltage_Temp_PowerLatch01
  Robin Greig
  2025.02.23
  Push button to start esp8266
  Print DS18b20 Temperature on display
  Print BatteryVoltage at ADC
  Shut off after displaying each for 5 seconds
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
#define analogPin A0  // ESP8266 Analog Pin ADC0 = A0

// Initialize the OLED display using Arduino Wire:

SSD1306Wire display(0x3c, 14, 12);  // ADDRESS, SDA, SCL  

// Define power latch pin GPIO 5 / D1
const int powerLatch = 5;

// Start with ledState = LOW = ON
int ledState = LOW;

// GPIO where the DS18B20 is connected to
const int oneWireBus = 02;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

int DEBUG = 1; //0 = no serial printing

int interval = 5; // number of seconds to display values

int adcSample = 0; // Variable to store sample ADC

int adcValue = 0; // Variable to store running total of ADC samples

int adcAverage = 0; // Variable to average value of ADC

float adcFloat = 0; //Variable to convert ADC value to battery voltag

void battVolt(){
    // Sample the battery voltage x 3 then publish
  adcValue = 0; // Reset adcValue to 0  
  for (int i = 1; i < 4; i++) {
    // Read the Analogue Input value
    adcSample = analogRead(analogPin);
    if (DEBUG > 0) {
      Serial.print("ADC Sample = ");
      Serial.println(adcSample);
    }
    adcValue += adcSample;
    if (DEBUG > 0) {
      Serial.print("ADC Value = ");
      Serial.println(adcValue);
    }
    adcAverage = (adcValue/i);
    if (DEBUG > 0) {
      Serial.print("ADC Average = ");
      Serial.println(adcAverage);
    }
    delay(300); // delay 0.3 seconds between reads
  }
  adcFloat = adcAverage * 0.0142; // reads 15.0vdc @ 1.0vdc ADC input
  if (DEBUG > 0) {  
    Serial.print("ADC Float = ");
    Serial.println(adcFloat);
  }
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_16);
  display.drawString(10, 0, "Battery Voltage");
//  display.setFont(ArialMT_Plain_16);
//  display.drawString(0, 10, "Hello world");
  display.setFont(ArialMT_Plain_24);
  display.drawString(10, 26, String(adcFloat) + " V");
}

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

  for (int i = 0; i < interval; i++){
    // clear the display
    display.clear();

    // display the temperature
    readTemp();
  
    // write the buffer to the display
    display.display();

    delay(1000);
  }
  
  for (int i = 0; i < interval; i++){
    // clear the display
    display.clear();

    // display the battery voltage
    battVolt();
  
    // write the buffer to the display
    display.display();

    delay(1000);
  }
  
  if (ledState == LOW) {
    ledState = HIGH;  // Note that this switches the LED *off*
  } else {
    ledState = LOW;  // Note that this switches the LED *on*
  }
    delay(500);
  digitalWrite(LED_BUILTIN, ledState);
  
  // Turns the power latch circuit off
      digitalWrite(powerLatch, LOW);
      if (DEBUG > 0){
        Serial.println("powerLatch = LOW");
      }
}
