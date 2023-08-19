/* PubSub_04_OTA.01
 * Robin Greig
 * 2023.08.19
 * Can be programmed OTA
 * Functions to call connect wifi & connect mqtt
 * So that if either fail, it will automatically reconnect
 * Sends RSSI via mqtt to verify ESP8266 is running
 * Watches mqtt topic which controls GPIO02 & 04
*/

#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include <PubSubClient.h>

// WiFi
const char* ssid = "Calalta02";
const char* password = "Micr0s0ft2018";

// MQTT Broker 

const char *mqttServer = "192.168.200.21";

const int mqttPort = 1883; 

const char *topic = "esp8266/11/GPIO"; 

const char *rssi = "esp8266/11/RSSI";

const char *mqtt_username = "emqx";  

const char *mqtt_password = "public"; 

unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
const long interval = 60000; // 60 second interval at which to publish MQTT values
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
  Serial.begin(115200);
  Serial.println("Booting");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("Connection Failed! Rebooting...");
    delay(5000);
    ESP.restart();
  }

  // Set pin 02 & 04 as output
  pinMode(02, OUTPUT);
  digitalWrite(02, HIGH); // Blue LED is OFF when HIGH
  pinMode(04, OUTPUT);
  digitalWrite(04, LOW);

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  // Port defaults to 8266
  // ArduinoOTA.setPort(8266);

  // Hostname defaults to esp8266-[ChipID]
  // ArduinoOTA.setHostname("myesp8266");

  // No authentication by default
  // ArduinoOTA.setPassword((const char *)"123");

  ArduinoOTA.onStart([]() {
    Serial.println("Start");
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
    else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
    else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
    else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
    else if (error == OTA_END_ERROR) Serial.println("End Failed");
  });
  ArduinoOTA.begin();
  Serial.println("Ready");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
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
    digitalWrite(04, HIGH);
    Serial.println("GPIO 04 ON");
  } else {
    digitalWrite(02, HIGH);
    Serial.println("GPIO 02 OFF");
    digitalWrite(04, LOW);
    Serial.println("GPIO 04 OFF");
  }

  Serial.println(); 
  Serial.println("-----------------------"); 

} 


void loop() {
  ArduinoOTA.handle();
  
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
