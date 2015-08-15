/* 
 One_Input_Function
 
  The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached to A2
 * A2 set as an input with pullup 
 
 created 12 July 2015
 by Robin Greig
 
 */

// constants won't change. They're used here to 
// set pin numbers:
const int buttonPin1 = A0;     // the number of the pushbutton pin
const int ledPin1 =  13;      // the number of the LED pin
////const int buttonPin2 = A1;     // the number of the pushbutton pin
////const int ledPin2 =  9;      // the number of the LED pin
////const int buttonPin3 = A2;     // the number of the pushbutton pin
////const int ledPin3 =  10;      // the number of the LED pin
////const int buttonPin4 = A3;     // the number of the pushbutton pin
////const int ledPin4 =  3;      // the number of the LED pin
////const int buttonPin5 = A4;     // the number of the pushbutton pin
////const int ledPin5 =  5;      // the number of the LED pin
////const int buttonPin6 = A5;     // the number of the pushbutton pin
////const int ledPin6 =  6;      // the number of the LED pin


// Variables will change:
int ledState1 = HIGH;         // the current state of the output pin
int buttonState1 = HIGH;             // the current reading from the input pin
int lastButtonState1 = LOW;   // the previous reading from the input pin
////int ledState2 = HIGH;         // the current state of the output pin
////int buttonState2 = HIGH;             // the current reading from the input pin
////int lastButtonState2 = LOW;   // the previous reading from the input pin
////int ledState3 = HIGH;         // the current state of the output pin
////int buttonState3 = HIGH;             // the current reading from the input pin
////int lastButtonState3 = LOW;   // the previous reading from the input pin
////int ledState4 = HIGH;         // the current state of the output pin
////int buttonState4 = HIGH;             // the current reading from the input pin
////int lastButtonState4 = LOW;   // the previous reading from the input pin
////int ledState5 = HIGH;         // the current state of the output pin
////int buttonState5 = HIGH;             // the current reading from the input pin
////int lastButtonState5 = LOW;   // the previous reading from the input pin
////int ledState6 = HIGH;         // the current state of the output pin
////int buttonState6 = HIGH;             // the current reading from the input pin
////int lastButtonState6 = LOW;   // the previous reading from the input pin

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime1 = 0;  // the last time the output pin was toggled
long debounceDelay1 = 50;    // the debounce time; increase if the output flickers
////long lastDebounceTime2 = 0;  // the last time the output pin was toggled
////long debounceDelay2 = 50;    // the debounce time; increase if the output flickers
////long lastDebounceTime3 = 0;  // the last time the output pin was toggled
////long debounceDelay3 = 50;    // the debounce time; increase if the output flickers
////long lastDebounceTime4 = 0;  // the last time the output pin was toggled
////long debounceDelay4 = 50;    // the debounce time; increase if the output flickers
////long lastDebounceTime5 = 0;  // the last time the output pin was toggled
////long debounceDelay5 = 50;    // the debounce time; increase if the output flickers
////long lastDebounceTime6 = 0;  // the last time the output pin was toggled
////long debounceDelay6 = 50;    // the debounce time; increase if the output flickers

void setup() {
  serial.begin(9600);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(ledPin1, OUTPUT);
////  pinMode(buttonPin2, INPUT_PULLUP);
////  pinMode(ledPin2, OUTPUT);
////  pinMode(buttonPin3, INPUT_PULLUP);
////  pinMode(ledPin3, OUTPUT);
////  pinMode(buttonPin4, INPUT_PULLUP);
////  pinMode(ledPin4, OUTPUT);
////  pinMode(buttonPin5, INPUT_PULLUP);
////  pinMode(ledPin5, OUTPUT);
////  pinMode(buttonPin6, INPUT_PULLUP);
////  pinMode(ledPin6, OUTPUT);
}
int x = 1;

int DebounceCheck(int x){

  int reading(x) = digitalRead(buttonPin(x));
  // If the switch changed, due to noise or pressing:
  if (reading(x) != lastButtonState(x)) {
    // reset the debouncing timer
    lastDebounceTime(x) = millis();
  } 

  if ((millis() - lastDebounceTime(x)) > debounceDelay(x)) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState(x) = reading(x);
  }
  digitalWrite(ledPin(x), buttonState(x));
  lastButtonState(x) = reading(x);
}


void loop() {
  // read the state of the switch into a local variable:
////  int reading1 = digitalRead(buttonPin1);
////  int reading2 = digitalRead(buttonPin2);
////  int reading3 = digitalRead(buttonPin3);
////  int reading4 = digitalRead(buttonPin4);
////  int reading5 = digitalRead(buttonPin5);
////  int reading6 = digitalRead(buttonPin6);
void DebounceCheck(x)
serial.println(reading(x));
  // check to see if you just pressed the button 
  // (i.e. the input went from LOW to HIGH),  and you've waited 
  // long enough since the last press to ignore any noise:  

  // If the switch changed, due to noise or pressing:
////  if (reading1 != lastButtonState1) {
    // reset the debouncing timer
////    lastDebounceTime1 = millis();
////  } 

////  if ((millis() - lastDebounceTime1) > debounceDelay1) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState1 = reading1;
////  }

  // If the switch changed, due to noise or pressing:
////  if (reading2 != lastButtonState2) {
    // reset the debouncing timer
////    lastDebounceTime2 = millis();
////  } 
    
////  if ((millis() - lastDebounceTime2) > debounceDelay2) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState2 = reading2;
////  }

  // If the switch changed, due to noise or pressing:
////  if (reading3 != lastButtonState3) {
    // reset the debouncing timer
////    lastDebounceTime3 = millis();
////  } 

////  if ((millis() - lastDebounceTime3) > debounceDelay3) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState3 = reading3;
////  }

  // If the switch changed, due to noise or pressing:
////  if (reading4 != lastButtonState4) {
    // reset the debouncing timer
////    lastDebounceTime4 = millis();
////  } 
    
////  if ((millis() - lastDebounceTime4) > debounceDelay4) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState4 = reading4;
////  }
  

  // If the switch changed, due to noise or pressing:
////  if (reading5 != lastButtonState5) {
    // reset the debouncing timer
////    lastDebounceTime5 = millis();
////  } 

////  if ((millis() - lastDebounceTime5) > debounceDelay5) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState5 = reading5;
////  }

  // If the switch changed, due to noise or pressing:
////  if (reading6 != lastButtonState6) {
    // reset the debouncing timer
////    lastDebounceTime6 = millis();
////  } 
    
////  if ((millis() - lastDebounceTime6) > debounceDelay6) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
////    buttonState6 = reading6;
////  }
  
  
  // set the LED using the state of the button:
////  digitalWrite(ledPin1, buttonState1);
////  digitalWrite(ledPin2, buttonState2);
////  digitalWrite(ledPin3, buttonState3);
////  digitalWrite(ledPin4, buttonState4);
////  digitalWrite(ledPin5, buttonState5);
////  digitalWrite(ledPin6, buttonState6);

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
////  lastButtonState1 = reading1;
////  lastButtonState2 = reading2;
////  lastButtonState3 = reading3;
////  lastButtonState4 = reading4;
////  lastButtonState5 = reading5;
////  lastButtonState6 = reading6;
}

