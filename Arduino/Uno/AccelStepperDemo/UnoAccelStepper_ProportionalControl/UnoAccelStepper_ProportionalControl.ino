/*
   Uno sketch to drive a stepper motor using the AccelStepper library.
   Works with a ULN-2003 unipolar stepper driver, or a bipolar, constant voltage motor driver
   such as the L298 or TB6612, or a step/direction constant current driver like the a4988.
// Make a single stepper follow the analog value read from a pot or whatever
// The stepper will move at a constant speed to each newly set posiiton,
// depending on the value of the pot.
// Copyright (C) 2012 Mike McCauley

   12-27-21 Solve problem with original version is that the motor "judders" when pot is not being moved.
       --jkl  jlarson@pacifier.com
*/

// Include the AccelStepper Library
#include <AccelStepper.h>

// Motor Connections (unipolar motor driver)
const int In1 = 8;
const int In2 = 9;
const int In3 = 10;
const int In4 = 11;
// Motor Connections (constant voltage bipolar H-bridge motor driver)
const int AIn1 = 8;
const int AIn2 = 9;
const int BIn1 = 10;
const int BIn2 = 11;
// Motor Connections (constant current, step/direction bipolar motor driver)
const int dirPin = 4;
const int stepPin = 5;

// Creates an instance - Pick the version you want to use and un-comment it. That's the only required change.
//AccelStepper myStepper(AccelStepper::FULL4WIRE, AIn1, AIn2, BIn1, BIn2);  // works for TB6612 (Bipolar, constant voltage, H-Bridge motor driver)
//AccelStepper myStepper(AccelStepper::FULL4WIRE, In1, In3, In2, In4);    // works for ULN2003 (Unipolar motor driver)
AccelStepper myStepper(AccelStepper::DRIVER, stepPin, dirPin);           // works for a4988 (Bipolar, constant current, step/direction driver)

// pot reading must move out of this band to cause motion - avoid judder
#define DEADBAND 5

// This defines the analog input pin for reading the control voltage
// Tested with a 10k linear pot between 5v and GND
#define ANALOG_IN A0

// This is a handy routine for viewing the data direction registers for ports b and d.
/*
void printPinMode()
{
    char pbuffer[20];
    Serial.print(F("DDRB: "));
    snprintf(pbuffer, 5, "%02X", DDRB);
    Serial.print(pbuffer);
    Serial.print(F("  DDRD: "));
    snprintf(pbuffer, 5, "%02X", DDRD);
    Serial.println(pbuffer);
}
*/
void setup()
{
  Serial.begin(115200);
//  printPinMode();    // just for testing
  myStepper.setMaxSpeed(200.);
}

void loop()
{
  static int oldReading = 0;  // old ADC reading
  static bool printOnce = false;   // print flag
  // Read new position  - four averages to cut noise.
  int analog_in = (analogRead(ANALOG_IN) + analogRead(ANALOG_IN)+ analogRead(ANALOG_IN)+ analogRead(ANALOG_IN))/4;
  if ((analog_in > (oldReading + DEADBAND)) || (analog_in < (oldReading - DEADBAND))) {
    myStepper.moveTo((long)analog_in);
    myStepper.setSpeed(100.);   // set speed MUST be called after calling moveTo - MoveTo calculates a new speed! Needed if runSpeedToPosition is used.
    oldReading = analog_in;
    printOnce = true;
  }
  if (myStepper.distanceToGo() != 0) {
    myStepper.runSpeedToPosition();
  } else if (printOnce == true) {
    Serial.print(oldReading);
    Serial.print ("   ");
    Serial.print(myStepper.currentPosition());
    Serial.print ("   ");
    Serial.println(myStepper.targetPosition());
    printOnce = 0;
  }
}
