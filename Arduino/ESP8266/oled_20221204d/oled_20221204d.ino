#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display = Adafruit_SSD1306();

#define BUTTON_A 0
#define BUTTON_B 16
#define BUTTON_C 2
#define LED      0

#if (SSD1306_LCDHEIGHT != 32)
 #error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

void setup() {  
  Serial.begin(115200);
  delay(1000);
  Serial.println("OLED FeatherWing test");
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x32)
  // init done
  Serial.println("OLED begun");
  
  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.
  display.display();
  delay(3000);

  // Clear the buffer.
  display.clearDisplay();
  display.display();
  delay(1000);
  
  Serial.println("IO test");

  pinMode(BUTTON_A, INPUT_PULLUP);
  pinMode(BUTTON_B, INPUT_PULLUP);
  pinMode(BUTTON_C, INPUT_PULLUP);

  // text display tests
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.print("Connecting to SSID\n'adafruit':");
  display.print("connected!");
  display.println("IP: 10.0.1.23");
  display.println("Sending val #0");
  display.setCursor(0,0);
  display.display(); // actually display all of the above
}


void loop() {
  if (! digitalRead(BUTTON_A)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("A");
  } else if (! digitalRead(BUTTON_B)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("B");
  } else if (! digitalRead(BUTTON_C)){
    display.clearDisplay();
    display.setCursor(0,0);
    display.print("C");
  }
  delay(10);
  yield();
  display.display();
}
