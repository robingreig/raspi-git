void setup(){
 Serial.begin(9600);
}

void loop(){
 if(Serial.available()){
  int number=Serial.read();
  Serial.print("Character Received: ");
  Serial.println(number);
  }
}
