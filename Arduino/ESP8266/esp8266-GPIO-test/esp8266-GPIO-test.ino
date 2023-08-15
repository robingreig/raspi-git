
/* esp8266-GPIO-test
 *  Robin Greig, 2023.08.13
 *  Use to test outputs on ESP8266
 *  Initialize GPIO00, FLASH pin as an output
 *  Initialize GPIO02, Internal Blue LED as an output
 *  Initialize GPIO4, SDA pin as an output
 *  Initialize GPIO5, SCL pin as an output
 *  Initialize GPIO12, MISO pin as an output
 *  Initialize GPIO13, MOSI pin as an output
 *  Initialize GPIO14, SCLK pin as an output
 *  Initialize GPIO15, CS pin as an output
 *  Initialize GPIO16, WAKE pin as an output
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *ssid = "Calalta02"; // Enter your WiFi name
const char *password =  "Micr0s0ft2018"; // Enter WiFi password
// MQTT
const char *mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char *mqttUser = "otfxknod";
const char *mqttPassword = "nSuUc1dDLygF";
// Topic
const char *topic01 = "esp8266/10/GPIO";
const char *rssi = "esp8266/10/RSSI";

WiFiClient espClient;
PubSubClient client(espClient);

int pinNum[9] = {00, 02, 04, 05, 12, 13, 14, 15, 16};

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
      client.subscribe(topic01); // subscribe to mqtt channel
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
    Serial.println("ANSI 48 = All Outputs OFF");
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
  }else if (*payload == 49){ // 49 = ansi 1
      for (int i = 0; i < 9; i++){ 
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[0], HIGH); // Turn ON GPIO00
      Serial.println("GPIO00 is ON");
  }else if (*payload == 50){ // 50 = ansi 2
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[1], HIGH); // Turn ON GPIO2
      Serial.println("GPIO02 is ON, Blue LED may be off?");
  }else if (*payload == 51){ // 51 = ansi 3
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[2], HIGH); // Turn ON GPIO04
      Serial.println("GPIO04 is ON");
  }else if (*payload == 52){ // 52 = ansi 4
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[3], HIGH); // Turn ON GPIO05
      Serial.println("GPIO05 is ON");
  }else if (*payload == 53){ // 53 = ansi 5
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[4], HIGH); // Turn ON GPIO12
      Serial.println("GPIO12 is ON");
  }else if (*payload == 54){ // 54 = ansi 6
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[5], HIGH); // Turn ON GPIO13
      Serial.println("GPIO13 is ON");
  }else if (*payload == 55){ // 55 = ansi 7
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[6], HIGH); // Turn ON GPIO14
      Serial.println("GPIO14 is ON");
  }else if (*payload == 56){ // 56 = ansi 8
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[7], HIGH); // Turn ON GPIO15
      Serial.println("GPIO15 is ON");
  }else if (*payload == 57){ // 57 = ansi 9
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
      }
      digitalWrite(pinNum[8], HIGH); // Turn ON GPIO17
      Serial.println("GPIO16 is ON");
  }else{
      for (int i = 0; i < 9; i++){
        digitalWrite(pinNum[i], LOW); // Turn all outputs off
      }
  }
  String WiFiRSSI = String(WiFi.RSSI());
  // publish RSSI to esp/rssi with retain flag set
  client.publish(rssi,WiFiRSSI.c_str(),"-r");
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
