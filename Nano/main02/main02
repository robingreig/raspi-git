// Robin Greig 2014.12.29 blink 1 led

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB = 0xff; // Set all pins of PORTB to outputs
	while (1) {
		PORTB |= 0b00100000; // Set PB5 high
		_delay_ms(300);
		PORTB &= 0b11011111; // Set PB low
		_delay_ms(300);
	}
	return 0;
}
