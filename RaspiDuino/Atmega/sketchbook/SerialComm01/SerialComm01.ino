const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{
  
  int valueAD;
  valueAD = analogRead(analogInTable[Channel]);
  Serial.print("A");
  Serial.print(Channel);
  Serial.print("=");
  Serial.println(valueAD); 
}



void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available() > 0)
    {
      
      inChar = Serial.read(); // read character
      
      if((inChar>='0') && (inChar <='5'))
         sendAnalogValue(inChar - '0');
    }
  delay(1);      
}
