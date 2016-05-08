const int analogInTable[6]= {A0,A1,A2,A3,A4,A5};

char inChar;

int recoverValue = 1;

const int numReadingsA0 = 10; // The number of samples to keep. Using a constant allows us to use it in a array
int readingsA0[numReadingsA0]; // Readings from A0
int readIndexA0 = 0; // The index of the current reading
int totalA0 = 0; // The running total
int averageA0 = 0; // The average of A0

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
  for (int thisReadingA0 = 0; thisReadingA0 < numReadingsA0; thisReadingA0 ++){
    readingsA0[thisReadingA0] = 0;
  } 
}

void loop() {  
  int sensorValueA0 = analogRead(A0);
  if (recoverValue < 1){
   delay(5000);
  }
  // subtract the last reading
  totalA0 = totalA0 - readingsA0[readIndexA0];
  // read from the sensor
  readingsA0[readIndexA0] = sensorValueA0;
  // add the reading to the total:
  totalA0 = totalA0 + readingsA0[readIndexA0];
  // advance to the next position in the array:
  readIndexA0 = readIndexA0 + 1;
  // if we're at the end of the array:
  if ((readIndexA0) >= numReadingsA0) {
    // wrap around to the beginning
    readIndexA0 = 0;
  }
  // Calculate the average:
  averageA0 = totalA0 / numReadingsA0;
  if(sensorValueA0 > 250)
    {
    digitalWrite(8,LOW);
    digitalWrite(13,HIGH);
    recoverValue = 1;
    }
  else if(sensorValueA0 > 200)
    {
    digitalWrite(8,LOW);
    digitalWrite(13,LOW);
    }
  else
    {
    digitalWrite(8,HIGH);
    digitalWrite(13,LOW);
    recoverValue = 0;
    delay(500);
    }
  if(Serial.available() > 0){
      inChar = Serial.read(); // read character
      if((inChar>='0') && (inChar <='5')){
         sendAnalogValue(inChar - '0');
      }
      if (inChar = '0'){
//       Serial.println(sensorValueA0);
//       Serial.println(averageA0);
      }
    }
  delay(100);      
}
