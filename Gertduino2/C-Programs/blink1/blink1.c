#include <avr/io.h>
#include <util/delay.h>

#define BlinkDelayMS 1000

int main (void)
{
// set pin 5 of PORTB for output
DDRB |= _BV(DDB5);

while(1){
  //set pin 5 high to turn led on
  PORTB |= _BV(PORTB5);
  _delay_ms(BlinkDelayMS);

  //set pin 5 low to turn led off
  PORTB &= ~_BV(PORTB5);
  _delay_ms(BlinkDelayMS);
  }
}
