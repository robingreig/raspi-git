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
 
void setup() {
 
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  pinMode(14, OUTPUT);
  
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect("ESP8266Client")) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }
 
//  client.publish("esp/test", "hello"); //Topic name
  client.publish("esp/test", mqttUser); //Topic name
  client.subscribe("esp/test");
}
 
void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Received ansi: ");
  Serial.println(*payload);
  switch(*payload){
    case 49: // ansi 49 = decimal 1
      digitalWrite(2, HIGH);
      digitalWrite(14, LOW);
      break;
    case 50: // ansi 50 = decimal 2
      digitalWrite(2, LOW);
      digitalWrite(14, HIGH);
      break;
    case 51: // ansi 51 = decimal 3
      digitalWrite(2, HIGH);
      digitalWrite(14, HIGH);
      break;
    default:
      digitalWrite(2, LOW);
      digitalWrite(14, LOW);
      break;
  }
}
 
void loop() {
  client.loop();
}
