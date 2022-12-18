#include <ESP8266WiFi.h> 
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

// DS18B20

// GPIO where the DS18B20's are connected to
const int oneWireBus = 04;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// Identify each DS18B20 sensor
uint8_t BlueSensor[8] = {0x28, 0xFF, 0x64, 0x02, 0xF5, 0x8D, 0x3B, 0xC1};
uint8_t BrownSensor[8] = {0x28, 0xFF, 0x0E, 0x84, 0x74, 0x16, 0x03, 0xE8};
uint8_t GreenRedSensor[8] = {0x28, 0xFF, 0x64, 0x02, 0xE8, 0x58, 0xE8, 0x89};
uint8_t RedGreenSensor[8] = {0x28, 0xFF, 0x64, 0x02, 0xF5, 0xB1, 0x1A, 0xDC};
uint8_t SilverSensor[8] = {0x28, 0xFF, 0x64, 0x02, 0xEB, 0xED, 0xAC, 0xB7};


// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

const char *topic1 = "temp/outTemp";

const char *topic2 = "temp/battTemp";

const char *topic3 = "esp8266/RSSI";

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

// LED to turn on when connected
#define LED 2

// initialize temp variable
float tempSensor1 = 0;
float tempSensor2 = 0;
char *tempChar = "00.00"; // temp needs to be char for mqtt
char rssi[6]; // RSSI signal needs to be char for mqtt

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

      String client_id = "esp8266-"; 

      String WiFiRSSI = String(WiFi.RSSI());

      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());

      strcpy(rssi, WiFiRSSI.c_str());

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
  while(!Serial) {}
  client.loop();
  sensors.requestTemperatures(); // request temps
  tempSensor1 = sensors.getTempC(SilverSensor); // get BrownSensor temp
  sprintf(tempChar, "%.2f", tempSensor1); //convert float tempSensor1 to char for tempChar
  client.publish(topic1, tempChar); //publish temp
  Serial.printf("Published Temp of %.2fºC to: %s\n",tempSensor1, topic1); //print temp
  delay(5000);
  tempSensor2 = sensors.getTempC(GreenRedSensor); //get BlueSensor temp
  sprintf(tempChar, "%.2f", tempSensor2); // convert float tempSensor2 to char tempChar
  client.publish(topic2, tempChar); //publish temp
  Serial.printf("Published Temp of %.2fºC to: %s\n",tempSensor2, topic2); //print temp
  delay(5000);
  client.publish(topic3, rssi); // publish RSSI
  Serial.printf("Published RSSI of %s to: %s\n",rssi, topic3);
  delay(5000);
  Serial.println("Going to sleep for 60 seconds");
  ESP.deepSleep(60e6);
}
