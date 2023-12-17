/* mqtt_da18b20_pico_d  2023.12.09
 *  Robin Greig
 *  Found the microDS18B20 library from Random Nerd Tutorials
 *  used dtosstrf to convert float to char
 *  pico_b worked great with small delays, but broke with larger
 *  pico_c uses reconnect functions
 *  pico_d doesn't use deay, currentmillis
 */

#include <WiFi.h> 
#include <PubSubClient.h>
#include <microDS18B20.h>
#include <string.h>

// DS18B20

// GPIO where the DS18B20 is connected to
MicroDS18B20<22> sensor;

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

const char *topic = "pico/00/basementTemp";  

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values
//const long interval = 300000; // 5 minute interval at which to publish MQTT values
const long interval = 600000; // 10 minute interval at which to publish MQTT values
 


// initialize temp variable
float temperatureC = 0;
char tempTest [8];

void reconnectMQTT() {
  while (!client.connected()) { 
    String client_id = "pico-00 > "; 
    client_id += String(WiFi.macAddress());
    Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
    if (client.connect(client_id.c_str())) { 
        Serial.println("Mqtt broker connected"); 
    } else { 
        Serial.print("failed with state "); 
        Serial.print(client.state()); 
        delay(1000); 
    } 

  } 
}

void reconnectWiFi() {
  WiFi.begin(ssid, password); // connecting to the WiFi network 

  while (WiFi.status() != WL_CONNECTED) { 
    delay(500); 
    Serial.println("Connecting to WiFi.."); 
  } 
  Serial.println("Connected to the WiFi network");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void setup() { 

  client.setServer(mqtt_broker, mqtt_port);

  Serial.begin(115200); // Start Serial Monitor
  
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
  // Check to see if it is time to publish MQTT
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    sensor.requestTemp();
    delay(1000); // delay to read sample?
    temperatureC = sensor.getTemp();
    Serial.println("Printing temperatureC");
    Serial.print(temperatureC);
    Serial.println("ºC");
    dtostrf(temperatureC, 6, 2, tempTest);
    Serial.print("tempTest = ");
    Serial.println(tempTest);
    client.publish(topic, tempTest ); //publish temp
  }
}
