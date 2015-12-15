const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{
  int valueAD;
  float BattVolt;
  valueAD = analogRead(analogInTable[Channel]);
  BattVolt = valueAD * (5.0/1023.0)+9.57;
  if (BattVolt <= 9.6){
    BattVolt = 0;
  }
  Serial.println(BattVolt); 
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
  pinMode(13,OUTPUT); // Relay to turn Battery Charger On & Onboard LED
  pinMode(12,OUTPUT); // Raspberry Pi Relay
  pinMode(8,OUTPUT); // Battery Voltage > 13VDC
  pinMode(7,OUTPUT); // Battery Voltage > 12VDC
  pinMode(4,OUTPUT); // Battery Voltage > 11VDC
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(8,LOW);
  digitalWrite(7,LOW);
  digitalWrite(4,LOW);
}

void loop() {  
  int sensorValue = analogRead(A0);
// Battery Charger Loop
// Sensor Value 900 = ((5.0/1023)*900)+9.57 = 13.97VDC
// Sensor Value 950 = ((5.0/1023)*950)+9.57 = 14.21VDC
// Sensor Value 1000 = ((5.0/1023)*1000)+9.57 = 14.46VDC
  if(sensorValue > 1000){
    digitalWrite(13,HIGH);
  }
// Sensor Value 395 = ((5.0/1023)*395)+9.57=11.5VDC
// Sensor Value 498 = ((5.0/1023)*498)+9.57=12.0VDC
  else if(sensorValue < 395){
    digitalWrite(13,LOW);
  }

// LED Voltage Indicator Loops:
// Sensor Value 293// Sensor Value 293 = ((5.0/1023)*293)+9.57=11.0VDC)
  if(sensorValue > 293){
    digitalWrite(4,HIGH);
  }
  else{
    digitalWrite(4,LOW);
  }
// Sensor Value 498 = ((5.0/1023)*498)+9.57=12.0VDC)
  if(sensorValue > 498){
    digitalWrite(7,HIGH);
  }
  else{
    digitalWrite(7,LOW);
  }
// Sensor Value 702 = ((5.0/1023*702)+9.57=13.0VDC
  if(sensorValue > 702){
    digitalWrite(8,HIGH);
  }
  else{
    digitalWrite(8,LOW);
  }

// Raspberry Pi Shutdown Loop
// Sensor Value 283 = ((5.0/1023)*293)+9.57=11.0VDC
  if(sensorValue > 283){
    digitalWrite(12,LOW);
  }
// Sensor Value 190 = ((5.0/1023)*190)+9.57=10.5VDC
  else if(sensorValue < 190){
    digitalWrite(12,HIGH);
  }
  if(Serial.available() > 0){
    ReadSerial();
  }
}

