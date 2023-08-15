/*  Pub_DeepSleep.02
 *  Robin Greig
 *  2023.10.13
 *  Subscribe to ESP8266/05/GPIO04
 *  In order for subscribe to work had to add additional delay 
 *  after client.subscribe & run client.loop() at least twice
 *  Subscribed GPIO turns off in DeepSleep
 *  Connects to wifi and sends RSSI, IP, & MAC via mqtt
 *  Sleeps for 60 Seconds
 *  To DeepSleep connect pins D0 / GPIO16 to Reset
 *  I'm curious how long it will run on a 9v battery
*/
#include <ESP8266WiFi.h> 

#include <PubSubClient.h> 

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqttServer = "192.168.200.21";

const int mqttPort = 1883; 

// Topics

const char *topic01 = "esp8266/07/GPIO04";  

const char *rssi = "esp8266/07/RSSI";

const char *mac = "esp8266/07/MAC";

const char *ipaddr = "esp8266/07/IP";

// MQTT Security

const char *mqtt_username = "emqx"; 

const char *mqtt_password = "public"; 

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
      delay(100);
      Serial.println("Subsribing to topic01");
      client.subscribe(topic01); // subscribe to mqtt topic
      // Added extra delay to allow subscribe process to complete
      delay(1000);
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
    for (int i = 0; i < 5; i++){
    digitalWrite(04, HIGH);
    Serial.println("GPIO 04 ON");
    delay(1000);
    digitalWrite(04, LOW);
    Serial.println("GPIO 04 OFF");
    delay(1000);
    }
  } else {
    digitalWrite(04,LOW);
    Serial.println("GPIO 04 OFF");
  }

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

  // Just running client.loop() once didn't pull topic value when it woke up
  for (int i = 0; i < 2; i++) { 
    Serial.println("Running client.loop()");
    client.loop();
    delay(100);
  }
  Serial.println("Going to sleep for 60 seconds");
  ESP.deepSleep(60e6);
} 
