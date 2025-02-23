
#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial(7, 6); // RX, TX
 
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
    data[0] = node.getResponseBuffer(0x00); // Cardinal 0 - 7
    data[1] = node.getResponseBuffer(0x01); // Degrees 0 - 360
 
    // Calculate actual Cardinal & Degree values
    float cardinal = data[0];      // Cardinal
    float degrees = data[1];   // Temperature is scaled by 10
 
    // Print the values to the Serial Monitor
    Serial.print("Cardinal: ");
    Serial.print(cardinal);
    Serial.println("");
 
    Serial.print("Degrees: ");
    Serial.print((degrees/10));
    Serial.println(" °");
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result, HEX); // Print the error code in hexadecimal format
  }
 
  // Wait for 2 seconds before the next read
  delay(2000);
}
