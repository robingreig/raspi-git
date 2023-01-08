/*
 * ESP8266 Deep sleep mode example
 * Rui Santos 
 * Complete Project Details http://randomnerdtutorials.com
 */
 
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2000);
  pinMode(2, OUTPUT); // initialize LED output
  pinMode(4, OUTPUT); // initialize LED output
  pinMode(5, OUTPUT); // initialize LED output
}

void loop() {
  // Wait for serial to initialize.
  while(!Serial) { }

  digitalWrite(2, HIGH); // turn on led
  digitalWrite(4, HIGH); // turn on led
  digitalWrite(5, HIGH); // turn on led
  delay(1000); // 1 second delay
  digitalWrite(2, LOW); // turn off led
  digitalWrite(4, LOW); // turn off led
  digitalWrite(5, LOW); // turn off led
  
  // Deep sleep mode for 30 seconds, the ESP8266 wakes up by itself when GPIO 16 (D0 in NodeMCU board) is connected to the RESET pin
  Serial.println("");
  Serial.println("I'm awake, but I'm going into deep sleep mode for 30 seconds");
  
  // Deep sleep mode until RESET pin is connected to a LOW signal (for example pushbutton or magnetic reed switch)
  //Serial.println("I'm awake, but I'm going into deep sleep mode until RESET pin is connected to a LOW signal");
  ESP.deepSleep(10e6); 
}
