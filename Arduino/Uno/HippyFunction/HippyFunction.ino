void ReadAndPrint(ModbusMaster node, char nodeNumber) {
  uint8_t result;   // Variable to store the result of Modbus operations
  uint16_t data[2]; // Array to store the data read from the Modbus slave
  float humidity;
  float temperature;

  // Read 2 holding registers for node starting at address 0x0000
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
    Serial.print("Humidity");
    Serial.print(nodeNumber);
    Serial.print(": ");
    Serial.print(humidity);
    Serial.println(" %RH");

    Serial.print("Temperature");
    Serial.print(nodeNumber);
    Serial.print(": ");
    Serial.print(temperature);
    Serial.println(" °C");
    Serial.println();
  } else {
    // Print an error message if the read fails
    Serial.print("Modbus read failed: ");
    Serial.println(result, HEX); // Print the error code in hexadecimal format
    Serial.println();
  }
  delay(200);
}
