//
// Basic operating test Motor shield P3
//

// These are the connection for a motor shield P3
int Mdir1 = 12;
int Mpwm1 = 3;
int Mbrk1 = 9;
int Mdir2 = 13;
int Mpwm2 = 11;
int Mbrk2 = 8;

void setup() {
  
  pinMode(Mdir1, OUTPUT);
  pinMode(Mpwm1, OUTPUT);
  pinMode(Mbrk1, OUTPUT);
  pinMode(Mdir2, OUTPUT);
  pinMode(Mpwm2, OUTPUT);
  pinMode(Mbrk2, OUTPUT);
  
  digitalWrite(Mdir1, LOW);
  digitalWrite(Mpwm1, LOW);
  digitalWrite(Mdir2, LOW);
  digitalWrite(Mpwm2, LOW);

  digitalWrite(Mbrk1, LOW);
  digitalWrite(Mbrk2, LOW);
  
  
}

void mot1(int on,int dir)
{ digitalWrite(Mpwm1, on ? HIGH : LOW );
  digitalWrite(Mdir1, dir ? HIGH : LOW);
}

void mot2(int on,int dir)
{ digitalWrite(Mpwm2, on ? HIGH : LOW );
  digitalWrite(Mdir2, dir ? HIGH : LOW);
}


void loop()
{
  delay(1000);
  mot1(1,0);
  delay(1000);
  mot1(0,0);
  delay(200);
  mot1(1,1);
  delay(1000);
  mot1(0,0);
  delay(1000);
  mot2(1,0);
  delay(1000);
  mot2(0,0);
  delay(200);
  mot2(1,1);
  delay(1000);
  mot2(0,0);
  delay(1000);
  
}


