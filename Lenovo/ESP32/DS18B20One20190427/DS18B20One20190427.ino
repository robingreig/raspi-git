/*
 * Rui Santos 
 * Complete Project Details https://randomnerdtutorials.com
 */

// Include the libraries we need
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is connected to GPIO15
#define ONE_WIRE_BUS 15
// Setup a oneWire instance to communicate with a OneWire device
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

//DeviceAddress sensor1 = { 0x28, 0xFF, 0xA1, 0x58, 0x74, 0x16, 0x4, 0x24 };
DeviceAddress sensor1 = { 0x28, 0xCD, 0x2A, 0xF0, 0x2, 0x0, 0x0, 0xB0 };
//DeviceAddress sensor2 = { 0x28, 0xCD, 0x2A, 0xF0, 0x2, 0x0, 0x0, 0xB0 };
//DeviceAddress sensor3= { 0x28, 0xFF, 0xA0, 0x11, 0x33, 0x17, 0x3, 0x96 };

void setup(void){
  Serial.begin(115200);
  sensors.begin();
}

void loop(void){ 
  Serial.print("Requesting temperatures...");
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.println("DONE");
  
  Serial.print("Sensor 1(*C): ");
  Serial.print(sensors.getTempC(sensor1)); 
  Serial.print(" Sensor 1(*F): ");
  Serial.println(sensors.getTempF(sensor1)); 
 
//  Serial.print("Sensor 2(*C): ");
//  Serial.print(sensors.getTempC(sensor2)); 
//  Serial.print(" Sensor 2(*F): ");
//  Serial.println(sensors.getTempF(sensor2)); 
  
//  Serial.print("Sensor 3(*C): ");
//  Serial.print(sensors.getTempC(sensor3)); 
//  Serial.print(" Sensor 3(*F): ");
//  Serial.println(sensors.getTempF(sensor3)); 
  
  delay(2000);
}
