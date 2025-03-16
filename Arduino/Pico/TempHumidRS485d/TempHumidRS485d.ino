/* 
 *  TempHumidRS485d.ino
 *  Robin Greig
 *  2025.03.16
 *  
 *  Reads the Temp & Humidity of multiple RS485 devicesnd prints it to Serial Monitor
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
 
// Create a SoftwareSerial object to communicate with the MAX485 module
SoftwareSerial mySerial1(1, 0); // RX, TX of Pico 2 W
SoftwareSerial mySerial2(5, 4); // GPIO Rx, Tx of Pico 2 W
//SerialPIO mySerial3(8, 9); //GPIO Tx, Rx SoftwareSerial PIO-based UART
 
// Create a ModbusMaster object
ModbusMaster node1;
ModbusMaster node2;
 
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
void loop() {
  float humid1;
  float temp1;
  float humid2;
  float temp2;
  tempHumid(node1, &humid1, &temp1);
  Serial.print("Humidity 1 Returned from pointer= ");
  Serial.println(humid1);
  Serial.println();
  Serial.print("Temperature 1 Returned from pointer= ");
  Serial.println(temp1);
  Serial.println();
  tempHumid(node2, &humid2, &temp2);
  Serial.print("Humidity 2 Returned from pointer= ");
  Serial.println(humid2);
  Serial.println();
  Serial.print("Temperature 2 Returned from pointer= ");
  Serial.println(temp2);
  Serial.println();
  // Wait for 2 seconds before the next read
  delay(5000);
}
