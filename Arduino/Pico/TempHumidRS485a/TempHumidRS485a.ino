/* 
 *  TempHumidRS485a.ino
 *  Robin Greig
 *  2025.02.15
 *  
 *  Reads the Temp & Humidity of RS485 device and prints it to Serial Monitor
 *  
 *  Based on the ModbusMaster example below
*/


#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial(1, 0); // RX, TX
 
// Create a ModbusMaster object
ModbusMaster node;
 
void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Initialize SoftwareSerial for Modbus communication
  mySerial.begin(9600);
 
  // Initialize Modbus communication with the Modbus slave ID 1
  node.begin(1, mySerial);
 
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
 
  // Wait for 2 seconds before the next read
  delay(5000);
}
