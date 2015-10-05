// RLG20141229
// analogue.c = read an analogue voltage and vary the brightness of an LED

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
//	volatile unsigned int val, val2;
	volatile unsigned int val;
	DDRB |= 0xff;
	PORTC |= 0x01;
	//ADMUX |= (1 << ADLAR); // left-adjust result
	ADMUX |= (1 << REFS0);
	ADCSRA |= (1 << ADPS1) | (1 << ADPS0);  // prescale of 8 (1MHz >> 125KHz)
	ADCSRA |= (1 << ADEN);
	for(;;) {
		ADCSRA |= (1 << ADSC);
		while (ADCSRA & (1 << ADSC))
			;
		val = ADCL;
		val = (ADCH << 8) | val;
		// val = ADCH;
		PORTB |= 0b00100000;
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		PORTB &= ~0b00100000;
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		_delay_loop_2(val << 6);
		if (val > 1000) {
			PORTB |= 0b00000100;
		} else {
			PORTB &= 0b11111011;
		}
	}
	return(0);
}
