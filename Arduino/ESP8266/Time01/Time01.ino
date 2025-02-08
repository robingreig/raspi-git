#include <TimeLib.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println();

  time_t t = 1598063880; //unix timestamp
  setTime(t);
  Serial.print("Date: ");
  Serial.print(day());
  Serial.print("/");
  Serial.print(month());
  Serial.print("/");
  Serial.print(year());
  Serial.print(" ");
  Serial.print(hour());
   Serial.print(":");
  Serial.print(minute());
 Serial.print(":");
  Serial.println(second()); 
}

void loop() {
  // put your main code here, to run repeatedly:
}
