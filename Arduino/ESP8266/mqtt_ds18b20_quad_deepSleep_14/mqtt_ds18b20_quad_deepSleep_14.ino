/******************************************************************************
 *    Filename: mqtt_ds18b20_double_deepSleep_14                              *
 *    Version: 1.0                                                            *
 *    Date: 01 April 2024                                                     *
 *    Programmer: Robin Greig                                                 *
 *                                                                            *                                             
 *    Hardware: ESP8266 & 4 x DS18B20                                         *
 *    Connect via wireless to Calalta02                                       *
 *    Send RSSI to esp8266/14/RSSI                                            *
 *    > Send mac to esp8266/14/mac (not working)                              *              
 *    > For some reason if I don't put the const char *topic6 in there        *
 *    > Then the RSSI doesn't get sent via mqtt?                              *
 *    Send topic1 to esp8266/14/whiteTemp which is the White DS18B20          *                                            
 *    Send topic2 to esp8266/14/blueTemp which is the Blue DS18B20            *
 *    Send topic3 to esp8266/14/orangeTemp which is the Orange DS18B20        *                                            
 *    Send topic4 to esp8266/14/greenTemp which is the Green DS18B20          *
 *    And go into deepSleep for 1 minute                                      *
 *                                                                            *
 *    Setup DEBUG variable to print if > 0                                    *
 *                                                                            *
 *    To program disconnect GPIO16 from Reset                                 *                                                                        
 *    And reconnect to allow unit to wake up after deep sleep                 *
 *    DS18B20 is sending data via GPIO04                                      *
 *                                                                            *
 ******************************************************************************/


#include <ESP8266WiFi.h> 
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

// Set DEBUG Variable > 0 then print the Serial.println statements
const int DEBUG = 0;


// DS18B20

// GPIO where the DS18B20 is connected to
const int oneWireBus = 04;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqttServer = "192.168.200.21";

const int mqttPort = 1883;

const char *switch01 = "esp8266/14/GPIO";

const char *topic1 = "esp8266/14/whiteTemp";

const char *topic2 = "esp8266/14/blueTemp";

const char *topic3 = "esp8266/14/orangeTemp";

const char *topic4 = "esp8266/14/greenTemp";

const char *topic5 = "esp8266/14/RSSI";

const char *topic6 = "esp8266/14/mac";

WiFiClient espClient; 

PubSubClient client(espClient); 

// initialize temp variable
float temperatureC = 0;
char *tempChar = "00.00"; // temp needs to be char for mqtt
char strength[6]; // RSSI signal needs to be char for mqtt
char mac[18]; // mac address needs to be char for mqtt

void reconnectMQTT() {
  while (!client.connected()) {
    if (DEBUG > 0) {
      Serial.println("Connecting to MQTT...");
    }
    // Unique client ID (using ESP8266 macAddress)  
    String client_id = "esp8266-";
    client_id += String(WiFi.macAddress());
    if (DEBUG > 0) {
      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
    }
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect(client_id.c_str())) {
      if (DEBUG > 0) {
        Serial.printf("The client %s is connected to MQTT\n", client_id.c_str());
      }
      String WiFiRSSI = String(WiFi.RSSI());
      if (DEBUG > 0) {
        Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      }
      strcpy(strength, WiFiRSSI.c_str());
      if (DEBUG > 0) {
        Serial.printf("strength = %s\n",strength);
      }
      client.subscribe(switch01); // subscribe to mqtt topic
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
    if (DEBUG > 0) {
      Serial.println("Connecting to WiFi..");
    }
  }
  if (DEBUG > 0) {
    Serial.println("Connected to the WiFi network");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
  }
}

void setup() { 
  
  Serial.begin(115200); // Start Serial Monitor
  
  sensors.begin(); // Start the DS18B20 sensor

  client.setServer(mqttServer, mqttPort);

  //client.setCallback(callback);

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

  client.loop();
  sensors.requestTemperatures();
  temperatureC = sensors.getTempCByIndex(0);
  sprintf(tempChar,"%.2f", temperatureC);
  if (DEBUG > 0) {
  Serial.printf("Published topic1 value of %.2fºC to whiteTemp from White DS18B20: %s\n", temperatureC, topic1);
  Serial.println();
  }
  client.publish(topic1, tempChar,"-r"); //publish temp
  delay(1000);
  temperatureC = sensors.getTempCByIndex(1);
  sprintf(tempChar,"%.2f", temperatureC);
  if (DEBUG > 0) {
  Serial.printf("Published topic2 value of %.2fºC to blueTemp from Blue DS18B20: %s\n", temperatureC, topic2);
  Serial.println();
  }
  client.publish(topic2, tempChar,"-r"); //publish temp
  delay(1000);  
  temperatureC = sensors.getTempCByIndex(2);
  sprintf(tempChar,"%.2f", temperatureC);
  if (DEBUG > 0) {
  Serial.printf("Published topic3 value of %.2fºC to orangeTemp from Orange DS18B20: %s\n", temperatureC, topic3);
  Serial.println();
  }
  client.publish(topic3, tempChar,"-r"); //publish temp
  delay(1000);
  temperatureC = sensors.getTempCByIndex(3);
  sprintf(tempChar,"%.2f", temperatureC);
  if (DEBUG > 0) {
  Serial.printf("Published topic4 value of %.2fºC to greenTemp from Green DS18B20: %s\n", temperatureC, topic4);
  Serial.println();
  }
  client.publish(topic4, tempChar,"-r"); //publish temp
  delay(1000);
  if (DEBUG > 0) {
  Serial.printf("Published RSSI to: %s\n",topic5);
  Serial.println();
  delay(5000);
  }
  client.publish(topic5, strength,"-r"); // publish RSSI
  delay(1000);
  Serial.println("Going to sleep for 1 minute / 60 seconds");
  ESP.deepSleep(60e6);
//  Serial.println("Going to sleep for 1.5 minutes / 90 seconds");
//  ESP.deepSleep(90e6);
//  Serial.println("Going to sleep for 2 minutes / 120 seconds");
//  ESP.deepSleep(120e6);
//  Serial.println("Going to sleep for 3 minutes / 180 seconds");
//  ESP.deepSleep(180e6);
//  Serial.println("Going to sleep for 5 minutes / 300 seconds");
//  ESP.deepSleep(300e6);
}
