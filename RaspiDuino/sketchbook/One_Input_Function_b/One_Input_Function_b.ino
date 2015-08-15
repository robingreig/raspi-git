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

// Variables will change:
int ledState1 = HIGH;         // the current state of the output pin
int buttonState1 = HIGH;             // the current reading from the input pin
int lastButtonState1 = LOW;   // the previous reading from the input pin

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime1 = 0;  // the last time the output pin was toggled
long debounceDelay1 = 50;    // the debounce time; increase if the output flickers

void setup() {
  serial.begin(9600);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(ledPin1, OUTPUT);
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

  // set the LED using the state of the button:
////  digitalWrite(ledPin1, buttonState1);

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
////  lastButtonState1 = reading1;
}

