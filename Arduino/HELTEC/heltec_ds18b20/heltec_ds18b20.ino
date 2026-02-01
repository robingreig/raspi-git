#include <Arduino.h>
#include <heltec.h>

#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 13 on the Arduino
//#define ONE_WIRE_BUS 13

//OneWire oneWire(ONE_WIRE_BUS);
OneWire ds(33);
DallasTemperature sensors(&ds);

//DallasTemperature sensors(&oneWire);

void setup() {
// Start the Serial Monitor
delay(2000);
Serial.begin(9600);
Serial.println(“Serial begins”);
// Start the DS18B20 sensor
sensors.begin();

sensors.requestTemperatures();
float Temperature = (float)(sensors.getTempCByIndex(0));
float temperatureC = sensors.getTempCByIndex(0);
float temperatureF = sensors.getTempFByIndex(0);
Serial.print(Temperature);
Serial.println(“ºC”);
Serial.print(temperatureF);
Serial.println(“ºF”);

//Serial.println(“Go to sleep”);
esp_deep_sleep(30e6);
}

void loop() {
}
