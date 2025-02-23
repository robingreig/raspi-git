/* 
 *  TempHumidRS485_2.ino
 *  Robin Greig
 *  2025.02.17
 *  
 *  Reads the Temp & Humidity of RS485 device and prints it to Serial Monitor
 *  
 *  Using both UARTS to read 2 RS485 TTL inputs
 *  
 *  Based on the ModbusMaster example below
*/


#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial1(1, 0); // GPIO Rx, Tx
SoftwareSerial mySerial2(5, 4); // GPIO Rx, Tx
//SerialPIO mySerial3(8, 9); //GPIO Tx, Rx SoftwareSerial PIO-based UART

// Create a ModbusMaster object
ModbusMaster node1;
ModbusMaster node2;

float humidity1;
float humidity2;
float temperature1;
float temperature2;
 
void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Initialize SoftwareSerial for Modbus communication
  mySerial1.begin(9600);
  mySerial2.begin(9600);
 
  // Initialize Modbus communication with the Modbus slave ID 1
  node1.begin(1, mySerial1);
  node2.begin(1, mySerial2);
 
  // Allow some time for initialization
  delay(1000);
}
 
void loop() {
  uint8_t result1;   // Variable to store the result of Modbus operations
  uint16_t data1[2]; // Array to store the data read from the Modbus slave
  uint8_t result2;   // Variable to store the result of Modbus operations
  uint16_t data2[2]; // Array to store the data read from the Modbus slave
 
  // Read 2 holding registers for node1 starting at address 0x0000
  // This function sends a Modbus request to the slave to read the registers
  result1 = node1.readHoldingRegisters(0x0000, 2);
 
  // If the read is successful, process the data
  if (result1 == node1.ku8MBSuccess) {
    // Get the response data from the response buffer
    data1[0] = node1.getResponseBuffer(0x00); // Humidity
    data1[1] = node1.getResponseBuffer(0x01); // Temperature
 
    // Calculate actual humidity and temperature values
    humidity1 = data1[0] / 10.0;      // Humidity is scaled by 10
    temperature1 = data1[1] / 10.0;   // Temperature is scaled by 10
 
    // Print the values to the Serial Monitor
    Serial.print("Humidity1: ");
    Serial.print(humidity1);
    Serial.println(" %RH");
 
    Serial.print("Temperature1: ");
    Serial.print(temperature1);
    Serial.println(" °C");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result1, HEX); // Print the error code in hexadecimal format
  }
  delay(1000);
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
    temperature2 = data2[1] / 10.0;   // Temperature is scaled by 10
 
    // Print the values to the Serial Monitor
    Serial.print("Humidity2: ");
    Serial.print(humidity2);
    Serial.println(" %RH");
 
    Serial.print("Temperature2: ");
    Serial.print(temperature2);
    Serial.println(" °C");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result2, HEX); // Print the error code in hexadecimal format
    Serial.println();
  }
 
  // Wait for 2 seconds before the next read
  delay(5000);
}
