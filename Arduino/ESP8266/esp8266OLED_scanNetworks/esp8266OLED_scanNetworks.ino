#include "SSD1306Wire.h"
#include "ESP8266WiFi.h"
// Initialize the OLED display using Arduino Wire:
//SSD1306Wire display(0x3c, SCL, SDA); // reversed!
SSD1306Wire display(0x3c, 14, 12); // reversed!

void setup() {
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  
  // Initialising the UI will init the display too.
  display.init();

  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.drawString(0, 0, "Starting.." );
  display.display();
}


void loop() {
  // clear the display
  display.clear();
  int height = 10;
  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
  if (n == 0) {
    display.drawString(0, 0, "no networks found");
  } else {
    for (int i = 0; i < n; ++i) {
      int y = i * height;
      String ssid = WiFi.SSID(i);
      String rssi = String(WiFi.RSSI(i));
      String encryption = "Unknown";
      switch(WiFi.encryptionType(i)) {
        case ENC_TYPE_WEP:
          encryption = "WEP";
          break;
        case ENC_TYPE_TKIP:
          encryption = "WPA";
          break;
        case ENC_TYPE_CCMP:
          encryption = "WPA2";
          break;
        case ENC_TYPE_NONE:
          encryption = "Open";
          break;
        case ENC_TYPE_AUTO:
          encryption = "Auto";
          break;
        default:
          encryption = "Unknown";
          break;
      }
      String line = ssid + ": " + rssi + " " + encryption;
      display.drawString(0, y, line);
      display.display();
      delay(10);
    }
  }

  // Wait a bit before scanning again
  delay(5000);
  }
