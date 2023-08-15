// PubSub_04.01
// Functions to call connect wifi & connect mqtt
// So that if either fail, it will automatically reconnect
// Sends RSSI via mqtt
// Watches mqtt topic which controls GPIO04
// 2023.10.10
// Robin Greig

#include <ESP8266WiFi.h> 

#include <PubSubClient.h> 

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqttServer = "192.168.200.21";

const int mqttPort = 1883; 

const char *topic = "esp8266/07/GPIP04"; 

const char *rssi = "esp8266/07/RSSI";

const char *mqtt_username = "emqx";  

const char *mqtt_password = "public"; 

unsigned long previousMillis = 0; // will store last time MQTT published
const long interval = 5000; // 5 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values

WiFiClient espClient; 

PubSubClient client(espClient); 


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
      client.subscribe(topic); // subscribe to mqtt topic
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(500);
    }
  }
}

void setup() { 
  // Set pin 04 as output
  pinMode(04, OUTPUT);
  digitalWrite(04, LOW);

  // Set software serial baud to 115200; 

  Serial.begin(115200); 

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

} 

 

void callback(char *topic, byte *payload, unsigned int length) { 

  Serial.print("Message arrived in topic: "); 
  Serial.println(topic); 
  Serial.print("Message:"); 

  for (int i = 0; i < length; i++) { 

      Serial.print((char) payload[i]); 

  } 
  Serial.println();
  Serial.println("-----------------------"); 

  if ((char)payload[0] == '1'){
    digitalWrite(04, HIGH);
    Serial.println("GPIO 04 ON");
  } else {
    digitalWrite(04,LOW);
    Serial.println("GPIO 04 OFF");
  }

  Serial.println(); 
  Serial.println("-----------------------"); 

} 

 

void loop() { 

  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  // Connect to MQTT if not connected
  if(!client.connected()) {
    reconnectMQTT();
  }

  unsigned long currentMillis = millis();
  /* Check to see if it is time to publish MQTT, if the difference between the current
   *  time and the last time > 5 seconds then pubilish again
   */

  if (currentMillis - previousMillis >= interval) {
    // Update previousMillis to current time
    previousMillis = currentMillis;
    // Publish RSSi to esp/gdnRSSI01 with retain flag set
    String WiFiRSSI = String(WiFi.RSSI());
    client.publish(rssi,WiFiRSSI.c_str(),"-r");
  }
  
  client.loop(); 
} 
