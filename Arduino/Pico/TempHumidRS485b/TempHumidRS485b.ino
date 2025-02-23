/* 
 *  TempHumidRS485b.ino
 *  Robin Greig
 *  2025.02.15
 *  
 *  Reads the Temp & Humidity of RS485 device and prints it to Serial Monitor
 *  Adding mqtt connectivity
 *  
 *  Based on the ModbusMaster example below
*/


#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>

#include <WiFi.h> 
#include <PubSubClient.h>
#include <string.h>

// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial(1, 0); // RX, TX
 
// Create a ModbusMaster object
ModbusMaster node;

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.143"; 

const char *topic1 = "pico2w/00/temp";
const char *topic2 = "pico2w/00/humid";  

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

// initialize temp variable
float temperatureC = 0;
char temperatureChar [6];
float humidityRH = 0;
char humidityChar [6];

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Initialize SoftwareSerial for Modbus communication
  mySerial.begin(9600);
 
  // Initialize Modbus communication with the Modbus slave ID 1
  node.begin(1, mySerial);

  WiFi.begin(ssid, password); // connecting to the WiFi network 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port); 

  while (!client.connected()) { 

      String client_id = "pico2w-00 > "; 

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

 
  // Allow some time for initialization
  delay(1000);
}
 
void loop() {
  uint8_t result;   // Variable to store the result of Modbus operations
  uint16_t data[2]; // Array to store the data read from the Modbus slave
 
  // Read 2 holding registers starting at address 0x0000
  // This function sends a Modbus request to the slave to read the registers
  result = node.readHoldingRegisters(0x0000, 2);
 
  // If the read is successful, process the data
  if (result == node.ku8MBSuccess) {
    // Get the response data from the response buffer
    data[0] = node.getResponseBuffer(0x00); // Humidity
    data[1] = node.getResponseBuffer(0x01); // Temperature
 
    // Calculate actual humidity and temperature values
    float humidity = data[0] / 10.0;      // Humidity is scaled by 10
    float temperature = data[1] / 10.0;   // Temperature is scaled by 10
    temperatureC = temperature;
    humidityRH = humidity;
 
    // Print the values to the Serial Monitor
    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.println(" %RH");
 
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" °C");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result, HEX); // Print the error code in hexadecimal format
  }

  client.loop();
  //client.publish(topic, temperatureTest ); //publish temp 
  sprintf(temperatureChar,"%.2f", temperatureC);
  Serial.print("temperatureChar = ");
  Serial.println(temperatureChar);
  client.publish(topic1, temperatureChar); //publish temp
  sprintf(humidityChar,"%.2f",humidityRH);
  Serial.print("humidityRH = ");
  Serial.println(humidityChar);
  client.publish(topic2, humidityChar); 
  
  // Wait for 5 seconds before the next read
  delay(5000);
}
