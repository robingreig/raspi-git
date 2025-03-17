/* 
 *  TempHumidRS485d_mqtt.ino
 *  Robin Greig
 *  2025.03.16
 *  
 *  For Pico 2 W (Pico02)
 *  
 *  Reads the Temp & Humidity of 2 RS485 devices and prints it to Serial Monitor & mqtt
 *  
 *  Based on the ModbusMaster example from websit below
 *  
 *  2025.03.16
 *  Working using Hippy's suggestion for function from Raspberry Pi Forum
 *  https://forums.raspberrypi.com/search.php?author_id=40310&sr=posts
 *  
 *  Getting humidity & temperature out of the function into individual variables
 *  
*/


#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>

#include <WiFi.h> 
#include <PubSubClient.h>
#include <string.h>
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial1(1, 0); // RX, TX of Pico 2 W
SoftwareSerial mySerial2(5, 4); // GPIO Rx, Tx of Pico 2 W
//SerialPIO mySerial3(8, 9); //GPIO Tx, Rx SoftwareSerial PIO-based UART
 
// Create a ModbusMaster object
ModbusMaster node1;
ModbusMaster node2;

// WiFi 
const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 
const char *mqtt_broker = "192.168.200.143"; 
const int mqtt_port = 1883; 

// MQTT Topics
const char *topic1 = "pico2w/02/temp1";
const char *topic2 = "pico2w/02/humid1";  
const char *topic3 = "pico2w/02/temp2";
const char *topic4 = "pico2w/02/humid2";
const char *rssi = "pico2w/00/RSSI";  

// Temp & Humid Variables
// floats for the tempHumid function
// chars to send via mqtt
float humid1F;
char humid1C[8];
float temp1F;
char temp1C[8];
float humid2F;
char humid2C[8];
float temp2F;
char temp2C[8];

// DEBUG > 0 Serial.print lines
int DEBUG = 0;

WiFiClient espClient; 

PubSubClient client(espClient);

void reconnectMQTT() {
  while (!client.connected()) {
    if (DEBUG > 0) {
      Serial.println("Connecting to MQTT...");      
    }
    // Unique client ID (using ESP8266 macAddress)  
    String client_id = "pico2w-02-";
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
      client.publish(rssi,WiFiRSSI.c_str(),"-r"); // retain flag set
      if (DEBUG > 0) {
        Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str()); 
      }
    } else {
      if (DEBUG > 0) {
        Serial.print("failed with state ");
        Serial.println(client.state());
        delay(500);  
      }
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

// function to measure temp & humid from various sensors
// Send it pointer to the variable *humidP
// Send it pointer to the variable *tempP

void tempHumid (ModbusMaster node, float *humidP, float *tempP)
  {
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
      *humidP = data[0] / 10.0;      // Humidity is scaled by 10
      *tempP = data[1] / 10.0;   // Temperature is scaled by 10
    } else {
      // Print an error message if the read fails
      Serial.print("Modbus read failed: ");
      Serial.println(result, HEX); // Print the error code in hexadecimal format
    }
}

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  
  // Initialize SoftwareSerial for Modbus communication
  mySerial1.begin(9600);
  mySerial2.begin(9600);
 
  // Initialize Modbus communication with the Modbus slave ID 1
  node1.begin(1, mySerial1);
  node2.begin(1, mySerial2);

  // Setup mqtt
  client.setServer(mqtt_broker, mqtt_port);
  
  // Allow some time for initialization
  delay(1000);
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
  tempHumid(node1, &humid1F, &temp1F);
  if (DEBUG > 0) {
    Serial.print("Temperature 1 Returned from pointer= ");
    Serial.println(temp1F);
    Serial.println();
  }
  dtostrf(temp1F, 6, 2, temp1C); // convert temp1F float to temp1C char
  client.publish(topic1, temp1C, "-r"); // publish temp1  
  if (DEBUG > 0) {
    Serial.print("Humidity 1 Returned from pointer= ");
    Serial.println(humid1F);
    Serial.println();
  }
  dtostrf(humid1F, 6, 2, humid1C); // convert humid1F float to humid1C char 
  client.publish(topic2, humid1C, "-r"); // publish humid 1
  tempHumid(node2, &humid2F, &temp2F);
  if (DEBUG > 0) {
    Serial.print("Temperature 2 Returned from pointer= ");
    Serial.println(temp2F);
    Serial.println();
  }
  dtostrf(temp2F, 6, 2, temp2C); // convert temp2F float to temp2C char
  client.publish(topic3, temp2C, "-r"); // publish temp2
  if (DEBUG > 0) {
    Serial.print("Humidity 2 Returned from pointer= ");
    Serial.println(humid2F);
    Serial.println(); 
  }
  dtostrf(humid2F, 6, 2, humid2C); // convert temp2F float to temp2C char
  client.publish(topic4, humid2C, "-r"); // publish temp2
    
  // Wait for 5 seconds before the next read
  delay(5000);
}
