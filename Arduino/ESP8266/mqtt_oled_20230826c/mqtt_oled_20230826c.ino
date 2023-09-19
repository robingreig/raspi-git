/*********
 * mqtt_oled_20230826c
 * Robin Greig 2023.08.26
 * Display RSSi and IP Address on OLED as a dynamic value
*********/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// WiFi
const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password

unsigned long previousMillis = 0; // will store last time MQTT published
const long interval = 6000; // 6 second interval at which to publish MQTT values
//const long interval = 8000; // 8 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

WiFiClient espClient;

void reconnectWiFi() {
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  
  Serial.begin(115200);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  delay(2000);
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(15, 20);
  display.println("Starting");
  display.display();
}

void loop() {

  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  unsigned long currentMillis = millis();
// Check to see if it is time to publish MQTT
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    display.clearDisplay();
    display.setTextSize(2);
    String WiFiAddr = WiFi.localIP().toString();
//    display.setCursor(25,25);
    display.setCursor(40,0);
    display.println("IP:");
    display.setCursor(10,20);
    for (int i = 0; i < 7; i++){
      display.print(WiFiAddr[i]);
    }
    display.println(WiFiAddr[7]);
    display.setCursor(15,40);
    for (int i = 8; i < 14; i++){
      display.print(WiFiAddr[i]);
    }
    display.println(WiFiAddr[14]);
    display.display();
    delay(3000);
    display.clearDisplay();
    display.setCursor(40, 0);
    // Display static text
    display.println("RSSI:");
    display.setTextSize(4);
    display.setCursor(25, 25);
    // Display dynamic RSSI
    String WiFiRSSI = String(WiFi.RSSI());
    display.println(WiFiRSSI);
    display.display();
  }
}
