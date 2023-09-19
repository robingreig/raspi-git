/*********
 * Robin Greig 2023.08.26
 * Display RSSi on OLED as a fixed value
*********/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

unsigned long previousMillis = 0; // will store last time MQTT published
const long interval = 5000; // 5 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(115200);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  delay(2000);
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(20, 30);
  display.println("Starting");
  display.display();
}

void loop() {

  unsigned long currentMillis = millis();
// Check to see if it is time to publish MQTT
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    display.clearDisplay();
    display.setTextSize(2);
//    display.setTextColor(WHITE);
    display.setCursor(40, 0);
    // Display static text
    display.println("RSSI:");
    display.setTextSize(3);
    display.setCursor(40, 22);
    // Display static text
    display.println("-48");
    display.display();
  }
}
