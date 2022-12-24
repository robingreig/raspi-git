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
const long interval = 4000; // time interval in mS
int toggle = 0; // switch between lat&long / date&time
int hourMT = 00; //change from GMT to MST

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
      if (currentMillis - previousMillis >= interval && toggle == 0)
        {
          displayLatLng();
          toggle = 1;
          previousMillis = currentMillis; // update previousMillis
        }
      if (currentMillis - previousMillis >= interval && toggle == 1)
        {
          displayDateTime();
          toggle = 2;
          previousMillis = currentMillis; // update previousMillis
        }
      if (currentMillis - previousMillis >= interval && toggle == 2)
        {
          displaySatHdop();
          toggle = 3;
          previousMillis = currentMillis; // update previousMillis
        }
      if (currentMillis - previousMillis >= interval && toggle == 3)
        {
          displayAltAge();
          toggle = 0;
          previousMillis = currentMillis; // update previousMillis
        }
      }
    Serial.print(F("Location: "));
    Serial.print(gps.location.lat(), 6);
    Serial.print(F(","));
    Serial.print(gps.location.lng(), 6);
  }
  else
  {
    lcd.clear();
    lcd.backlight();
    lcd.print("Aquiring Sats1");
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
    lcd.clear();
    lcd.backlight();
    lcd.print("Aquiring Sats2");
    Serial.print(F("INVALID"));
  }

  Serial.print(F(" "));
  if (gps.time.isValid())
  {
    hourMT = (gps.time.hour() - 7); // adjust hour from GMT to MT
    // if hour GMT < 7 it will be negative so 24 + (-)hourMT will correct it
    if (hourMT < 1) (hourMT = 24 + hourMT); //
    if (hourMT < 10) Serial.print(F("0"));
//    if (gps.time.hour() < 10) Serial.print(F("0"));
    Serial.print(hourMT);
//    Serial.print(gps.time.hour());
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
    lcd.clear();
    lcd.backlight();
    lcd.print("Aquiring Sats3");
    Serial.print(F("INVALID"));
  }

  Serial.println();
}

void displayLatLng() // function to display lat & long
{
  lcd.clear(); // clear lcd display
  lcd.backlight(); //turn backlight on
  lcd.setCursor(0,0); // set cursor to first column, first row
  lcd.print("Lat:   "); //print Lat message
  lcd.print(gps.location.lat(), 6); // display latitude from gps
  lcd.setCursor(0,1); // set cursor to second column, first row
  lcd.print("Lon: "); // print Long message
  lcd.print(gps.location.lng(), 6); // display longitude from gps  
}

void displayDateTime()
{
  int DST = 7; // DST = 7 winter & 6 summer
  int hourMT = 0; // hour variable to conver GMT to MT
  int dayMT = 0; // day variable to convert GMT to MT
  lcd.clear(); // clear lcd display
  lcd.backlight(); //turn backlight on
  lcd.setCursor(0,0); // set cursor to first column, first row
  lcd.print("Date: "); //print Date message
  lcd.print(gps.date.year());
  lcd.print(F("/"));
  lcd.print(gps.date.month());
  lcd.print(F("/"));
  hourMT = (gps.time.hour() - DST); // adjust hour from GMT to MT
  dayMT = (gps.date.day());
  // if hourMT is negative, it is yesterday MT so dayMT - 1
  if (hourMT < 0) (dayMT -=1);
  lcd.print(dayMT);
  lcd.setCursor(0,1); // set cursor to second column, first row
  lcd.print("Time: "); // print Time message
  // if hour GMT < 7 it will be negative so 24 + (-)hourMT will correct it
  if (hourMT < 1) (hourMT = 24 + hourMT); // adjust hour from GMT to MT
  if (hourMT < 10) Serial.print(F("0"));
  lcd.print(hourMT);
  lcd.print(F(":"));
  if (gps.time.minute() < 10) lcd.print(F("0"));
  lcd.print(gps.time.minute());
  lcd.print(F(":"));
  if (gps.time.second() < 10) lcd.print(F("0"));
  lcd.print(gps.time.second());
}
void displaySatHdop()
{
  int satVal = 0;
  float hdopVal = 0;
  Serial.print("Number of Satellites: ");
  satVal = gps.satellites.value();
  Serial.println(satVal);
  Serial.print("Horizontal Dillution of Precision: ");
  hdopVal = gps.hdop.hdop();
  Serial.println(hdopVal);
  lcd.clear(); // clear lcd display
  lcd.backlight(); //turn backlight on
  lcd.setCursor(0,0); // set cursor to first column, first row
  lcd.print("Satellites: "); //print Satellites message
  lcd.print(satVal); // number of satellites
  lcd.setCursor(0,1);
  lcd.print("HDOP (1-2): ");
  lcd.print(hdopVal);
}
void displayAltAge()
{
  int ageVal = 0;
  float altVal = 0;
  Serial.print("Altitude(m): ");
  altVal = gps.altitude.meters();
  Serial.println(altVal);
  Serial.print("Age(ms): ");
  ageVal = gps.location.age();
  Serial.println(ageVal);
  lcd.clear(); // clear lcd display
  lcd.backlight(); //turn backlight on
  lcd.setCursor(0,0); // set cursor to first column, first row
  lcd.print("Alt (m): "); //print Satellites message
  lcd.print(altVal); // number of satellites
  lcd.setCursor(0,1);
  lcd.print("Age (ms) : ");
  lcd.print(ageVal);
}
