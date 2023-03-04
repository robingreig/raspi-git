/*
  blink_All.ino
  Blink the blue LED on the ESP-12E module (GPIO1, LED_BUILTIN, TXD0)
  Blink the blue LED on the NodeMCU module (GPIO16, Wake)

  NOTE: Both LED's on the board are active LOW so they work in reverse to the outputs
  
  The blue LED on the ESP-12E module is connected to GPIO1
  (which is also the TXD pin; so we cannot use Serial.print() at the same time)

  Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/
int pinNum[9] = {16, 14, 12, 13, 15, 00, 04, 05, 02};
// Initialize Relay 1, GPIO16, WAKE pin as an output
// Initialize Relay 2, GPIO14, SCLK pin as an output
// Initialize Relay 3, GPIO12, MISO pin as an output
// Initialize Relay 4, GPIO13, MOSI pin as an output
// Initialize Relay 5, GPIO15, CS pin as an output
// Initialize Relay 6, GPIO0, FLASH pin as an output
// Initialize Relay 7, GPIO4, SDA pin as an output
// Initialize Relay 8, GPIO5, SCL pin as an output

void setup() {
  for (int i = 0; i < 9; i++){
    pinMode(pinNum[i], OUTPUT);
    digitalWrite(pinNum[i], LOW); 
  }
}

// the loop function runs over and over again forever
void loop() {
  delay(1000);
  for (int i = 0; i < 9; i++){
    digitalWrite(pinNum[i], HIGH);
    delay(500); 
  }
  delay(1000);
  for (int i = 9; i > -1; i--){
    digitalWrite(pinNum[i], LOW);
    delay(500);
  }
  delay(3000);
}
