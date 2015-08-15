/* 
 Debounce
 
 Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
 press), the output pin is toggled from LOW to HIGH or HIGH to LOW.  There's
 a minimum delay between toggles to debounce the circuit (i.e. to ignore
 noise).  
 
 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground
 
 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.
 
 
 created 21 November 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Limor Fried
 
This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Debounce
 */

// constants won't change. They're used here to 
// set pin numbers:
const int buttonPin01 = A0;     // the number of the pushbutton pin
const int ledPin01 =  13;      // the number of the LED pin
const int buttonPin02 = A1;     // the number of the pushbutton pin
const int ledPin02 =  9;      // the number of the LED pin
const int buttonPin03 = A2;     // the number of the pushbutton pin
const int ledPin03 =  10;      // the number of the LED pin
const int buttonPin04 = A3;     // the number of the pushbutton pin
const int ledPin04 =  3;      // the number of the LED pin
const int buttonPin05 = A4;     // the number of the pushbutton pin
const int ledPin05 =  5;      // the number of the LED pin
const int buttonPin06 = A5;     // the number of the pushbutton pin
const int ledPin06 =  6;      // the number of the LED pin


// Variables will change:
int ledState01 = HIGH;         // the current state of the output pin
int buttonState01 = HIGH;             // the current reading from the input pin
int lastButtonState01 = LOW;   // the previous reading from the input pin
int ledState02 = HIGH;         // the current state of the output pin
int buttonState02 = HIGH;             // the current reading from the input pin
int lastButtonState02 = LOW;   // the previous reading from the input pin
int ledState03 = HIGH;         // the current state of the output pin
int buttonState03 = HIGH;             // the current reading from the input pin
int lastButtonState03 = LOW;   // the previous reading from the input pin
int ledState04 = HIGH;         // the current state of the output pin
int buttonState04 = HIGH;             // the current reading from the input pin
int lastButtonState04 = LOW;   // the previous reading from the input pin
int ledState05 = HIGH;         // the current state of the output pin
int buttonState05 = HIGH;             // the current reading from the input pin
int lastButtonState05 = LOW;   // the previous reading from the input pin
int ledState06 = HIGH;         // the current state of the output pin
int buttonState06 = HIGH;             // the current reading from the input pin
int lastButtonState06 = LOW;   // the previous reading from the input pin

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime01 = 0;  // the last time the output pin was toggled
long debounceDelay01 = 50;    // the debounce time; increase if the output flickers
long lastDebounceTime02 = 0;  // the last time the output pin was toggled
long debounceDelay02 = 50;    // the debounce time; increase if the output flickers
long lastDebounceTime03 = 0;  // the last time the output pin was toggled
long debounceDelay03 = 50;    // the debounce time; increase if the output flickers
long lastDebounceTime04 = 0;  // the last time the output pin was toggled
long debounceDelay04 = 50;    // the debounce time; increase if the output flickers
long lastDebounceTime05 = 0;  // the last time the output pin was toggled
long debounceDelay05 = 50;    // the debounce time; increase if the output flickers
long lastDebounceTime06 = 0;  // the last time the output pin was toggled
long debounceDelay06 = 50;    // the debounce time; increase if the output flickers

void setup() {
  pinMode(buttonPin01, INPUT_PULLUP);
  pinMode(ledPin01, OUTPUT);
  pinMode(buttonPin02, INPUT_PULLUP);
  pinMode(ledPin02, OUTPUT);
  pinMode(buttonPin03, INPUT_PULLUP);
  pinMode(ledPin03, OUTPUT);
  pinMode(buttonPin04, INPUT_PULLUP);
  pinMode(ledPin04, OUTPUT);
  pinMode(buttonPin05, INPUT_PULLUP);
  pinMode(ledPin05, OUTPUT);
  pinMode(buttonPin06, INPUT_PULLUP);
  pinMode(ledPin06, OUTPUT);
}

void loop() {
  // read the state of the switch into a local variable:
  int reading01 = digitalRead(buttonPin01);
  int reading02 = digitalRead(buttonPin02);
  int reading03 = digitalRead(buttonPin03);
  int reading04 = digitalRead(buttonPin04);
  int reading05 = digitalRead(buttonPin05);
  int reading06 = digitalRead(buttonPin06);

  // check to see if you just pressed the button 
  // (i.e. the input went from LOW to HIGH),  and you've waited 
  // long enough since the last press to ignore any noise:  

  // If the switch changed, due to noise or pressing:
  if (reading01 != lastButtonState01) {
    // reset the debouncing timer
    lastDebounceTime01 = millis();
  } 

  if ((millis() - lastDebounceTime01) > debounceDelay01) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState01 = reading01;
  }

  // If the switch changed, due to noise or pressing:
  if (reading02 != lastButtonState02) {
    // reset the debouncing timer
    lastDebounceTime02 = millis();
  } 
    
  if ((millis() - lastDebounceTime02) > debounceDelay02) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState02 = reading02;
  }

  // If the switch changed, due to noise or pressing:
  if (reading03 != lastButtonState03) {
    // reset the debouncing timer
    lastDebounceTime03 = millis();
  } 

  if ((millis() - lastDebounceTime03) > debounceDelay03) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState03 = reading03;
  }

  // If the switch changed, due to noise or pressing:
  if (reading04 != lastButtonState04) {
    // reset the debouncing timer
    lastDebounceTime04 = millis();
  } 
    
  if ((millis() - lastDebounceTime04) > debounceDelay04) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState04 = reading04;
  }
  

  // If the switch changed, due to noise or pressing:
  if (reading05 != lastButtonState05) {
    // reset the debouncing timer
    lastDebounceTime05 = millis();
  } 

  if ((millis() - lastDebounceTime05) > debounceDelay05) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState05 = reading05;
  }

  // If the switch changed, due to noise or pressing:
  if (reading06 != lastButtonState06) {
    // reset the debouncing timer
    lastDebounceTime06 = millis();
  } 
    
  if ((millis() - lastDebounceTime06) > debounceDelay06) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    buttonState06 = reading06;
  }
  
  
  // set the LED using the state of the button:
  digitalWrite(ledPin01, buttonState01);
  digitalWrite(ledPin02, buttonState02);
  digitalWrite(ledPin03, buttonState03);
  digitalWrite(ledPin04, buttonState04);
  digitalWrite(ledPin05, buttonState05);
  digitalWrite(ledPin06, buttonState06);

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
  lastButtonState01 = reading01;
  lastButtonState02 = reading02;
  lastButtonState03 = reading03;
  lastButtonState04 = reading04;
  lastButtonState05 = reading05;
  lastButtonState06 = reading06;
}

