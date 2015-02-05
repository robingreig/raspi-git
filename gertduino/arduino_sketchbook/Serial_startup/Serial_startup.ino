  /*

   Serial Sartup
   Use to get your serial comport working.
   This program outputs a pattern without flooding
   the output too much.
   It echo's received characters between ><
   Written for 16MHz clock

  */

int spaces = 0;

void send_serial_string(char *str);

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);

  send_serial_string("Hello world!\r\n");

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
  { Serial.write('>');
    Serial.write(inByte);
    Serial.write('<');
  }
  for (wait=0; wait<spaces; wait++)
     Serial.write(' ');
  spaces++;
  if (spaces>20)
    spaces = 0;
  send_serial_string("Hi\r\n");
}

void send_serial_string(char *str)
{

while(*str)
  Serial.write(*str++);

}
