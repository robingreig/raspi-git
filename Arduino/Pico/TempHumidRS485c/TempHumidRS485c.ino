/* 
 *  TempHumidRS485c.ino
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

// char variable for node input
int nodeNumber;

void tempHumid (ModbusMaster node, int nodeNumber)
  {
    uint8_t result;   // Variable to store the result of Modbus operations
    uint16_t data[2]; // Array to store the data read from the Modbus slave
    float humidity;
    float temperature;
 
    // Read 2 holding registers starting at address 0x0000
    // This function sends a Modbus request to the slave to read the registers
    result = node.readHoldingRegisters(0x0000, 2);
 
    // If the read is successful, process the data
    if (result == node.ku8MBSuccess) {
      // Get the response data from the response buffer
      data[0] = node.getResponseBuffer(0x00); // Humidity
      data[1] = node.getResponseBuffer(0x01); // Temperature
 
      // Calculate actual humidity and temperature values
      humidity = data[0] / 10.0;      // Humidity is scaled by 10
      temperature = data[1] / 10.0;   // Temperature is scaled by 10
     
      // Print the values to the Serial Monitor
      Serial.println();
      Serial.print("Humidity ");
      Serial.print(nodeNumber);
      Serial.print(": ");
      Serial.print(humidity);
      Serial.println(" %RH");
 
      Serial.print("Temperature ");
      Serial.print(nodeNumber);
      Serial.print(": ");
      Serial.print(temperature);
      Serial.println(" °C");
      Serial.println();
    } else {
      // Print an error message if the read fails
      Serial.print("Modbus read failed: ");
      Serial.println(result, HEX); // Print the error code in hexadecimal format
    }
}
void loop() {
  tempHumid(node1, 1);
  tempHumid(node2, 2);
  // Wait for 2 seconds before the next read
  delay(5000);
}
