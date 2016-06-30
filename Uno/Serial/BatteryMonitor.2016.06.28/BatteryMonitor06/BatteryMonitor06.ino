const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;
int val = 0; // Set switch value to 0
//int inPin = 7; // Switch Port
int inPin = A2; // Switch Port

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
  pinMode(inPin,INPUT_PULLUP);
  digitalWrite(8,HIGH);
}

void loop() {  
  int sensorValue = analogRead(A0);
  if(sensorValue < 200) {
      digitalWrite(8,LOW); // Turn Supply Relay Off
  } else {
      digitalWrite(8,HIGH); // Turn Supply Relay On
  }
  val = digitalRead(inPin);  // Read the value of the switch

  if (val == LOW) {
  //  Serial.println(sensorValue);
    if(sensorValue > 814) {
      digitalWrite(6,HIGH);
    }
    if(sensorValue > 712) {
      digitalWrite(5,HIGH);
    }
    if(sensorValue > 610) {
      digitalWrite(8,HIGH);
    }
    if(sensorValue > 508) {
      digitalWrite(3,HIGH);
    }
    if(sensorValue > 405) {
      digitalWrite(10,HIGH);
    }
    if(sensorValue > 302) {
      digitalWrite(9,HIGH);
    }
    if(sensorValue > 200) {
      digitalWrite(13,HIGH);
    }
    delay(3000);
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(3,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(13,LOW);

    if(Serial.available() > 0){
      
      inChar = Serial.read(); // read character
      
      if((inChar>='0') && (inChar <='5'))
         sendAnalogValue(inChar - '0');
      }
    delay(50);      
  }
}
