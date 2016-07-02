import processing.io.*; // use the GPIO library

int buttonAX = 20;
int buttonAY = 20;
int buttonAW = 50;
int buttonAH = 50;

// store the desired state of the LED in a variable
boolean ledOn = false; 

void setup() {
  // set pin 17 as an output:
  GPIO.pinMode(17, GPIO.OUTPUT);
  // set size & fill of ButtonA
  size(700,500);
  fill(255,0,0);
}

void draw() {
  // set the background
  background(0,100,0);
  //draw button A
  rect(buttonAX, buttonAY, buttonAW, buttonAH);
  if (ledOn == true) { // If the desired state is on, then:
    // turn the LED on:
    GPIO.digitalWrite(17, GPIO.HIGH);
    fill(0,255,0);
  }
  else { // otherwise:
    // turn the LED off:
    GPIO.digitalWrite(17, GPIO.LOW);
    fill(255,0,0);
  }
}

void mousePressed() {
 // when the mouse button is pressed, check to see if it is withing the square
 // if it is, change the color of the square
 //if ((mouseX >= u) && (mouseX <= (u+x) && (mouseY >= v) && (mouseY <= (v+y)) {
 if ((mouseX >= buttonAX) && (mouseX <= (buttonAX+buttonAW)) && (mouseY >= buttonAY) && (mouseY <= (buttonAY+buttonAH))){
   ledOn = !ledOn;
 } 
}