
/*
  intToBin20230301a
  Robin Greig, 2023.03.01
  Integer to Binary for 8 channel relay
  So I can send it one number and it will turn on & off the 8 relays
  according to the binary number
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
}
 
  
void loop()
{
  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  for (int num = 0; num < 8; num++){
    //uint8_t bitsCount = sizeof(num) * 8;
    //char str[bitsCount +1];
    char str[3];
    itoa(num, str, 2);
    Serial.print("String: ");
    Serial.println(str);
    Serial.print("bitRead(num, 0): ");
    Serial.println(bitRead(num, 0));
    Serial.print("bitRead(num, 1): ");
    Serial.println(bitRead(num, 1));
    Serial.print("bitRead(num, 2): ");
    Serial.println(bitRead(num, 2));
    delay(3000);
  }
}
