/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
*********/

#include <LiquidCrystal_I2C.h>
#include <OneWire.h>
#include <DallasTemperature.h>

int lcdColumns = 16; // Set LCD Columns
int lcdRows = 2; // Set LCD Rows
const int buttonPin = 15; // pushbutton gpio pin number
int buttonState = 0; // variable for storing button state
const int oneWireBus = 13; // GPIO for DS18B20

// set LCD address, number of columns and rows
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

void setup(){
  // initialize LCD
  lcd.init();
  // turn off LCD backlight                      
  lcd.noBacklight();
  // initialize the pushbutton pin as an input
  pinMode(buttonPin, INPUT);
  Serial.begin(115200);
  Serial.println("\n LCD_Pushbutton_b");
  sensors.begin(); // Start DS18B20 sensor
}

void loop(){
  buttonState = digitalRead(buttonPin);
  Serial.println("Running outside IF loop");
  Serial.print("buttonState = ");
  Serial.println(buttonState);
  if (buttonState == HIGH) {
    Serial.println("Running inside IF loop");
    lcd.backlight(); // turn backlight on
    lcd.setCursor(0, 0); // set cursor to first column, first row
    lcd.print("Outside Temp"); // print message on first line
    lcd.setCursor(0,1); // set cursor to first column, second row
    sensors.requestTemperatures(); // poll DS18B20 for temp
    float temperatureC = sensors.getTempCByIndex(0);
    Serial.print(temperatureC);
    Serial.println("ºC");
    lcd.print(temperatureC); // print message on second line
    lcd.print(" C");
    delay(5000);
    lcd.clear(); // clear display
    lcd.noBacklight(); // turn backlight off
    buttonState = 0; // reset button state loq
  }
}
