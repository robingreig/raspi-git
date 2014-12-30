// RLG20141229

#include <avr/io.h>

int main(void)
{
	DDRB = 0b00000000;
	DDRB |= (1 << PB5);
	DDRB |= (1 << PB1);
	PORTC |= (1 << PC2);
	PORTC |= (1 << PC3);
	for(;;) {
		if (PINC & (1 << PC2)) {
			PORTB &= ~(1 << PB5);
		} else {
			PORTB |= (1 << PB5);
		}
		if (PINC & (1 << PC3)) {
			PORTB &= ~(1 << PB1);
		} else {
			PORTB |= (1 << PB1);
		}
	}
	return 0;
}
