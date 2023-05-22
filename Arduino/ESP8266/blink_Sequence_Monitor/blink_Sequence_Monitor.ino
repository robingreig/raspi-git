/*
  blink_All.ino
  Blink the blue LED on the ESP-12E module (GPIO1, LED_BUILTIN, TXD0)
  Blink the blue LED on the NodeMCU module (GPIO16, Wake)

  NOTE: Both LED's on the board are active LOW so they work in reverse to the outputs
  
  The blue LED on the ESP-12E module is connected to GPIO1
  (which is also the TXD pin; so we cannot use Serial.print() at the same time)

  Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/
int pinNum[9] = {16, 5, 4, 0, 2, 14, 12, 13, 15};
//  Initialize D0, GPIO16, WAKE pin as an output
//  Initialize D1, GPIO5, SCL pin as an output
//  Initialize D2, GPIO4, SDA pin as an output
//  Initialize D3, GPIO0, FLASH pin as an output
//  Initialize D4, GPIO2, TXD1 pin as an output
//  Initialize D5, GPIO14, SCLK pin as an output
//  Initialize D6, GPIO12, MISO pin as an output
//  Initialize D7, GPIO13, MOSI pin as an output
//  Initialize D8, GPIO15, CS pin as an output

void setup() {
  for (int i = 0; i < 9; i++){
    pinMode(pinNum[i], OUTPUT);
    Serial.begin(115200); 
  }
}

// the loop function runs over and over again forever
void loop() {
  for (int i = 0; i < 9; i++){
    digitalWrite(pinNum[i], HIGH);
    Serial.printf("pinNum HIGH: %i",pinNum[i]);
    Serial.println();
    delay(2000);
  }
  for (int i = 8; i > -1; i--){
    digitalWrite(pinNum[i], LOW);
    Serial.printf("pinNum LOW: %i",pinNum[i]);
    Serial.println();
    delay(2000); 
  }
}
