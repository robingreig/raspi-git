/* SoilMqtt_20230813a
 *  Robin Greig, 2023.08.13
 *  Use Capacitive Moisture sensor to detect soil moisture content
 *  Return Analogue value to mqtt
 *  mqtt keepalive is only 15 seconds so I've added 2 functions
 *  to check for wifi & mqtt connection at the start of the loop
 *  Publish only, no subscrbe so I don't need the callback funcion
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

// WiFi
const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
// MQTT
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
// Variables
int adcValue = 0;  /* Variable to store Output of ADC */
const char *rssi = "esp8266/09/RSSI";
const char *mac = "esp8266/09/MAC";
const char *ipaddr = "esp8266/09/IP";
const char *soil = "esp8266/09/SOIL";
char adcChar[5]; // adc as a character
String adcString; // adc as a string

unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values
 
WiFiClient espClient;
PubSubClient client(espClient);

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
 
  client.setServer(mqttServer, mqttPort);
//  client.setCallback(callback);
}
 
//void callback(char* topic, byte* payload, unsigned int length) {
// 
//  Serial.print("Message arrived in topic: ");
//  Serial.println(topic);
//}
  
void loop()
{
  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  // Connect to MQTT if not connected
  if(!client.connected()) {
    reconnectMQTT();
  }

//  unsigned long currentMillis = millis();
  // Check to see if it is time to publish MQTT
//  if (currentMillis - previousMillis >= interval){
//    previousMillis = currentMillis;
    // Read the Analogue Input value
    adcValue = analogRead(analogPin);
    // Print the output in the Serial Monitor
    Serial.print("ADC Value = ");
    Serial.println(adcValue);
    // Convert the adcValue int to a string
    adcString=String(adcValue);
    Serial.print("ADC String = ");
    Serial.println(adcString);
    // Convert the adcString to a char
    adcString.toCharArray(adcChar,5);
    Serial.print("ADC Char = ");
    Serial.println(adcChar);
    client.loop();
    client.publish(soil,adcChar,"-r");
    delay(100);
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
//  }
  Serial.println("Going to sleep for 60 seconds");
  ESP.deepSleep(60e6);
}
