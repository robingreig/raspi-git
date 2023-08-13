/*
  SoilMqtt_20230215a
  Robin Greig, 2023.02.05
  Use Capacitive Moisture sensor to detect soil moisture content
  Return Analogue value to mqtt
  mqtt keepalive is only 15 seconds so I've added 2 functions
  to check for wifi & mqtt connection at the start of the loop
  mqtt broker: mqtt21.local
  mqtt topic: esp/test
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

int adcValue = 0;  /* Variable to store Output of ADC */

const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
char signal[6];
char adcChar[5];
String adcString;
 
WiFiClient espClient;
PubSubClient client(espClient);

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect("ESP8266Client")) {
      Serial.println("connected to MQTT");
      // Unique client ID (using ESP8266-03)  
      String client_id = "esp8266 - "; 
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      strcpy(signal, WiFiRSSI.c_str());
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
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
  client.publish("esp/soil01",adcChar);
  // delay 30 seconds (30 x 1000 = 30000)
//  delay(30000);
  // delay 1 minute (1 x 60 x 1000 = 60000)
//  delay(60000);
  // delay 5 minutes (5 x 60 x 1000 = 300000)
//  delay(300000);
  // delay 15 minutes (15 x 60 x 1000 = 900000)
  delay(900000);
}
