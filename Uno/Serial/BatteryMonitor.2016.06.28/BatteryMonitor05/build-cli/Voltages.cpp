#include <Arduino.h>
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
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(8,OUTPUT);
  digitalWrite(8,HIGH);
}

void loop() {  
  delay(500);
  int sensorValue = analogRead(A0);
//  Serial.println(sensorValue);
//  if(sensorValue > 525)
  if(sensorValue > 814)
    {
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 712)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(8,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 610)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 508)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 405)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 302)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else if(sensorValue > 200)
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    }
  else
    {
    digitalWrite(13,LOW);
    digitalWrite(8,HIGH);
    }
  if(Serial.available() > 0)
    {
      
      inChar = Serial.read(); // read character
      
      if((inChar>='0') && (inChar <='5'))
         sendAnalogValue(inChar - '0');
    }
  delay(1);      
}
