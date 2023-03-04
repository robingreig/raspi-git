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
  pinMode(2, OUTPUT); // GPIO02 = D4
  digitalWrite(2, HIGH); //Turn off D4 / Blue Light
  pinMode(4, OUTPUT); // GPIO04 = D2
  digitalWrite(4, LOW); //Turn off D2
  pinMode(5, OUTPUT); // GPIO05 = D1
  digitalWrite(5, LOW); //Turn off D1
  pinMode(14, OUTPUT); // GPIO14 = D5
  digitalWrite(14, LOW); // Turn off D5 output to MOSFETS
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
}
 

void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Received ansi: ");
  Serial.println(*payload);
  if (*payload == 49){ // 49 = ansi 1
      digitalWrite(2, LOW); // Turn on D4 / Blue light on ESP-8266
      digitalWrite(14, HIGH); // Turn on D5
  }else if (*payload == 50){ // 50 = ansi 2
      digitalWrite(2, HIGH); // Turn off D4 / Blue Light
      digitalWrite(4, HIGH); // Turn on GPIO04, D2
      digitalWrite(5, LOW); // Turn off GPIO05, D1
      digitalWrite(14, LOW); // Turn off GPIO14, D5
  }else if (*payload == 51){ // 51 = ansi 3
      digitalWrite(2, HIGH); // Turn off D4 / Blue Light
      digitalWrite(4, LOW); // Turn off GPIO04, D2
      digitalWrite(5, HIGH); // Turn on GPIO05, D1
      digitalWrite(14, LOW); // Turn off GPIO14, D5
  }else if (*payload == 52){ // 52 = ansi 4
      digitalWrite(2, LOW); // Turn on D4 / Blue Light
      digitalWrite(4, HIGH); // Turn on GPIO04, D2
      digitalWrite(5, HIGH); // Turn on GPIO05, D1
      digitalWrite(14, HIGH); // Turn on GPIO14, D5
  }else{
    digitalWrite(2, HIGH); // Turn off D4 / Blue Light
    digitalWrite(4, LOW); // Turn off GPIO04, D2
    digitalWrite(5, LOW); // Turn on GPIO05, D1
    digitalWrite(14, LOW); // Turn off GPIO14, D5
  }
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
  
  // delay 30 seconds (30 x 1000 = 30000)
//  delay(30000);
  // delay 1 minute (1 x 60 x 1000 = 60000)
//  delay(60000);
  // delay 5 minutes (5 x 60 x 1000 = 300000)
//  delay(300000);
  // delay 15 minutes (15 x 60 x 1000 = 900000)
//  delay(900000);
}
