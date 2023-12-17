/* mqtt_da18b20_pico_b  2023.12.09
 *  Robin Greig
 *  Found the microDS18B20 library from Random Nerd Tutorials
 *  used dtosstrf to convert float to char
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

const char *topic = "pico-00/temp";  

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 


// initialize temp variable
float temperatureC = 0;
char tempTest [8];

void setup() { 

  Serial.begin(115200); // Start Serial Monitor
  
  WiFi.begin(ssid, password); // connecting to the WiFi network 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port); 

  while (!client.connected()) { 

      String client_id = "pico-00 > "; 

      client_id += String(WiFi.macAddress());

      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
      if (client.connect(client_id.c_str())) { 

          Serial.println("Mqtt broker connected"); 
          
      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(1000); 

      } 

  } 

}

 

void loop() { 

  client.loop();
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
  delay(50000);
}
