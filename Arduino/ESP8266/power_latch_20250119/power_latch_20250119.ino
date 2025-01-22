/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
*********/

// Define power latch pin for ESP32 (GPIO 5) / ESP8266 (GPIO 5) / Arduino (Digital 5)
const int powerLatch = 5;
// reset timer every loop
unsigned long previousMillis = 0;
// Length of time before power down
const long interval = 10000;
// Start with ledState = LOW = ON
int ledState = LOW;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  // Define powerLatch pin as an OUTPUT
  pinMode(powerLatch, OUTPUT);  
  // Keeps the circuit on
  digitalWrite(powerLatch, HIGH);
}

void loop() {
  if (ledState == LOW) {
    ledState = HIGH;  // Note that this switches the LED *off*
  } else {
    ledState = LOW;  // Note that this switches the LED *on*
  }
  delay(500);
  digitalWrite(LED_BUILTIN, ledState);
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    // Turns the power latch circuit off
    digitalWrite(powerLatch, LOW);
  }
}
