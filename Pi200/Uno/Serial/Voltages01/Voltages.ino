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
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
}

void loop() {  
  delay(50);
  int sensorValue = analogRead(A0);
  if(sensorValue > 200)
    {
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
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
