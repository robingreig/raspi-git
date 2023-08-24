/*  BasicOTA_GPIO_Test.01
 *  Robin Greig, 2023.08.19
 *  Can be programmed OTA
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
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include <PubSubClient.h>

// WiFi
//const char* ssid = "Calalta02";
//const char* password = "Micr0s0ft2018";
const char* ssid = "TELUS2547";
const char* password =  "g2299sjk6p";

// MQTT Broker 

const char *mqttServer = "192.168.200.21";

const int mqttPort = 1883; 

const char *topic = "esp8266/11/GPIO"; 

const char *rssi = "esp8266/11/RSSI";

const char *mac = "esp8266/11/MAC";

const char *ipaddr = "esp8266/11/IP";

const char *mqtt_username = "emqx";  

const char *mqtt_password = "public"; 

unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values

WiFiClient espClient; 

PubSubClient client(espClient); 

int pinNum[9] = {00, 02, 04, 05, 12, 13, 14, 15, 16};


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

void publishValues(){
  // publish RSSI to esp8266/chipNum/RSSI with retain flag set
  String WiFiRSSI = String(WiFi.RSSI());
  client.publish(rssi,WiFiRSSI.c_str(),"-r");
  delay(100);
  // Convert MAC Address to String & publish with retain flag set
  String WiFiMac = String(WiFi.macAddress());
  client.publish(mac,WiFiMac.c_str(),"-r");
  delay(100);
  // Convert IP Address to String & publish with retain flag set
  String WiFiAddr = WiFi.localIP().toString();
  client.publish(ipaddr,WiFiAddr.c_str(),"-r");
  delay(100);
}

void scanGPIO(){
  for (int i = 0; i < 9; i++){
    turnOffGPIO();
    digitalWrite(pinNum[i], HIGH); // Turn On GPIO
    Serial.printf("scanGPIO() is turning GPIO %d ON\n",pinNum[i]);
    delay(2000);
  }
}

void turnOffGPIO(){
  Serial.println("Turning OFF all GPIO");
  for (int i = 0; i < 9; i++){
    digitalWrite(pinNum[i], LOW); // Turn all outputs OFF
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Received ansi: ");
  Serial.println(*payload);
  if (*payload == 48){ // 48 = ansi 0
    Serial.println("Running scanGPIO()");
      scanGPIO();
  }else if (*payload == 49){ // 49 = ansi 1
      turnOffGPIO();
      digitalWrite(pinNum[0], HIGH); // Turn ON GPIO00
      Serial.println("GPIO00 is ON");
  }else if (*payload == 50){ // 50 = ansi 2
      turnOffGPIO();
      digitalWrite(pinNum[1], HIGH); // Turn ON GPIO2
      Serial.println("GPIO02 is ON, Blue LED may be off?");
  }else if (*payload == 51){ // 51 = ansi 3
      turnOffGPIO();
      digitalWrite(pinNum[2], HIGH); // Turn ON GPIO04
      Serial.println("GPIO04 is ON");
  }else if (*payload == 52){ // 52 = ansi 4
      turnOffGPIO();
      digitalWrite(pinNum[3], HIGH); // Turn ON GPIO05
      Serial.println("GPIO05 is ON");
  }else if (*payload == 53){ // 53 = ansi 5
      turnOffGPIO();
      digitalWrite(pinNum[4], HIGH); // Turn ON GPIO12
      Serial.println("GPIO12 is ON");
  }else if (*payload == 54){ // 54 = ansi 6
      turnOffGPIO();
      digitalWrite(pinNum[5], HIGH); // Turn ON GPIO13
      Serial.println("GPIO13 is ON");
  }else if (*payload == 55){ // 55 = ansi 7
      turnOffGPIO();
      digitalWrite(pinNum[6], HIGH); // Turn ON GPIO14
      Serial.println("GPIO14 is ON");
  }else if (*payload == 56){ // 56 = ansi 8
      turnOffGPIO();
      digitalWrite(pinNum[7], HIGH); // Turn ON GPIO15
      Serial.println("GPIO15 is ON");
  }else if (*payload == 57){ // 57 = ansi 9
      turnOffGPIO();
      digitalWrite(pinNum[8], HIGH); // Turn ON GPIO17
      Serial.println("GPIO16 is ON");
  }else{
      turnOffGPIO();
  }
  publishValues();
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

  for (int i = 0; i < 9; i++){ // Setup GPIO pins as Outputs
    pinMode(pinNum[i], OUTPUT);
    digitalWrite(pinNum[i], LOW); 
  }

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
