/*********
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ds18b20-arduino/
  
  Example adapted from the microDS18B20 library examples folder - microSD18B20 library: https://github.com/GyverLibs/microDS18B20
*********/

#include <microDS18B20.h>
#include <SoftwareSerial.h>


// We're using GPIO 22, change accordingly
MicroDS18B20<15> sensor;
SoftwareSerial mySerial (1, 0);

void setup() {
  Serial.begin(115200);
  mySerial.begin(115200);
}

void loop() {
  //request temperature from sensor
  sensor.requestTemp();

  delay(2000);
  
  //print the temperature
  Serial.print("Temperature from Serial (ºC): ");
  Serial.println(sensor.getTemp());
  mySerial.print("Temperature from mySerial (ºC): ");
  mySerial.println(sensor.getTemp());


}
