void setup() {
  // put your setup code here, to run once:
  ESP.wdtDisable();
  Serial.begin(115200);
}

unsigned long previousMillis1 = 0; // will store last time for wDT feed
unsigned long previousMillis2 = 0; // will store last time for restart
const long interval1 = 5000; // 5 second interval for WDT
//const long interval2 = 60000; // 60 second interval for restart
const long interval2 = 300000; // 5 minute interval for restart
int count = 0;

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis(); // will store current time
  Serial.print("loop is running: ");
  Serial.println(count);
  count ++;
  delay(1000);
  if (currentMillis - previousMillis1 >= interval1){
    previousMillis1 = currentMillis;
    ESP.wdtFeed();
    Serial.println("Just fed the dog");
  }
  if (currentMillis - previousMillis2 >= interval2){
    Serial.println("Restarting ESP8266");
    delay(500);
    ESP.restart();
  }
}
