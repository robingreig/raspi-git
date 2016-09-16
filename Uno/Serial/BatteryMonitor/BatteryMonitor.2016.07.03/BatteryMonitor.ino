/* Battery Monitor 2016.07.03
   Pins 3, 5, 6, 9, 10, & 13 display the voltage level of the battery when button 2 is pushed  
   Pin 4  will turn the battery charger on
   Pin 7 controls the Raspi (Pin 7 on, Raspi on)
*/

const int analogInTable[7]= {A0,A1,A2,A3,A4,A5,A6};
int Sw1 = 2; // Switch 1 is port 2 
int readSw1 = 0; // value of switch 1
int Pin4 = 4; // Pin 4
int readPin4 = 0; //value of Pin4
int Pin7 = 7; // Pin 7
int readPin7 = 0; //value of Pin7
//float zener = 9.56; // Zener Voltage Drop //Actual measured, but calculated still too high
//float zener = 9.4; // Zener Voltage Drop
float zener = 9.15; // Zener Voltage Drop
float multiplier = 5.00; //*** Calculated is still a little high (11.72 vs 11.51) 
//float multiplier = 4.90; //***  *** Multiplier to set digital to analog steps
//float multiplier = 4.80; //***  *** Multiplier to set digital to analog steps
//float multiplier = 4.70; //***  Calculated is still a little high (12.96 vs 13.2) 
//float multiplier = 4.60; //***  *** Multiplier to set digital to analog steps
const int debug = 1; // If debug > 0 then the extra lines are printed
char inChar;

void sendAnalogValue(byte Channel)
{
  int valueAD;
  float SensorAnalog;
  float BattVolt;
  valueAD = analogRead(analogInTable[Channel]);
  if (analogInTable[Channel] == 20) {
    valueAD = analogRead(A0);
    Serial.print("AnalogInTable[Channel]: ");
    Serial.println(analogInTable[Channel]);
    Serial.print("valueAD: ");
    Serial.println (valueAD);
    Serial.print("multiplier: analog > digital: ");
    Serial.println(multiplier);
    SensorAnalog = (valueAD * (multiplier/1023.0)); // 0-5 V
    Serial.print("SensorAnalog (valueAT * (multiplier/1023)): ");
    Serial.println (SensorAnalog);
    Serial.print("Zener Voltage: ");
    Serial.println (zener);
    BattVolt = (SensorAnalog + zener); // Send back Calculated Battery Voltage
    Serial.print("Calculated Battery Voltage (SensorAnalog + zener): ");
    Serial.println(BattVolt);
    readPin4 = digitalRead(Pin4); // assign value of pin 4
    Serial.print("Pin 4 / Battery Charger (High = charge): "); 
    Serial.println(readPin4); 
    readPin4 = digitalRead(Pin7); // assign value of pin 7
    Serial.print("Pin 7 / Raspi power (Low = power on): "); 
    Serial.println(readPin7); 
    Serial.println(); 
  } else {
    SensorAnalog = (valueAD * (multiplier/1023.0)); // 0-5 V
    //BattVolt = ((valueAD * (multiplier/1023.0))+zener); // Send back Calculated Battery Voltage
    BattVolt = (SensorAnalog + zener); // Send back Calculated Battery Voltage
  if (BattVolt <= 9.6){
    BattVolt = 0;
  }
  Serial.println(BattVolt); 
  }
}

void ReadSerial()
{
 inChar = Serial.read(); // read character
 if((inChar>='0') && (inChar <='6'))
   sendAnalogValue(inChar - '0');
 return;
}

void setup() {
  Serial.begin(9600);
  pinMode(Sw1,INPUT_PULLUP);	// Button to turn Battery Display on
  pinMode(Pin4,OUTPUT);		// Relay to turn Battery Charger On
  pinMode(Pin7,OUTPUT);		// Raspberry Pi Relay (Pi on when relay on)
  pinMode(13,OUTPUT);		// Battery Voltage > 11.5 VDC
  pinMode(9,OUTPUT);		// Battery Voltage > 12 VDC
  pinMode(10,OUTPUT);		// Battery Voltage > 12.5 VDC
  pinMode(3,OUTPUT);		// Battery Voltage > 13 VDC
  pinMode(5,OUTPUT);		// Battery Voltage > 13.5 VDC
  pinMode(6,OUTPUT);		// Battery Voltage > 14 VDC
  digitalWrite(Pin4,HIGH);
  digitalWrite(Pin7,LOW);
  digitalWrite(13,LOW);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(3,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
}

void loop() {  
  int sensorValue = analogRead(A0);
///// Battery Charger Loop
// Sensor Value 900 = ((5.0/1023)*900)+9.59 = 13.99 VDC
// Sensor Value 950 = ((5.0/1023)*950)+9.59 = 14.23 VDC
// Sensor Value 1000 = ((5.0/1023)*1000)+9.59 = 14.47 VDC
  if(sensorValue > 1000){
    digitalWrite(Pin4,LOW); // High to charge
  }
// Sensor Value 395 = ((5.0/1023)*395)+9.59 = 11.52 VDC
// Sensor Value 498 = ((5.0/1023)*498)+9.59 = 12.02 VDC
  else if(sensorValue < 395){
    digitalWrite(Pin4,HIGH);
  }

///// LED Voltage Indicator Loops:
  readSw1 = digitalRead(Sw1); // Read the value of the switch on port 2
  if (readSw1 == LOW) {
    // Sensor Value 906 = ((5.0/1023)*906)+9.57= 14.0 VDC
    if(sensorValue > 906){
      digitalWrite(6,HIGH);
    }
    // Sensor Value 814 = ((5.0/1023)*814)+9.57= 13.5 VDC
    if(sensorValue > 814){
      digitalWrite(5,HIGH);
    }
    // Sensor Value 712 = ((5.0/1023*712)+9.57= 13.0 VDC
    if(sensorValue > 712){
      digitalWrite(3,HIGH);
    }
    // Sensor Value 600 = ((5.0/1023)*600)+9.57= 12.5 VDC
    if(sensorValue > 600){
      digitalWrite(10,HIGH);
    }
    // Sensor Value 497 = ((5.0/1023)*497)+9.57= 12 VDC
    if(sensorValue > 497){
      digitalWrite(9,HIGH);
    }
    // Sensor Value 395 = ((5.0/1023*395)+9.57= 11.5 VDC
    if(sensorValue > 395){
      digitalWrite(13,HIGH);
    }
    delay(2000); // delay so that you can read the led's
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(13,LOW);
  }

// Raspberry Pi Shutdown Loop
// Sensor Value 283 = ((5.0/1023)*293)+9.57= 11.0 VDC
  if(sensorValue > 283){
    digitalWrite(7,LOW);
  }
// Sensor Value 190 = ((5.0/1023)*190)+9.57= 10.5 VDC
  else if(sensorValue < 190){
    digitalWrite(7,HIGH);
  }
  if(Serial.available() > 0){
    ReadSerial();
  }
}

