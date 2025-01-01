/* mqtt_ds18b20_pico_a doesn't work
 *  mqtt_ds18b20_pico_b works with smaller onewire library
 */

#include <WiFi.h> 
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

// DS18B20

// GPIO where the DS18B20 is connected to
const int oneWireBus = 15;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.143"; 

const char *topic = "pico/00/temp";  

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 


// initialize temp variable
float temperatureC = 0;
char *temperatureTest = "-15.5";
 

void setup() { 

  Serial.begin(115200); // Start Serial Monitor
  
  sensors.begin(); // Start the DS18B20 sensor

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
  sensors.requestTemperatures();
  temperatureC = sensors.getTempCByIndex(0);
  Serial.print(temperatureC);
  Serial.println("ºC");
  client.publish(topic, temperatureTest ); //publish temp 
  sprintf(temperatureTest,"%.2f", temperatureC);
  client.publish(topic, temperatureTest ); //publish temp 
  delay(5000);
}
