// Motor demo using Gertduino and P3 shield 
// These are the connection for a motor shield P3
int Mdir1 = 12; // Motor 1 direction
int Mpwm1 = 3;  // Motor 1 on/off 
int Mbrk1 = 9;  // Motor 1 break (unused)
int Mdir2 = 13; // Motor 2 direction
int Mpwm2 = 11; // Motor 2 on/off
int Mbrk2 = 8;  // Motor 2 break (unused)
int inByte = 0; // incoming serial byte

void setup()
{ // define if pins are input or outputs 
  pinMode(Mdir1, OUTPUT);
  pinMode(Mpwm1, OUTPUT);
  pinMode(Mbrk1, OUTPUT);
  pinMode(Mdir2, OUTPUT);
  pinMode(Mpwm2, OUTPUT);
  pinMode(Mbrk2, OUTPUT);
  // set each pin low at the start 
  digitalWrite(Mdir1, LOW);
  digitalWrite(Mpwm1, LOW);
  digitalWrite(Mdir2, LOW);
  digitalWrite(Mpwm2, LOW);
  digitalWrite(Mbrk1, LOW);
  digitalWrite(Mbrk2, LOW);
  Serial.begin(9600); // start serial port at 9600 bps:  
}
// control motor 1 on/off forward/backward  
void mot1(int on,int dir)
{ digitalWrite(Mpwm1, on  ? HIGH : LOW );
  digitalWrite(Mdir1, dir ? HIGH : LOW);
}
// control motor 2 on/off forward/backward  
void mot2(int on,int dir)
{ digitalWrite(Mpwm2, on  ? HIGH : LOW );
  digitalWrite(Mdir2, dir ? HIGH : LOW);
}

void loop()
{ // if we get a valid byte, act on it
  if (Serial.available() > 0)
  { inByte = Serial.read();
    switch(inByte)  {
    case '1': mot1(1,1);            break; // left back
    case '2': mot1(1,1); mot2(1,1); break; // left & right back 
    case '3': mot2(1,1);            break; // right back
    case '4': mot1(0,0);            break; // Left stop 
    case '5': mot1(0,0); mot2(0,0); break; // left & right stop
    case '6': mot2(0,0);            break; // right stop 
    case '7': mot1(1,0);            break; // left forwards
    case '8': mot1(1,0); mot2(1,0); break; // left & right forward
    case '9': mot2(1,0);            break; // right forward
    }
  } // If serial avaiable.
} // main loop 
