
#include <ModbusMaster.h>       //https://github.com/4-20ma/ModbusMaster
#include <SoftwareSerial.h>
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial(13, 02); // RX pin of RS-485, TX pin of RS-485
 
// Create a ModbusMaster object
ModbusMaster node;
 
void setup() {
  // Initialize serial communication for debugging
  Serial.begin(115200);
  // Initialize SoftwareSerial for Modbus communication
  mySerial.begin(4800);
 
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
    int cardinal = data[0];      // Cardinal
    float degrees = data[1];   // Temperature is scaled by 10
 
    // Print the values to the Serial Monitor
    Serial.print("Cardinal: ");
    Serial.print(cardinal);
    Serial.println("");
 
    Serial.print("Degrees: ");
    Serial.print(degrees);
    Serial.println(" °");
    switch (cardinal) {
            case 0:
              Serial.println("North");  //North
              break;
            case 1:
              Serial.println("North East"); //North-East
              break;
            case 2:
              Serial.println("East");  //East
              break;
            case 3:
              Serial.println("South East"); //South-East
              break;
            case 4:
              Serial.println("South");  //South
              break;
            case 5:
              Serial.println("South West"); //South-West
              break;
            case 6:
              Serial.println("West");  //West
              break;
            case 7:
              Serial.println("North West"); //North-West
              break;
            default:
              ("Invalid");   //invalid
          }
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result, HEX); // Print the error code in hexadecimal format
  }
 
  // Wait for 2 seconds before the next read
  delay(2000);
}
