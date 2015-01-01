// RLG20141229
// analogue.c = read an analogue voltage and vary the brightness of an LED

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
//	volatile unsigned int val, val2;
	volatile unsigned int val;
	DDRB |= 0xff;
	DDRD |= 0xff;
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
		if (val > 200) {
			PORTB |= 0b00100000; // set PB5 to 1
		} else {
			PORTB &= 0b11011111; // set PB5 to 0
		}
		if (val > 300) {
			PORTB |= 0b00000010; // set PB2 to 1
		} else {
			PORTB &= 0b11111101; // set PB2 to 0
		}
		if (val > 400) {
			PORTB |= 0b00000100; // set PB3 to 1
		} else {
			PORTB &= 0b11111011; // set PB3 to 0
		}
		if (val > 500) {
			PORTD |= 0b00001000; // set PD3 to 1
		} else {
			PORTD &= 0b11110111; // set PD3 to 0
		}
		if (val > 600) {
			PORTD |= 0b00100000; // set PD5 to 1
		} else {
			PORTD &= 0b11011111; // set PD5 to 0
		}
		if (val > 700) {
			PORTD |= 0b01000000; // set PD6 to 1
		} else {
			PORTD &= 0b10111111; // set PD6 to 0
		}
	}
	return(0);
}
