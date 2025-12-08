
/************************************************************************
 * 4channelRelay12_20251207
 * Robin Greig
 * 2025.12.07
 * Control 4 Relays via GPIO 14/D5 12/D6 13/D7 16
 * Use 4 channel Relay board with built in ESP8266
 * To program connect GPIO00 to GND pin & TX, RX, & GND to Raspi
 * device is nodeMCU 1.0 (ESP-12E module)
 * port is /dev/ttyUSB0
 * mqtt keepalive is only 15 seconds so I've added 2 functions
 * to check for wifi & mqtt connection at the start of the loop
 * mqtt broker: 192.168.200.143
 * mqtt topics: esp8266/12/relay1, 2 , 3, or 4
 * Send mqtt 0000 for all off & 1111 for all on
 * Each digit represents a relay (first on left & fourth on right)
 * And Publish RSSI on MQTT esp8266/12/RSSI
**************************************************************************/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <string.h>

#define relay1 16 // ESP8266 GPIO16 / D0 / WAKE controls relay1
#define relay2 14 // ESP8266 GPIO14 / D5 / SCLK controls relay2
#define relay3 12 // ESP8266 GPIO12 / D6 / MISO controls relay3
#define relay4 13 // ESP8266 GPIO13 / D7 / MOSI controls relay4


const char* ssid = "Calalta02"; // WiFi name
const char* password =  "Micr0s0ft2018"; // WiFi password
//const char* ssid = "Calalta03"; // WiFi name
//const char* password =  "Micr0$0ft2024"; // WiFi password
//const char* ssid = "TELUS2547"; // WiFi name
//const char* password =  "g2299sjk6p"; // WiFi password
//const char* mqttServer = "192.168.200.21";
const char* mqttServer = "192.168.200.143";
const int mqttPort = 1883;
//const char* mqttUser = "otfxknod";
//const char* mqttPassword = "nSuUc1dDLygF";

const char *relay01 = "esp8266/12/relay1"; // MQTT subscribe topic for relay1 inputs
const char *relay02 = "esp8266/12/relay2"; // MQTT publish topic for relay2 input
const char *relay03 = "esp8266/12/relay3"; // MQTT subscribe topic for relay1 inputs
const char *relay04 = "esp8266/12/relay4"; // MQTT publish topic for relay2 input
const char *rssi = "esp8266/12/RSSI"; // MQTT publish topic for signal RSSI

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
      client.publish(rssi,WiFiRSSI.c_str(),"-r"); // retain flag set
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      client.subscribe(relay01); // subscribe to mqtt topic
      client.subscribe(relay02); // subscribe to mqtt topic
      client.subscribe(relay03); // subscribe to mqtt topic
      client.subscribe(relay04); // subscribe to mqtt topic
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
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  digitalWrite(relay1, LOW);
  digitalWrite(relay2, LOW);
  digitalWrite(relay3, LOW);
  digitalWrite(relay4, LOW);
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
}
 
void callback(String topic, byte* message, unsigned int length) {
  Serial.println();
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  String messageTemp;  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  // If a message is received on the topic room/lamp, you check if the message is either on or off. Turns the lamp GPIO according to the message
  if(topic==relay01){
      Serial.print("Turning Relay1 ");
      if(messageTemp == "on"){
        digitalWrite(relay1, HIGH);
        Serial.println("On");
      }
        else if(messageTemp == "off"){
          digitalWrite(relay1, LOW);
          Serial.println("Off");
      }
  } else if (topic == relay02){
    Serial.print("Turning Relay2 ");
     if(messageTemp == "on"){
       digitalWrite(relay2, HIGH);
       Serial.println("On");
      } 
        else if(messageTemp == "off"){
          digitalWrite(relay2, LOW);
          Serial.println("Off");    
      }
  } else if (topic == relay03){
    Serial.print("Turning Relay3 ");
     if(messageTemp == "on"){
       digitalWrite(relay3, HIGH);
       Serial.println("On");
      } 
        else if(messageTemp == "off"){
          digitalWrite(relay3, LOW);
          Serial.println("Off");    
      }
   } else if (topic == relay04){
    Serial.print("Turnng Relay4 ");
     if(messageTemp == "on"){
       digitalWrite(relay4, HIGH);
       Serial.println("On");
      } 
        else if(messageTemp == "off"){
          digitalWrite(relay4, LOW);
          Serial.println("Off");    
      }  Serial.println();
  }
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
