#include <Wire.h>
 
#define SLAVE_ADDRESS 0x04
int number = 0;
int state1 = 0;
int state3 = 0;
int state4 = 0;

double temp;

// callback for received data
void receiveData(int byteCount){
 
 while(Wire.available()) {
  number = Wire.read();
 
  if (number == 1){
   if (state1 == 0){
    digitalWrite(13, HIGH); // set the LED on
    state1 = 1;
   } else{
    digitalWrite(13, LOW); // set the LED off
    state1 = 0;
   }
  }

  if(number==2) {
   number = (int)temp;
  }

  if (number == 3){
   if (state3 == 0){
    digitalWrite(8, HIGH); // set the LED on
    state3 = 1;
   } else{
    digitalWrite(8, LOW); // set the LED off
    state3 = 0;
   }
  }

  if (number == 4){
   if (state4 == 0){
    digitalWrite(9, HIGH); // set the LED on
    state4 = 1;
   } else{
    digitalWrite(9, LOW); // set the LED off
    state4 = 0;
   }
  }
 
 }
}
 
// callback for sending data
void sendData(){
 Wire.write(number);
}
 
// Get the internal temperature of the arduino
double GetTemp(void)
{
 unsigned int wADC;
 double t;
 ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
 ADCSRA |= _BV(ADEN); // enable the ADC
 delay(20); // wait for voltages to become stable.
 ADCSRA |= _BV(ADSC); // Start the ADC
 while (bit_is_set(ADCSRA,ADSC));
 wADC = ADCW;
 t = (wADC - 324.31 ) / 1.22;
 return (t);
}
 
void setup() {
 pinMode(13, OUTPUT);
 pinMode(8, OUTPUT);
 pinMode(9, OUTPUT);
 
 // initialize i2c as slave
 Wire.begin(SLAVE_ADDRESS);
 
 // define callbacks for i2c communication
 Wire.onReceive(receiveData);
 Wire.onRequest(sendData);
}
 
void loop() {
 delay(100);
 temp = GetTemp();
}
 
