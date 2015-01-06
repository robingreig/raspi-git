// RLG20141229

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB |= 0b00100110; // leave all the other bits alone, just set bit 1 (PB1), 2 (PB2), & 5 (PB5) by or'ing with 00100110
	DDRC &= 0b11111011; // leave all the other bits alone, just clear bit 2 (PC2) by anding with 1111 1011
//	PORTC |= (1 << PC2); // set pull up resistor on PC2
	PORTC |= 0b00000100; // set pull up resistor on PC2 by or'ing with 00000100
	while (1) {
		if (PINC & (1 << PC2)) { //  pinc & 1 only until the button is pressed
//			PORTB &= ~(1 << PB5);
			PORTB &= 0b11011111; // if the button is not pressed then PB5 = 0
		} else {
//			PORTB |= (1 << B5); // if the button is pressed then PB5 = 1
			PORTB |= 0b00100000; // if the button is pressed then PB5 = 1
		}
	}
	return(0);
}
