/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-rs485
 */

void setup() {
  // start communication with baud rate 9600
  Serial.begin(9600);

  // wait a moment to allow serial ports to initialize
  delay(100);
}

void loop() {
  // Check if there's data available on Serial
  if (Serial.available()) {
    char data = Serial.read();  // read the received character
    Serial.print(data);         // echo back to data to the sender
  }
}
