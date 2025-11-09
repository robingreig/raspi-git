/* 
 *  TempHumidWindRS485_1b.ino
 *  Robin
 *  2025.09.30
 *  
 *  Reads the RS485 data and prints it to the Serial Monitor
 *  
 *  Using both UARTS and PIO-based UART to read 3 RS485 > TTL inputs
 *  mySerial1 = Rx / Pin 2 / GPIO 1 & Tx / Pin 1 / GPIO 0 = Anemometer at 4800 Baud
 *  mySerial2 = Rx / Pin 7 / GPIO 5 & Tx / Pin 6 / GPIO 4 = Wind Vane at 4800 baud
 *  mySerial3 = SerialPIO = Tx / Pin 11 / GPIO 8 & Rx / Pin 12 / GPIO 9 = TempHumid at 9600 Baud
 *  
 *  Addint mqtt connectivity
 *  
 *  Based on the ModbusMaster example below
*/

#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>

#include <WiFi.h> 
#include <PubSubClient.h>
#include <string.h>

// Create a SoftwareSerial object to communicate with the MAX485 module
// MySereial1 is connected to the Anemometer
SoftwareSerial mySerial1(1, 0); // Rx-Pin 2-GPIO 1 & Tx-Pin 1-GPIO 0
// MySerial2 is connected to the wind vane
SoftwareSerial mySerial2(5, 4); // Rx-Pin 7-GPIO 5 & Tx-Pin 6-GPIO 4
// MySerial3 is connected to the TempHumid sensor
SerialPIO mySerial3(8, 9); // Tx-GPIO 8-Pin 11 & Rx-GPIO 12-Pin 10
//for SoftwareSerial PIO-based UART

// Create a ModbusMaster object
ModbusMaster node1;
ModbusMaster node2;
ModbusMaster node3;

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.143"; 

const char *topic1 = "pico2w/02/speed1";
const char *topic2 = "pico2w/02/speed2";  
const char *topic3 = "pico2w/02/temp2";
const char *topic4 = "pico2w/02/humid2";  
const char *topic5 = "pico2w/02/temp3";
const char *topic6 = "pico2w/02/humid3";  

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

float humidity1;
char humidChar1 [6];
float humidity2;
char humidChar2 [6];
float humidity3;
char humidChar3 [6];
float temperature1;
char tempChar1 [6];
float temperature2;
char tempChar2 [6];
float temperature3;
char tempChar3 [6];

