/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-rs485
 */

#include <SoftwareSerial.h>

// define the SoftwareSerial object and their pins
SoftwareSerial rs485(6, 7);  // RX: 6, TX: 7

void setup() {
  // start communication with baud rate 9600
  rs485.begin(9600);
  Serial.begin(115200);

  // wait a moment to allow serial ports to initialize
  delay(100);
}

void loop() {
  // Check if there's data available on rs485
  if (rs485.available()) {
    char data = rs485.read();  // read the received character
//    rs485.print(data);         // echo back to data to the sender
    Serial.println(data);         // echo back to data to the sender
  }
}
