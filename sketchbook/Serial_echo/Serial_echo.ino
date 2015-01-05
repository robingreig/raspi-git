  /*

   Serial Echo
   Use to echo received characters between ><
   Written for 16MHz clock

  */

int spaces = 0;

void send_serial_string(char *str);

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);

  send_serial_string("Start of Serial Echo Program\r\n");
  
}

char str[128];
void loop()
{ volatile long wait;
  int inByte;
  inByte= -1;
  for (wait=0; wait<50000 && inByte==-1; wait++)
  { wait++;
    wait--;
    inByte = Serial.read();
  }
  if (inByte!=-1)
  {
    Serial.write('>');
    Serial.write(inByte);
    Serial.write('<');
    Serial.write('\r');
    Serial.write('\n');
  }
}

void send_serial_string(char *str)
{

while(*str)
  Serial.write(*str++);
}
