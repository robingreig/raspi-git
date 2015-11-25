const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{
  int valueAD;
  float VoltageA0;
  valueAD = analogRead(analogInTable[Channel]);
//  Serial.print("A");
//  Serial.print(Channel);
//  Serial.print("=");
//  Serial.println(valueAD);
  VoltageA0 = valueAD * (5.0/1023.0)+9.52;
  Serial.println(VoltageA0); 
}

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
  digitalWrite(13,HIGH);
}

void loop() {  
  int sensorValue = analogRead(A0);
//  Serial.println(sensorValue);
  if(sensorValue > 250)
    {
    digitalWrite(8,LOW);
    digitalWrite(13,HIGH);
    }
  else if(sensorValue > 200)
    {
    digitalWrite(8,LOW);
    digitalWrite(13,LOW);
    }
  else
    {
    digitalWrite(8,HIGH);
    digitalWrite(13,LOW);
    delay(500);
    }
  if(Serial.available() > 0)
    {
      digitalWrite(8,LOW);
      inChar = Serial.read(); // read character
      if((inChar>='0') && (inChar <='5'))
         sendAnalogValue(inChar - '0');
    }
  delay(100);      
}
