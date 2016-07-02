const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{
  int valueAD;
  float VoltageA0;
  valueAD = analogRead(analogInTable[Channel]);
  VoltageA0 = valueAD * (5.0/1023.0)+9.57;
  Serial.println(VoltageA0); 
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
  pinMode(13,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
}

void loop() {  
  delay(50);
  int sensorValue = analogRead(A0);
// Battery Charger Loop
// Sensor Value 1000 = ((5.0/1023)*1000)+9.57=14.46VDC)
  if(sensorValue > 1000)
    {
    digitalWrite(9,HIGH);
    }
// Sensor Value 250 = ((5.0/1023*175)+9.57=10.8VDC
  else if(sensorValue < 250)
    {
    digitalWrite(9,LOW);
    }
// Raspberry Pi Shutdown Loop:
// Sensor Value 200 = ((5.0/1023)*200)+9.57=10.55VDC)
  if(sensorValue > 200)
    {
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
// Sensor Value 175 = ((5.0/1023*175)+9.57=10.43VDC
  else if(sensorValue > 175)
    {
    digitalWrite(13,LOW);
    digitalWrite(8,LOW);
    }
  else
    {
    digitalWrite(13,LOW);
    digitalWrite(8,HIGH);
    }
  if(Serial.available() > 0)
    {
    ReadSerial();
    }
}
