// RLG20141229

#include <avr/io.h>

int main(void)
{
	DDRB = 0b00000000;
	DDRB |= (1 << PB5);
	DDRB |= (1 << PB1);
	DDRD &= 0b01111111;
	PORTD |= 0b10000000;
	for(;;) {
		if (~PIND & (1 << PD7)) {
			PORTB |= (1 << PB5);
		} else {
			PORTB &= ~(1 << PB5);
		}
	}
	return 0;
}
