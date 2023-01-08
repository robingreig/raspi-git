/*
  blink_All.ino
  Blink the blue LED on the ESP-12E module (GPIO1, LED_BUILTIN, TXD0)
  Blink the blue LED on the NodeMCU module (GPIO16, Wake)

  NOTE: Both LED's on the board are active LOW so they work in reverse to the outputs
  
  The blue LED on the ESP-12E module is connected to GPIO1
  (which is also the TXD pin; so we cannot use Serial.print() at the same time)

  Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/

void setup() {
//  pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  pinMode(0, OUTPUT);     // Initialize GPIO0, FLASH pin as an output
  pinMode(1, OUTPUT);     // Initialize GPIO1, TX, TXD0, LED_BUILTIN pin as an output
  pinMode(2, OUTPUT);     // Initialize GPIO2, D4, TXD1 pin as an output
  pinMode(3, OUTPUT);     // Initialize GPIO3, RX, RXD0 pin as an output
  pinMode(4, OUTPUT);     // Initialize GPIO4, D2, SDA pin as an output
  pinMode(5, OUTPUT);     // Initialize GPIO5, D1, SCL pin as an output
//  pinMode(9, OUTPUT);     // GPIO9, SDD2, Locks up the ESP8266
  pinMode(10, OUTPUT);     // Initialize GPIO10, SDD3 pin as an output
  pinMode(12, OUTPUT);     // Initialize GPIO12, D6, MISO pin as an output
  pinMode(13, OUTPUT);     // Initialize GPIO13, D7, MOSI pin as an output
  pinMode(14, OUTPUT);     // Initialize GPIO14, D5, SCLK pin as an output
  pinMode(15, OUTPUT);     // Initialize GPIO15, D8, CS pin as an output
  pinMode(16, OUTPUT);     // Initialize GPIO16, D0, WAKE pin as an output
}

// the loop function runs over and over again forever
void loop() {
//  digitalWrite(LED_BUILTIN, LOW);   // Turn the LED on, by making the voltage LOW
  digitalWrite(1, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(3, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(15, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(13, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(12, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(14, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(2, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(0, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(4, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(5, HIGH);   // Turn the LED on (Note that HIGH is the voltage level
  delay(500);                      // Wait for half a second
  digitalWrite(16, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(500);                      // Wait for a second
  digitalWrite(10, HIGH);   // Turn the LED on, Note that HIGH is the voltage level
  delay(2000);                      // Wait for half a second
//  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED off by making the voltage HIGH
  digitalWrite(1, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(3, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(15, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(13, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(12, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(14, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(2, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(0, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(4, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(5, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);                      // Wait for half a second
  digitalWrite(16, LOW);  // Turn the LED off by making the voltage LOW
  delay(500);            // Wait for one second & start all over
  digitalWrite(10, LOW);  // Turn the LED off by making the voltage LOW
  delay(2000);                      // Wait for half a second
}
