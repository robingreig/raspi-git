/* Voltages.ino 2016.06.30
   Pins 3, 5, 6, 9, 10, & 13 display the voltage level of the battery when button 2 is pushed  
   Pin 4  will turn the battery charger on
   Pin 7 controls the Raspi (Pin 7 on, Raspi on)
*/

const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};
int val = 0; // value of switch
int sw1 = 2; // Switch 1 is port 2 
float zener = 9.59; // Zener Voltage Drop
float multiplier = 4.6; //Multiplier to set digital > analog steps
const int debug = 1; // If debug = 1 then extra lines printed
char inChar;

void sendAnalogValue(byte Channel)
{
  int valueAD;
  float SensorAnalog;
  float BattVolt;
  valueAD = analogRead(analogInTable[Channel]);
  SensorAnalog = (valueAD * (multiplier/1023.0)); // 0-5 V
  //BattVolt = ((valueAD * (multiplier/1023.0))+zener); // Send back Calculated Battery Voltage
  BattVolt = (SensorAnalog + zener); // Send back Calculated Battery Voltage
  if (BattVolt <= 9.6){
    BattVolt = 0;
  }
  if (debug == 1) {
    Serial.print("valueAD: ");
    Serial.println (valueAD);
    Serial.print("SensorAnalog: ");
    Serial.println (SensorAnalog);
    Serial.print("Calculated Battery Voltage: ");
    Serial.println(BattVolt); 
  } else {
    Serial.println(BattVolt); 
  }
}

void ReadSerial()
{
 inChar = Serial.read(); // read character
 if((inChar>='0') && (inChar <='5'))
   sendAnalogValue(inChar - '0');
 return;
}

void setup() {
  Serial.begin(9600);
  pinMode(sw1,INPUT_PULLUP);	// Button to turn Battery Display on
  pinMode(4,OUTPUT);		// Relay to turn Battery Charger On
  pinMode(7,OUTPUT);		// Raspberry Pi Relay (Pi on when relay on)
  pinMode(13,OUTPUT);		// Battery Voltage > 11.5 VDC
  pinMode(9,OUTPUT);		// Battery Voltage > 12 VDC
  pinMode(10,OUTPUT);		// Battery Voltage > 12.5 VDC
  pinMode(3,OUTPUT);		// Battery Voltage > 13 VDC
  pinMode(5,OUTPUT);		// Battery Voltage > 13.5 VDC
  pinMode(6,OUTPUT);		// Battery Voltage > 14 VDC
  digitalWrite(4,LOW);
  digitalWrite(7,HIGH);
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
// Sensor Value 900 = ((4.6/1023)*900)+9.59 = 13.64 VDC
// Sensor Value 950 = ((4.6/1023)*950)+9.59 = 13.86 VDC
// Sensor Value 1000 = ((4.6/1023)*1000)+9.59 = 14.08 VDC
// Sensor Value 1050 = ((4.6/1023)*1000)+9.59 = 14.31 VDC
// Sensor Value 1060 = ((4.6/1023)*1000)+9.59 = 14.36 VDC
// Sensor Value 1070 = ((4.6/1023)*1000)+9.59 = 14.4 VDC
  if(sensorValue > 1050){
    digitalWrite(4,HIGH);
  }
// Sensor Value 395 = ((5.0/1023)*395)+9.57=11.5VDC
// Sensor Value 498 = ((5.0/1023)*498)+9.57=12.0VDC
  else if(sensorValue < 395){
    digitalWrite(4,LOW);
  }

///// LED Voltage Indicator Loops:
  val = digitalRead(sw1); // Read the value of the switch on port 2
  if (val == LOW) {
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
    digitalWrite(7,HIGH);
  }
// Sensor Value 190 = ((5.0/1023)*190)+9.57= 10.5 VDC
  else if(sensorValue < 190){
    digitalWrite(7,LOW);
  }
  if(Serial.available() > 0){
    ReadSerial();
  }
}

