
#include <ESP8266WiFi.h>

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 2 (LED_BUILTIN) as an output.
  pinMode(2, OUTPUT);
  Serial.begin(115200);
}
// the loop function runs over and over again forever
void loop() {
  int i;
  
  for(i=0;i<20;i++)
  {
    digitalWrite(2, HIGH);   // turn the LED on
    delay(500);              // wait for a second
    digitalWrite(2, LOW);    // turn the LED off
    delay(500);              // wait for a second
    Serial.print("count");
    Serial.println(i);

    if(i==6)
    {
      Serial.println("Resetting ESP");
      delay(500);
      ESP.restart(); //ESP.reset();
    }
  }
}
