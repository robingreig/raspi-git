
/*
  8channelRelay_pSwitch02_20230304a
  Robin Greig, 2023.03.04
  Use 8 channel Relay board with built in ESP8266
  mqtt keepalive is only 15 seconds so I've added 2 functions
  to check for wifi & mqtt connection at the start of the loop
  mqtt broker: mqtt21.local
  mqtt topic: esp/pSwitch02
  Send mqtt message 0000000 for all off & 11111111 for all on
  each digit represents a relay (first on left & eigth on right)
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
      client.subscribe("esp/pSwitch02"); // subscribe to mqtt channel
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
  Serial.print("Full Message Arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  // Switch on Relay 1 & the BuiltInLED if a 1 was received as the first character
  if ((char)payload[0] == '1') {
    digitalWrite(pinNum[0], HIGH);   // Turn on Relay 1
    digitalWrite(BUILTIN_LED, LOW); // Turn on BuiltIn LED
  } else {
    digitalWrite(pinNum[0], LOW);  // Turn off Relay 1
    digitalWrite(BUILTIN_LED, HIGH); // Turn off BuiltIn LED
  }
  // Switch on Relay 2 if a 1 was received as the second character
  if ((char)payload[1] == '1') {
    digitalWrite(pinNum[1], HIGH);   // Turn on Relay 2
  } else {
    digitalWrite(pinNum[1], LOW);  // Turn off Relay 2
  }
  // Switch on Relay 3 if a 1 was received as the third character
  if ((char)payload[2] == '1') {
    digitalWrite(pinNum[2], HIGH);   // Turn on Relay 3
  } else {
    digitalWrite(pinNum[2], LOW);  // Turn off Relay 3
  }
  // Switch on Relay 4 if a 1 was received as the fourth character
  if ((char)payload[3] == '1') {
    digitalWrite(pinNum[3], HIGH);   // Turn on Relay 4
  } else {
    digitalWrite(pinNum[3], LOW);  // Turn off Relay 4
  }
  // Switch on Relay 5 if a 1 was received as the fifth character
  if ((char)payload[4] == '1') {
    digitalWrite(pinNum[4], HIGH);   // Turn on Relay 5
  } else {
    digitalWrite(pinNum[4], LOW);  // Turn off Relay 5
  }
  // Switch on Relay 6 if a 1 was received as the sixth character
  if ((char)payload[5] == '1') {
    digitalWrite(pinNum[5], HIGH);   // Turn on Relay 6
  } else {
    digitalWrite(pinNum[5], LOW);  // Turn off Relay 6
  }
  // Switch on Relay 7 if a 1 was received as the seventh character
  if ((char)payload[6] == '1') {
    digitalWrite(pinNum[6], HIGH);   // Turn on Relay 7
  } else {
    digitalWrite(pinNum[6], LOW);  // Turn off Relay 7
  }
  // Switch on Relay 8 if a 1 was received as the eighth character
  if ((char)payload[7] == '1') {
    digitalWrite(pinNum[7], HIGH);   // Turn on Relay 8
  } else {
    digitalWrite(pinNum[7], LOW);  // Turn off Relay 8
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
