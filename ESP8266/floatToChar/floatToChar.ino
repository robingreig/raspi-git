/*
convert float to char
*/

#include <string.h>

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

float temperature = -12.5;
char convert[16];

// the loop routine runs over and over again forever:
void loop() {
  Serial.print("float temp = ");
  Serial.println(temperature);
  sprintf(convert, "%.3f", temperature);
  Serial.print("A converted float: %s");
  Serial.println(convert);
  delay(1000);        // delay in between reads for stability
}
