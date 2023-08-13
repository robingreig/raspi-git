// Pub_DeepSleep.01
// Connects to wifi and sends RSSI via mqtt
// Sleeps for 60 Seconds
// I'm curious how long it will run on a 9v battery
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

const char *topic01 = "esp8266/05/GPIO02"; 

//const char *topic02 = "esp8266/05/GPIO04"; 

const char *rssi = "esp8266/05/RSSI";

const char *mac = "esp8266/05/MAC";

const char *ipaddr = "esp8266/05/IP";

const char *mqtt_username = "emqx"; 

const char *mqtt_password = "public"; 

//unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
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
      Serial.println("Publishing esp8266/05/RSSI");
      // Convert RSSI to String & publish with retain flag set
      client.publish(rssi,WiFiRSSI.c_str(),"-r");
      delay(100);
      Serial.println("Publishing esp8266/05/MAC");
      // Convert MAC Address to String & publish with retain flag set
      String WiFiMac = String(WiFi.macAddress());
      client.publish(mac,WiFiMac.c_str(),"-r");
      delay(100);
      Serial.println("Publishing esp8266/05/IP");
      // Convert IP Address to String & publish with retain flag set
      String WiFiAddr = WiFi.localIP().toString();
      client.publish(ipaddr,WiFiAddr.c_str(),"-r");
      client.subscribe(topic01); // subscribe to mqtt topic
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(500);
    }
  }
}

void setup() { 
  // Set pin 04 as output
  pinMode(02, OUTPUT);
  digitalWrite(02, HIGH); // Internal LED is OFF when HIGH

  // Set software serial baud to 115200; 

  Serial.begin(115200);
  Serial.setTimeout(2000);

  while(!Serial) {}

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
    digitalWrite(02, LOW);
    Serial.println("GPIO 02 ON");
  } else {
    digitalWrite(02,HIGH);
    Serial.println("GPIO 02 OFF");
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

//  unsigned long currentMillis = millis();
  /* Check to see if it is time to publish MQTT, if the difference between the current
   *  time and the last time > 5 seconds then pubilish again
   */

//  if (currentMillis - previousMillis >= interval) {
    // Update previousMillis to current time
//    previousMillis = currentMillis;
    // Publish RSSi to esp/gdnRSSI01 with retain flag set
//    String WiFiRSSI = String(WiFi.RSSI());
//    client.publish(rssi,WiFiRSSI.c_str(),"-r");
//  }
  
  client.loop(); 
  Serial.println("Going to sleep for 60 seconds");
  ESP.deepSleep(60e6);
} 
