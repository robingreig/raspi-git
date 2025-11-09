/* @file HelloKeypad.pde
|| @version 1.0
|| @author Alexander Brevig
|| @contact alexanderbrevig@gmail.com
||
|| @description
|| | Demonstrates the simplest use of the matrix Keypad library.
|| #
*/
#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 4; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

const String password = "123BAD456"; // put password here
String input_password;

void setup(){
  Serial.begin(115200);
  input_password.reserve(16); // maximum input characters is 17
}
  
void loop(){
  char key = keypad.getKey();
  
  if (key){
    Serial.print(key);

    if(key == '*'){
      input_password = ""; // clear input password
      Serial.println();
      Serial.println("Password Cleared");
    } else if (key == '#'){
      if(password == input_password) {
        Serial.println();
        Serial.println("Password is Correct");
      } else {
        Serial.println();
        Serial.println("Password is incorrect, try again");
      }
    input_password = ""; // clear input password
    } else {
      input_password += key; // append new character to input password string
    }
  }
}
