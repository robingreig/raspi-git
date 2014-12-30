// Robin Greig 2014.12.29 blink 1 led

#include <avr/io.h>

int main(void)
{
	DDRB = 127;
	PORTB = 4;
}
