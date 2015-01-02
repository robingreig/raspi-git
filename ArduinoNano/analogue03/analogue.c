// RLG20141229
// analogue.c = read an analogue voltage and vary the # of LED's on a bar graph

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	volatile unsigned int val;
	DDRB = 0xff; // set all PORTB to outputs
	DDRD = 0xff; // set all PORTD to outputs
	DDRD &= 0b01111111; // set PD7 to input
	PORTC |= 0x01; //Set A0, PC0 as an analogue input
	PORTD |= 0b10000000; // set the pull up resistor for PD7 (pushbutton to ground)
	ADMUX |= (1 << REFS0);
	ADCSRA |= (1 << ADPS1) | (1 << ADPS0);  // prescale of 8 (1MHz >> 125KHz)
	ADCSRA |= (1 << ADEN);
	for(;;) {
		if (~PIND & (1 << PD7)) { // if PD7 pushbutton is pressed & drops to 0V, then show bar graph
			for(int display = 0; display < 50; display++) { // setup delay so that bar graph only shows for ~5sec
	 			ADCSRA |= (1 << ADSC);
				while (ADCSRA & (1 << ADSC)) { // Not sure.... while I'm still reading an analogue value???
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
					_delay_ms (100); // delay for bar graph
				}
			}
		}
	PORTB &= 0b11011001; // reset bar graph back to off
	PORTD &= 0b10010111; // reset bar graph back to off
	}
	return(0);
}
