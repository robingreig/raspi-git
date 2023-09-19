/*********
 * mqtt_oled_20230829a
 * Robin Greig 2023.08.29
 * Display RSSi and IP Address on OLED as a dynamic value
 * Publish RSSI on esp8266/11/RSSI
 * Publish MAC on esp8266/11/MAC
 * Publish IP on esp8266/11/IP
*********/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// WiFi
const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
// MQTT
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
// Variables
const char *rssi = "esp8266/11/RSSI";
const char *mac = "esp8266/11/MAC";
const char *ipaddr = "esp8266/11/IP";

unsigned long previousMillis = 0; // will store last time MQTT published
const long interval = 6000; // 6 second interval at which to publish MQTT values
//const long interval = 8000; // 8 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

WiFiClient espClient;
PubSubClient client(espClient);

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

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect("ESP8266Client")) {
      Serial.println("connected to MQTT");
      // Unique client ID (using ESP8266-03)  
      String client_id = "esp8266-"; 
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
      if (client.connect(client_id.c_str())){
        Serial.printf("The client %s is connected to MQTT\n", client_id.c_str());
        String WiFiRSSI = String(WiFi.RSSI());
        Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      }
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(500);
    }
  }
}

void setup() {
  
  Serial.begin(115200);

  client.setServer(mqttServer, mqttPort);  

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

  // Connect to MQTT if not connected
  if(!client.connected()) {
    reconnectMQTT();
  }

  unsigned long currentMillis = millis();
// Check to see if it is time to publish MQTT
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    // Publish RSSi to esp8266/09/RSSI with retain flag set
    String WiFiRSSI = String(WiFi.RSSI());
    client.publish(rssi,WiFiRSSI.c_str(),"-r");
    delay(100);
    // Convert MAC Address to String & publish with retain flag set
    String WiFiMac = String(WiFi.macAddress());
    client.publish(mac,WiFiMac.c_str(),"-r");
    delay(100);
    // Convert IP Address to String & publish with retain flag set
    String WiFiAddr = WiFi.localIP().toString();
    client.publish(ipaddr,WiFiAddr.c_str(),"-r");
    delay(100);
    display.clearDisplay();
    display.setTextSize(2);
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
    display.println(WiFiRSSI);
    display.display();
  }
}
