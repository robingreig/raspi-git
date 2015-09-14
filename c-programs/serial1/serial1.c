// first try at arduino serial comms using pure c
// 2015.09.10 Robin Greig

#define F_CPU 16000000UL	// Confirms clock frequency to compiler
#include <avr/io.h>		// General definitions of the register values
#include <util/delay.h>		// This is where the delay functions are located

#define BAUDRATE 9600
#define BAUD_PRESCALLER (((F_CPU / (BAUDRATE * 16UL))) - 1)
 
//Declaration of our functions
void USART_init(void);
unsigned char USART_receive(void);
void USART_send( unsigned char data);
void USART_putstring(char* StringPtr);
 
char String[]="Hello world!!";    
/*String[] is in fact an array but when we put the text between the " " symbols the compiler 
treats it as a String and automatically puts the null termination character in the end of the text*/
 
int main(void){		// Beginning of our main funtion
USART_init();        //Call the USART initialization code
 
while(1){        //Infinite loop
 USART_putstring(String);    //Pass the string to the USART_putstring function and sends it over the serial
 _delay_ms(5000);        //Delay for 5 seconds so it will re-send the string every 5 seconds
 }
 
return 0;		// All non void funtions must have a return
}

void USART_init(void){
 
 UBRR0H = (uint8_t)(BAUD_PRESCALLER>>8);
 UBRR0L = (uint8_t)(BAUD_PRESCALLER);
 UCSR0B = (1<<RXEN0)|(1<<TXEN0);
 UCSR0C = ((1<<UCSZ00)|(1<<UCSZ01));
}
void USART_send( unsigned char data){
 
 while(!(UCSR0A & (1<<UDRE0)));
 UDR0 = data;
 
}
void USART_putstring(char* StringPtr){
 
while(*StringPtr != 0x00){
 USART_send(*StringPtr);
 StringPtr++;}
 
}
