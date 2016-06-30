const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{
  
  int valueAD;
  float VoltageA0;
  valueAD = analogRead(analogInTable[Channel]);
  VoltageA0 = valueAD * (5.0/1023.0)+9.57;
  if (VoltageA0 <= 9.7){
    VoltageA0 = 0;
  }
  Serial.println(VoltageA0); 
}

void setup() {
  Serial.begin(9600);
  pinMode(6,OUTPUT);
  digitalWrite(6,LOW);
  pinMode(5,OUTPUT);
  digitalWrite(5,LOW);
  pinMode(3,OUTPUT);
  digitalWrite(3,LOW);
  pinMode(10,OUTPUT);
  digitalWrite(10,LOW);
  pinMode(9,OUTPUT);
  digitalWrite(9,LOW);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  pinMode(7,OUTPUT);
//  digitalWrite(7,HIGH);
  digitalWrite(7,LOW);
  pinMode(8,OUTPUT);
//  digitalWrite(8,HIGH);
  digitalWrite(8,LOW);
}

void loop() {  
  delay(1000);

  int sensorValue = analogRead(A0);

  // sensorValue of 190 = ((5/1023 * 200)+9.57) = 10.49
  if(sensorValue < 190){
    digitalWrite(13,LOW);
    digitalWrite(8,HIGH);
    }

  // sensorValue of 302 = ((5/1023 * 302)+9.57)=11.05VDC
  if(sensorValue > 302){ 
    digitalWrite(13,HIGH);
    }

  // sensorValue of 405 = ((5/1023 * 405)+9.57)=11.55
  if(sensorValue > 405){
    digitalWrite(9,HIGH);
    }

  // sensorValue of 508 = ((5/1023 * 508)+9.57)=12.05
  if(sensorValue > 508){
    digitalWrite(10,HIGH);
    }

  // sensorValue of 610 = ((5/1023 * 610)+9.57)=12.55
  if(sensorValue > 610){
    digitalWrite(3,HIGH);
    }

  // sensorValue of 712 = ((5/1023 * 712)+9.57)=13.05
  if(sensorValue > 712){
    digitalWrite(5,HIGH);
    }

  // sensorValue of 814 = ((5/1023 * 814)+9.57)=13.55
  if(sensorValue > 814){
    digitalWrite(6,HIGH);
    }

  if(Serial.available() > 0){
      inChar = Serial.read(); // read character
     
      if((inChar>='0') && (inChar <='5')){
         sendAnalogValue(inChar - '0');
      }
      else if (inChar=='6'){
        Serial.println("Nothing to Do!"); 
      }
      else if (inChar=='7'){
        Serial.println("Relay 02 Off"); 
        digitalWrite(7,HIGH);
        delay(1000);
        digitalWrite(7,LOW);
        delay(1000);
      }
      else if (inChar=='8'){
        Serial.println("Relay 01 Off"); 
        digitalWrite(8,HIGH);
        delay(1000);
        digitalWrite(8,LOW);
        delay(1000);
      }
    }
  delay(100);      
}
