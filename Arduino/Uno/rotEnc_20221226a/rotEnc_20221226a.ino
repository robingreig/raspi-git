/* Rotary Encoder #1
 *  monitors state in while loop
 *  from lastminuteengineer.com
 *  had to swap the if statement from CLK to Dt
 *  every turn changes DT first then CLK
 */
// Rotary Encoder Inputs
#define CLK 2
#define DT 3
#define SW 4

int counter = 0;
int currentStateCLK;
int lastStateCLK;
int currentStateDT;
int lastStateDT;
String currentDir ="";
unsigned long lastButtonPress = 0;

void setup() {
  
  // Set encoder pins as inputs
  pinMode(CLK,INPUT);
  pinMode(DT,INPUT);
  pinMode(SW, INPUT_PULLUP);

  // Setup Serial Monitor
  Serial.begin(4800);

  // Read the initial state of CLK
  lastStateCLK = digitalRead(CLK);
  lastStateDT = digitalRead(DT);
}

void loop() {
  
  // Read the current state of CLK
  currentStateCLK = digitalRead(CLK);
  currentStateDT = digitalRead(DT);
//  Serial.print("currentStateCLK = ");
//  Serial.println(currentStateCLK);
//  Serial.print("lastStateCLK = ");
//  Serial.println(lastStateCLK);
//  Serial.print("digitalRead(DT)");
//  Serial.println(digitalRead(DT));  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
//  if (currentStateCLK != lastStateCLK  && currentStateCLK == 1){
  if (currentStateDT != lastStateDT){
    Serial.println("Entering IF statement");
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
//    Serial.print("digitalRead(DT)");
//    Serial.println(digitalRead(DT));
    Serial.print("Direction: ");
    Serial.print(currentDir);
    Serial.print(" | Counter: ");
    Serial.println(counter);
  }

  // Remember last CLK state
  lastStateCLK = currentStateCLK;
  lastStateDT = currentStateDT;

  // Read the button state
  int btnState = digitalRead(SW);

  //If we detect LOW signal, button is pressed
  if (btnState == LOW) {
    //if 50ms have passed since last LOW pulse, it means that the
    //button has been pressed, released and pressed again
    if (millis() - lastButtonPress > 50) {
      Serial.println("Button pressed!");
    }

    // Remember last button press event
    lastButtonPress = millis();
  }

  // Put in a slight delay to help debounce the reading
  delay(1);
}
