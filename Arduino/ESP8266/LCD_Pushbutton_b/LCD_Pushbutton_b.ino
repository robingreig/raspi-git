/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
*********/

#include <LiquidCrystal_I2C.h>

// set the LCD number of columns and rows
int lcdColumns = 16;
int lcdRows = 2;
const int buttonPin = 15; // pushbutton gpio pin number
int buttonState = 0; // variable for storing button state

// set LCD address, number of columns and rows
// if you don't know your display address, run an I2C scanner sketch
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  

void setup(){
  // initialize LCD
  lcd.init();
  // turn off LCD backlight                      
  lcd.noBacklight();
  // initialize the pushbutton pin as an input
  pinMode(buttonPin, INPUT);
  Serial.begin(115200);
  Serial.println("\n LCD_Pushbutton_b");
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
    lcd.print("-15.2 C"); // print message on second line
    delay(5000);
    lcd.clear(); // clear display
    lcd.noBacklight(); // turn backlight off
    buttonState = 0; // reset button state loq
  }
}
