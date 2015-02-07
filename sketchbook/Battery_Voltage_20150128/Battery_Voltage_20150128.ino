/*
  Parts of this were copied from:
  Analog input, analog output, serial output
  by Tom Igoe
  
  The rest was written by Robin Greig
  2015.01.02
  
  Reads an analog input pin, maps the result to a range from 0 to 255
  and uses the result to set the pulsewidth modulation (PWM) of an output pin.
  Also outputs the results to the serial port.
 
  The circuit:
  * potentiometer connected to analog pin 0.
    Center pin of the potentiometer goes to the analog pin.
    side pins of the potentiometer go to +5V and ground
  * PWM LED connected on pin 9 (Gertduino D6)
  * Battery Low Indicator LED on pin 13 (Gertduino D5)
  
  */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to
const int lowVoltLED = 13; // UnderVoltage LED on pin 13 (Gertduino D5)
const float battVoltMinRange = 11.00; // Minimum range of battery voltage
const float battVoltMaxRange = 15.7; // Maximum range of battery voltage
const float battVoltMinValue = 11.8; // Minimum battery voltage for undervoltag led

int sensorValue = 0; // value read from the pot
int outputValue = 0; // value output to the PWM (analog out)
float battVoltNow = 0; // last read value of battery voltage
float battVoltAvg = battVoltMinValue; // average battery voltage starts at min
boolean battVoltPrint = false; // if we received a serial request
boolean outputValuePrint = false; // if we received a serial request
boolean sensorValuePrint = false; // if we received a serial request

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(lowVoltLED, OUTPUT);  
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  analogWrite(analogOutPin, outputValue); 
  // calculate the battery voltage within the range of 11 - 15 V
  battVoltNow = (sensorValue - 0) * (battVoltMaxRange - battVoltMinRange) / (1023 - 0) + battVoltMinRange;
  //battVoltNow = ((sensorValue * .00488759) + 9.46);
  //battVoltNow = ((sensorValue * .00488759) + 11);
  battVoltAvg = ((battVoltAvg + battVoltNow) / 2);
  
  // if the result is below 12.9 v, then turn LowVoltageLED on
  if (battVoltAvg <= 11.5) {
    digitalWrite(lowVoltLED, HIGH);
  } else if (battVoltAvg > 11.6) {
    digitalWrite(lowVoltLED, LOW);
  }
  if (battVoltPrint) {
    Serial.print("Battery Voltage Avg = "); // print the results to the serial monitor:
    Serial.println(battVoltAvg); // print the results to the serial monitor:
    Serial.print("Battery Voltage Avg = "); // print the results to the serial monitor:
    Serial.println(battVoltAvg); // print the results to the serial monitor:
    battVoltPrint = false;
  } else if (sensorValuePrint) {
    Serial.print("Sensor Value = "); // print the results to the serial monitor:
    Serial.println(sensorValue); // print the results to the serial monitor:
    sensorValuePrint = false;
  } else if (outputValuePrint) {
    Serial.print("Output Value ="); // print the results to the serial monitor:
    Serial.println(outputValue); // print the results to the serial monitor:
    outputValuePrint = false;
  }
  // wait 20 milliseconds before repeating loop 
  delay(20);
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte
    char inChar = (char)Serial.read();
    // if the incoming character is a top hat, set a flag
    // so that the main loop will print the battery voltage
    if (inChar == '^') {
      battVoltPrint = true;
    } else if (inChar == '~') {
      sensorValuePrint = true;
    } else if (inChar == '+') {
      outputValuePrint = true;
    }
  }
}  
