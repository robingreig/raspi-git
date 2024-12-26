/*
  BatteryTruck_01_20240525
  Robin Greig, 2024.05.25
  Use Analogue input to monitor truck battery voltage
  Return Analogue value to mqtt
  mqtt keepalive is only 15 seconds so I've added 2 functions
  to check for wifi & mqtt connection at the start of the loop
  mqtt broker: mqtt21.local
  mqtt topic: esp/test
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

//const char* ssid = "Calalta02"; // Enter your WiFi name
//const char* password =  "Micr0s0ft2018"; // Enter WiFi password

const char* ssid = "Calalta03"; // Enter your WiFi name
const char* password =  "Micr0$0ft2024"; // Enter WiFi password

//const char *ssid = "TELUS2547"; // Enter your WiFi name 
//const char *password = "g2299sjk6p";  // Enter WiFi password 

const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";


char signal[6];
int adcValue = 0;  /* Variable to store Output of ADC */
float adcFloat = 0; /* Variable to store Output of ADC as voltage*/
char adcFloatChar[6]; /* Variable to store Voltage as a Char */
const char *topic1 = "esp8266/01/battVolt";
const char *topic2 = "esp8266/01/RSSI";
 
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
  /* Convert the digital ADC value to the actual voltage 
   *  as a float using a 12K and 3K3 resistor*/
  adcFloat = adcValue * 0.0478;
  Serial.print("ADC Float = ");
  Serial.println(adcFloat);
  // Convert voltage float into char
  sprintf(adcFloatChar, "%.2f", adcFloat);
  Serial.print("ADC Float Char = ");
  Serial.println(adcFloatChar);
  client.loop();
  client.publish(topic1,adcFloatChar,"-r");
  delay(2000);
  String strength = String(WiFi.RSSI());  
  client.publish(topic2, strength.c_str(),"-r"); // publish RSSI
  Serial.print("RSSI = ");
  Serial.printf(strength.c_str());
  Serial.println();
  Serial.printf("Published RSSI to: %s\n",topic2);
  Serial.println();
  delay(5000);
}
