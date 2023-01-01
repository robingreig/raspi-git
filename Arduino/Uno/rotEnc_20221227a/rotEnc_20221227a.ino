/*Rotary Encoder #2
 * Rotary Encoder is monitored by interrupts
 * Only need to monitor DT since it changes state first / part way thru a turn
 */
// Rotary Encoder Inputs
#define CLK 2
#define DT 3

int counter = 0;
int currentStateCLK;
int lastStateCLK;
int currentStateDT;
int lastStateDT;
String currentDir ="";

void setup() {
  
  // Set encoder pins as inputs
  pinMode(CLK,INPUT);
  pinMode(DT,INPUT);

  // Setup Serial Monitor
  Serial.begin(9600);

  // Read the initial state of CLK
  lastStateCLK = digitalRead(CLK);
  lastStateDT = digitalRead(DT);
  
  // Call updateEncoder() when any high/low changed seen
  // on interrupt 0 (pin 2), or interrupt 1 (pin 3)
//  attachInterrupt(0, updateEncoder, CHANGE);
  attachInterrupt(1, updateEncoder, CHANGE);
}

void loop() {
  //Do some useful stuff here
}

void updateEncoder(){
  // Read the current state of DT
  currentStateDT = digitalRead(DT); 
  // Read the current state of CLK
  currentStateCLK = digitalRead(CLK);
  // If last and current state of DT are different, then pulse occurred
  // React to only 1 state change to avoid double count
//  if (currentStateCLK != lastStateCLK  && currentStateCLK == 1){
  if (currentStateDT != lastStateDT){

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (currentStateDT != currentStateCLK) {
      counter --;
      currentDir ="CCW";
    } else {
      // Encoder is rotating CW so increment
      counter ++;
      currentDir ="CW";
    }

    Serial.print("Direction: ");
    Serial.print(currentDir);
    Serial.print(" | Counter: ");
    Serial.println(counter);
  }

  // Remember last CLK state
  lastStateCLK = currentStateCLK;
  lastStateDT = currentStateDT;
}
