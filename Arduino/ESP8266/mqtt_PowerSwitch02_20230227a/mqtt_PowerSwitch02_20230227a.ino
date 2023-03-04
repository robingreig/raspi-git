
/*
  mqtt_PowerSwitch_20230218b
  Robin Greig, 2023.02.18
  Use ESP8266 to switch 5VDC power to raspberry pi via
  BS-170 FET & IRF9540 MOSFET & 12V > 5v Power Supply
  mqtt keepalive is only 15 seconds so I've added 2 functions
  to check for wifi & mqtt connection at the start of the loop
  mqtt broker: mqtt21.local
  mqtt topic: esp/pSwitch01
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
 
WiFiClient espClient;
PubSubClient client(espClient);

int pinNum[9] = {16, 14, 12, 13, 15, 00, 04, 05, 02};
// Initialize Relay 1, GPIO16, WAKE pin as an output
// Initialize Relay 2, GPIO14, SCLK pin as an output
// Initialize Relay 3, GPIO12, MISO pin as an output
// Initialize Relay 4, GPIO13, MOSI pin as an output
// Initialize Relay 5, GPIO15, CS pin as an output
// Initialize Relay 6, GPIO0, FLASH pin as an output
// Initialize Relay 7, GPIO4, SDA pin as an output
// Initialize Relay 8, GPIO5, SCL pin as an output

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    // Unique client ID (using ESP8266 macAddress)  
    String client_id = "esp8266-";
    client_id += String(WiFi.macAddress());
    Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect(client_id.c_str())) {
      Serial.printf("The client %s is connected to MQTT\n", client_id.c_str());
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      client.subscribe("esp/pSwitch01"); // subscribe to mqtt channel
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
  for (int i = 0; i < 9; i++){
    pinMode(pinNum[i], OUTPUT);
    digitalWrite(pinNum[i], LOW); 
  }
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
}
 

void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Received ansi: ");
  Serial.println(*payload);
  if (*payload == 48){ // 48 = ansi 0
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
      }
  }else if (*payload == 49){ // 49 = ansi 1
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
        //delay(500);
      }
      digitalWrite(pinNum[0], HIGH); // Turn on Relay 1
  }else if (*payload == 50){ // 50 = ansi 2
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
      }
      digitalWrite(pinNum[1], HIGH); // Turn on Relay 2
  }else if (*payload == 51){ // 51 = ansi 3
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
      }
      digitalWrite(pinNum[2], HIGH); // Turn on Relay 3
  }else if (*payload == 52){ // 52 = ansi 4
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
      }
      digitalWrite(pinNum[3], HIGH); // Turn on Relay 4
  }else{
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW);
      }
  }
  String WiFiRSSI = String(WiFi.RSSI());
  // publish RSSI to esp/rssi with retain flag set
  client.publish("esp/rssi",WiFiRSSI.c_str(),"-r");
  delay(500);
}
  
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

  client.loop();
}
