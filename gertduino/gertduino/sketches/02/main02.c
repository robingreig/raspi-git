// RLG20141229

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB = _BV(PB2);
	for(;;){
		PORTB = _BV(PB2);
		_delay_ms(1000);
		PORTB = 0;
		_delay_ms(1000);
	}
	return 0;
}
