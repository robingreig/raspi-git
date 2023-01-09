/*
  mqtt8channelRelay20230108a
  Robin Greig
  2023.01.08
  mqtt 0 = all OFF
  mqtt 1 - 8 turns on that indvidual relay
  mqtt 9 = all ON
  Any other selection will turn them all off
  mqtt broker: mqtt21.local
  mqtt topic: esp/test
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

int pinNum[9] = {16, 5, 4, 0, 2, 14, 12, 13, 15};
//  Initialize D0, GPIO16, WAKE pin as an output
//  Initialize D1, GPIO5, SCL pin as an output
//  Initialize D2, GPIO4, SDA pin as an output
//  Initialize D3, GPIO0, FLASH pin as an output
//  Initialize D4, GPIO2, TXD1 pin as an output
//  Initialize D5, GPIO14, SCLK pin as an output
//  Initialize D6, GPIO12, MISO pin as an output
//  Initialize D7, GPIO13, MOSI pin as an output
//  Initialize D8, GPIO15, CS pin as an output

const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";
char signal[6];
 
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  for (int i = 0; i < 8; i++){
    pinMode(pinNum[i], OUTPUT);
    digitalWrite(pinNum[i], HIGH); 
  }
 
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
      String client_id = "esp8266- > "; 
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      strcpy(signal, WiFiRSSI.c_str());
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
 
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
    case 48: // ansi 48 = decimal 0
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      break;
    case 49: // ansi 49 = decimal 1
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[0], LOW);
      break;
    case 50: // ansi 50 = decimal 2
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[1], LOW);
      break;
    case 51: // ansi 51 = decimal 3
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[2], LOW);
      break;
    case 52: // ansi 52 = decimal 4
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[3], LOW);
      break;
    case 53: // ansi 53 = decimal 5
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[4], LOW);
      break;
    case 54: // ansi 54 = decimal 6
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[5], LOW);
      break;
    case 55: // ansi 55 = decimal 7
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[6], LOW);
      break;
    case 56: // ansi 56 = decimal 8
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      digitalWrite(pinNum[7], LOW);
      break;
    case 57: // ansi 57 = decimal 9
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], LOW);
      }
      break;
    default:
      for (int i = 0; i < 8; i++){
        digitalWrite(pinNum[i], HIGH);
      }
      break;
  }
}
 
void loop() {
  client.loop();
}
