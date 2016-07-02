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
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
//  digitalWrite(7,HIGH);
  digitalWrite(7,LOW);
//  digitalWrite(8,HIGH);
  digitalWrite(8,LOW);
}

void loop() {  
  delay(500);
  int sensorValue = analogRead(A0);
//  Serial.println(sensorValue);
//  if(sensorValue > 525)
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=13.55
  if(sensorValue > 814) // 13.55VDC
    {
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);

    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=13.05
  else if(sensorValue > 712) // 13.05VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(8,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=12.55
  else if(sensorValue > 610) // 12.55VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=12.05
  else if(sensorValue > 508) // 12.05VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=11.55
  else if(sensorValue > 405) // 11.55VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,HIGH);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=11.05
  else if(sensorValue > 302) // 11.05VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  // sensorValue of 814 = ((5/1023 * 814)+9.57)=10.55
  else if(sensorValue > 200) // 10.55VDC
    {
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(8,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
//    digitalWrite(7,HIGH);
    digitalWrite(7,LOW);
//    digitalWrite(8,HIGH);
    digitalWrite(8,LOW);
    }
  else
    {
    digitalWrite(13,LOW);
    digitalWrite(8,HIGH);
    }
  if(Serial.available() > 0){
      inChar = Serial.read(); // read character
     
      if((inChar>='0') && (inChar <='5')){
         sendAnalogValue(inChar - '0');
      }
      else if (inChar=='8'){
        Serial.println("Relay 01 On"); 
        digitalWrite(8,HIGH);
        delay(1000);
        Serial.println("Relay 01 Off"); 
      }
      else if (inChar=='7'){
        Serial.println("Relay 02 On"); 
        digitalWrite(7,HIGH);
        delay(1000);
        Serial.println("Relay 02 Off"); 
      }
    }
  delay(10);      
}