void setup() {

  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Initialize SoftwareSerial for Modbus communication
  mySerial1.begin(4800);
  mySerial2.begin(4800);
  mySerial3.begin(9600);
 
  // Initialize Modbus communication with the Modbus slave ID 1
  node1.begin(1, mySerial1);
  node2.begin(1, mySerial2);
  node3.begin(1, mySerial3);

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
          Serial.println();
          
      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(1000); 

      } 
 
  // Allow some time for initialization
  delay(500);
  }
} 
void loop() {
  uint8_t result1;   // Variable to store the result of Modbus operations
  uint16_t data1[2]; // Array to store the data read from the Modbus slave
  uint8_t result2;   // Variable to store the result of Modbus operations
  uint16_t data2[2]; // Array to store the data read from the Modbus slave
  uint8_t result3;   // Variable to store the result of Modbus operations
  uint16_t data3[2]; // Array to store the data read from the Modbus slave
 
  // Read 2 holding registers for node1 starting at address 0x0000
  // This function sends a Modbus request to the slave to read the registers
//  result1 = node1.readHoldingRegisters(0x0000, 2);
  result1 = node1.readHoldingRegisters(0x0000, 2);
 
  // If the read is successful, process the data
  if (result1 == node1.ku8MBSuccess) {
    // Get the response data from the response buffer
    data1[0] = node1.getResponseBuffer(0x00); // Wind Speed
    data1[1] = node1.getResponseBuffer(0x01); // ?????
 
    // Calculate actual humidity and temperature values
    humidity1 = data1[0] / 10.0;      // Wind Speed is scaled by 10
    temperature1 = data1[1] / 10.0;   // ?????
 
    // Print the values to the Serial Monitor
    Serial.print("Wind Speed: ");
    Serial.print(humidity1);
    Serial.print(" m/s or ");
    Serial.print(humidity1*3.6);
    Serial.println(" km/hr");
    Serial.println();
 
    //Serial.print("Temperature1: ");
    //Serial.print(temperature1);
    //Serial.println(" °C");
    //Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result1, HEX); // Print the error code in hexadecimal format
    Serial.println();
  }
  delay(200);
  // Read 2 holding registers for node2 starting at address 0x0000
  // This function sends a Modbus request to the slave to read the registers
  result2 = node2.readHoldingRegisters(0x0000, 2);
 
  // If the read is successful, process the data
  if (result2 == node2.ku8MBSuccess) {
    // Get the response data from the response buffer
    data2[0] = node2.getResponseBuffer(0x00); // Humidity
    data2[1] = node2.getResponseBuffer(0x01); // Temperature
 
    // Calculate actual humidity and temperature values
    humidity2 = data2[0] / 10.0;      // Humidity is scaled by 10
    temperature2 = data2[1] ;   // Don't scale wind direction 0 - 360 degrees
 
    // Print the values to the Serial Monitor
    //Serial.print("Humidity2: ");
    //Serial.print(humidity2);
    //Serial.println(" %RH");
 
    Serial.print("Wind Direction: ");
    Serial.print(temperature2);
    Serial.println(" °");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result2, HEX); // Print the error code in hexadecimal format
    Serial.println();
  }
  delay(200);
  // Read 2 holding registers for node3 starting at address 0x0000
  // This function sends a Modbus request to the slave to read the registers
  result3 = node3.readHoldingRegisters(0x0000, 2);
 
  // If the read is successful, process the data
  if (result3 == node3.ku8MBSuccess) {
    // Get the response data from the response buffer
    data3[0] = node3.getResponseBuffer(0x00); // Humidity
    data3[1] = node3.getResponseBuffer(0x01); // Temperature
 
    // Calculate actual humidity and temperature values
    humidity3 = data3[0] / 10.0;      // Humidity is scaled by 10
    temperature3 = data3[1] / 10.0;   // Temperature is scaled by 10
 
    // Print the values to the Serial Monitor
    Serial.print("Humidity3: ");
    Serial.print(humidity3);
    Serial.println(" %RH");
 
    Serial.print("Temperature3: ");
    Serial.print(temperature3);
    Serial.println(" °C");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result3, HEX); // Print the error code in hexadecimal format
    Serial.println();
  }

  client.loop();
  //sprintf(tempChar1,"%.2f", temperature1);
  //Serial.print("tempChar1 = ");
  //Serial.println(tempChar1);
  //client.publish(topic1, tempChar1); //publish temp
  sprintf(humidChar1,"%.2f",humidity1);
  Serial.print("Wind Speed in m/s = ");
  Serial.println(humidChar1);
  client.publish(topic2, humidChar1); 
  Serial.println();

  sprintf(tempChar2,"%.2f", temperature2);
  Serial.print("Wind Direction = ");
  Serial.println(tempChar2);
  client.publish(topic3, tempChar2); //publish wind direction
  Serial.println();
  //sprintf(humidChar2,"%.2f",humidity2);
  //Serial.print("humidChar2 = ");
  //Serial.println(humidChar2);
  //client.publish(topic4, humidChar2); 

  sprintf(tempChar3,"%.2f", temperature3);
  Serial.print("tempChar3 = ");
  Serial.println(tempChar3);
  client.publish(topic5, tempChar3); //publish temp
  sprintf(humidChar3,"%.2f",humidity3);
  Serial.print("humidChar3 = ");
  Serial.println(humidChar3);
  Serial.println();
  client.publish(topic6, humidChar3); 

  // Wait before the next read
  //delay(1000);
  //delay(2000);
  delay(5000);
}
