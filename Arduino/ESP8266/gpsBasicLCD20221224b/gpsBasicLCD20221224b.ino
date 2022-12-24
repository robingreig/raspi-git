#include <LiquidCrystal_I2C.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>
/*
   This sample sketch demonstrates the normal use of a TinyGPSPlus (TinyGPSPlus) object.
   It requires the use of SoftwareSerial, and assumes that you have a
   4800-baud serial GPS device hooked up on pins 4(rx) and 3(tx).
*/
static const int RXPin = 13, TXPin = 15; // tx & rx pins to gps
static const uint32_t GPSBaud = 9600;  // gps baud rate

int lcdColumns = 16; // Set LCD Columns
int lcdRows = 2; // Set LCD Rows
// set LCD address, number of columns and rows
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);

unsigned long previousMillis = 0; // variable to hold previous time
const long interval = 2000; // time interval in mS

// The TinyGPSPlus object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);

void setup()
{
  Serial.begin(115200);
  ss.begin(GPSBaud);
  lcd.init(); // initialize LCD

  Serial.println(F("DeviceExample.ino"));
  Serial.println(F("A simple demonstration of TinyGPSPlus with an attached GPS module"));
  Serial.print(F("Testing TinyGPSPlus library v. ")); Serial.println(TinyGPSPlus::libraryVersion());
  Serial.println(F("by Mikal Hart"));
  Serial.println();
}

void loop()
{
  // This sketch displays information every time a new sentence is correctly encoded.
  while (ss.available() > 0)
    if (gps.encode(ss.read()))
      displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    while(true);
  }
}

void displayInfo()
{
  unsigned long currentMillis = millis(); // current time
  if (gps.location.isValid())
  {
    if (currentMillis - previousMillis >= interval)
      {
      Serial.print("interval = ");
      Serial.println(interval);
      Serial.print("currentMillis = ");
      Serial.println(currentMillis);
      Serial.print("previousMillis = ");
      Serial.println(previousMillis);
      lcd.backlight(); //turn backlight on
      lcd.setCursor(0,0); // set cursor to first column, first row
      lcd.print("Lat:   "); //print Lat message
      lcd.print(gps.location.lat(), 6); // display latitude from gps
      lcd.setCursor(0,1); // set cursor to second column, first row
      lcd.print("Lng: "); // print Long message
      lcd.print(gps.location.lng(), 6); // display longitude from gps
      previousMillis = currentMillis; // updated previousMillis
      }
    Serial.print(F("Location: "));
    Serial.print(gps.location.lat(), 6);
    Serial.print(F(","));
    Serial.print(gps.location.lng(), 6);
  }
  else
  {
    lcd.print("Aquiring Sats");
    Serial.print(F("INVALID"));
  }

  Serial.print(F("  Date/Time: "));
  if (gps.date.isValid())
  {
    Serial.print(gps.date.month());
    Serial.print(F("/"));
    Serial.print(gps.date.day());
    Serial.print(F("/"));
    Serial.print(gps.date.year());
  }
  else
  {
    Serial.print(F("INVALID"));
  }

  Serial.print(F(" "));
  if (gps.time.isValid())
  {
    if (gps.time.hour() < 10) Serial.print(F("0"));
    Serial.print(gps.time.hour());
    Serial.print(F(":"));
    if (gps.time.minute() < 10) Serial.print(F("0"));
    Serial.print(gps.time.minute());
    Serial.print(F(":"));
    if (gps.time.second() < 10) Serial.print(F("0"));
    Serial.print(gps.time.second());
    Serial.print(F("."));
    if (gps.time.centisecond() < 10) Serial.print(F("0"));
    Serial.print(gps.time.centisecond());
  }
  else
  {
    Serial.print(F("INVALID"));
  }

  Serial.println();
}
