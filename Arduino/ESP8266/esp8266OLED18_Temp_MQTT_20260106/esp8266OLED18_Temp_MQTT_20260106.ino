/*
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
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <string.h>

const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password

//const char* ssid = "Calalta03"; // Enter your WiFi name
//const char* password =  "Micr0$0ft2024"; // Enter WiFi password

//const char *ssid = "TELUS2547"; // Enter your WiFi name 
//const char *password = "g2299sjk6p";  // Enter WiFi password 

const char* mqttServer = "192.168.200.143";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
const char *topic1 = "esp8266/18/temp";
const char *topic2 = "esp8266/18/RSSI";

char rssiSignal[6]; // setup rssi global variable for mqtt
char *tempChar = "0.0"; // temp needs to be char for mqtt

WiFiClient espClient;
PubSubClient client(espClient);

// Initialize the OLED display using Arduino Wire:

SSD1306Wire display(0x3c, 14, 12);  // ADDRESS, SDA, SCL  

// GPIO where the DS18B20 is connected to
const int oneWireBus = 02;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

int DEBUG = 0; //0 = no serial printing
//int timeDelay = 5000; // 5 sec time delay
//int timeDelay = 30000; // 30 sec time delay
int timeDelay = 60000; // 60 sec time delay


void reconnectMQTT() {
  // Loop until we're reconnected
  while (!client.connected()) {
    // Attempt to connect
    Serial.println("Attempting MQTT connection...");
    // Establish unique ID string
    String client_id = "esp8266 > ";
    client_id += String(WiFi.macAddress());
    Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
    if (client.connect(client_id.c_str())) {
      Serial.println("Connected!!");
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      strcpy(rssiSignal, WiFiRSSI.c_str());
      client.publish(topic2, rssiSignal,"-r"); // publish RSSI 
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void reconnectWiFi() {
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
}

void readTemp(){
  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);
  sprintf(tempChar, "%.2f", temperatureC);
  if (DEBUG > 0){
    Serial.print(temperatureC);
    Serial.println("ºC");
  }
  client.publish(topic1, tempChar, "-r"); // publish temp
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

  client.setServer(mqttServer, mqttPort);

  // Initialising the UI will init the display too.
  display.init();

  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);

  // Start the DS18B20 sensor
  sensors.begin();
}

void loop() {

  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  // Connect to MQTT if not connected
  if(!client.connected()) {
    reconnectMQTT();
  }

  client.loop();

  // clear the display
  display.clear();

    // display the temperature
    readTemp();
  
    // write the buffer to the display
    display.display();

    delay(timeDelay);

}
