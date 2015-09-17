const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

void sendAnalogValue(byte Channel)
{

  int valueAD;
  float VoltageA0;
  valueAD = analogRead(analogInTable[Channel]);
  if (Channel == 0)
  {
    VoltageA0 = valueAD * (5.0/1023.0)+9.43;
  }
  else if (Channel == 1)
  {
    VoltageA0 = valueAD * (5.0/1023.0)+9.41;
  }
  else if (Channel == 2)
  {
    VoltageA0 = valueAD * (5.0/1023.0)+9.52;
  }
  else if (Channel == 3)
  {
    VoltageA0 = valueAD * (5.0/1023.0)+23.3;
  }
  else
  {
    VoltageA0 = valueAD * (5.0/1023.0)+1.00;
  }
  Serial.println(VoltageA0);
  Serial.println(byte(Channel));
}

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
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
