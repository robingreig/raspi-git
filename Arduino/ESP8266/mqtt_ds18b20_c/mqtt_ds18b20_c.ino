#include <ESP8266WiFi.h> 
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

// DS18B20

// GPIO where the DS18B20 is connected to
const int oneWireBus = 13;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

//const char *topic1 = "temp/outside";
const char *topic1 = "test/outside";

//const char *topic2 = "esp8266/RSSI";
const char *topic2 = "test/RSSI";

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

// LED to turn on when connected
#define LED 2

// initialize temp variable
float temperatureC = 0;
char *temperatureChar = "00.00";
char signal[6]; 

void setup() { 

  Serial.begin(115200); // Start Serial Monitor
  
  sensors.begin(); // Start the DS18B20 sensor

  pinMode(LED, OUTPUT); // setup onboard LED as output

  WiFi.begin(ssid, password); // connecting to the WiFi network 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 
  // turn on onboard led
  digitalWrite(LED, HIGH);

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port); 

  while (!client.connected()) { 

      String client_id = "esp8266-00 > "; 

      String WiFiRSSI = String(WiFi.RSSI());

      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());

      strcpy(signal, WiFiRSSI.c_str());

      client_id += String(WiFi.macAddress());

      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 

//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
      if (client.connect(client_id.c_str())) { 

          Serial.println("Mqtt broker connected"); 
          digitalWrite(LED, HIGH);
          
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
  sprintf(temperatureChar,"%.2f", temperatureC);
  client.publish(topic1, temperatureChar); //publish temp
  client.publish(topic2, signal); // publish RSSI
  delay(5000);
}
