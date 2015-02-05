// RLG20141229
// blink LED'S in sequence using the toggle ^ option

#include <avr/io.h> //for DDRB, PORTB, etc
#include <util/delay.h> // for _delay_ms
enum {
	blink_delay_ms = 200, //set delay time
};


int main(void)
{
	// Clear the DDRB register
	DDRB = 0x00;
	// Clear the DDRD register
	DDRD = 0x00;
	// Gertduino LED D5 = PB5, LED D6 = PB1, LED D7 = PB2
	DDRB |= (1 << DDB5);
	DDRB |= (1 << DDB1);
	DDRB |= (1 << DDB2);
	// Gertduino LED D8 = PD3, LED D9 = PD5, LED D10 = PD6
	DDRD |= (1 << DDB3);
	DDRD |= (1 << DDB5);
	DDRD |= (1 << DDB6);
	while (1) {
		PORTB ^= ((1 << PB5));
		_delay_ms(blink_delay_ms); // time delay set by blink_delay_ms variable
		PORTB ^= ((1 << PB1));
		_delay_ms (blink_delay_ms); // time delay set by blink_delay_ms variable
		PORTB ^= ((1 << PB2));
		_delay_ms (blink_delay_ms); // time delay set by blink_delay_ms variable
		PORTD ^= ((1 << PD3));
		_delay_ms (blink_delay_ms); // time delay set by blink_delay_ms variable
		PORTD ^= ((1 << PD5));
		_delay_ms (blink_delay_ms); // time delay set by blink_delay_ms variable
		PORTD ^= ((1 << PD6));
		_delay_ms (blink_delay_ms); // time delay set by blink_delay_ms variable
	}
	return 0;
}
