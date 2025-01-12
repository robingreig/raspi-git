
/*****
 * bme280_pico_b from Random Nerd Tutorials who got it from Adafruit
 * Measure Temperature, Air Pressure & humidity and post to mqtt
 * Print Values
 * Robin Greig
 * 2025.01.05 
 ******/

#include <WiFi.h> 
#include <PubSubClient.h>
#include <microDS18B20.h>
#include <string.h>

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

/*#include <SPI.h>
#define BME_SCK 18
#define BME_MISO 19
#define BME_MOSI 23
#define BME_CS 5*/

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C (default pins for Raspberry Pi Pico: GPIO 4 (SDA), GPIO 5(SCL)
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.143"; 

const char *topic = "pico/00/basementTemp";  //

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 


unsigned long delayTime;
unsigned long previousMillis = 0; // will store last time MQTT published
const long interval = 5000; // 5 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values
//const long interval = 300000; // 5 minute interval at which to publish MQTT values
//const long interval = 600000; // 10 minute interval at which to publish MQTT values

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
  Serial.begin(115200);
  
  client.setServer(mqtt_broker, mqtt_port);  

  bool status;

  // default settings
  // (you can also pass in a Wire library object like &Wire2)
  status = bme.begin(0x76);  
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  delayTime = 5000;

  Serial.println();
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

    Serial.print("Temperature = ");
    Serial.print(bme.readTemperature());
    Serial.println(" *C");
    

//  printValues();
  }
}

/*void printValues() {
  Serial.print("Temperature = ");
  Serial.print(bme.readTemperature());
  Serial.println(" *C");
  
  // Convert temperature to Fahrenheit
  /*Serial.print("Temperature = ");
  Serial.print(1.8 * bme.readTemperature() + 32);
  Serial.println(" *F");*/
  
/*  Serial.print("Pressure = ");
  Serial.print(bme.readPressure() / 100.0F);
  Serial.println(" hPa");

  Serial.print("Approx. Altitude = ");
  Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.println(" m");

  Serial.print("Humidity = ");
  Serial.print(bme.readHumidity());
  Serial.println(" %");

  Serial.println();
}
*/
