//
//
// Example code which uses the 32767KHz Crystal to
// implement a 1-second event handler
//
//
// Atmega Low power operation example
// Using a 32768 Khz crystal on timer 2 and full power down mode
// to implement a 1-second event handler
//
// This code is written for the GCC compiler
// Example program for the Gertduino Atmega 48PA device
// (This program wil NOT run on the 328!)
// This code is freeware
//


#include <avr/interrupt.h>
#include <avr/sleep.h>

volatile unsigned long count_seconds;    // 1 second time

main()
{
  // set PB0 as output
  DDRB = 0xFE;

// Set-up 32 KHz oscillator
  TIMSK2 = 0x00;     // No interrupts
  ASSR   = 0x20;     // async run from xtal
  TCNT2  = 0;        // clear counter
  TCCR2B = 0x05;     // prescale 5=/128, 6=/256, 7=/1024


  // Wait for all 'busy' bits to be clear
  // That happens on the first timer overflow
  // which can take 8 seconds if you have a max pre-scaler!!
  while (ASSR&0x07) ;

  TIMSK2 = 0x01;     // overflow IRQ enable

  count_seconds = 0; // clear seconds counter
  sei();             //set the Global Interrupt Enable Bit

  while (1)
  {
     SMCR = 0x7; // Go into lowest power sleep mode
     asm("sleep");
     asm("nop");
     // Interrupt woke us up
     // If we get here the interrupt routine has already been called

     // Toggle LED on port B0 using LS timer bit
     PORTB = count_seconds & 0x01;
  }
} // main

//
// Timer 2 overflow
// if we set timer2 up correctly this routine is called every second
//
ISR(TIMER2_OVF_vect)
{ count_seconds++; // all we do here is count seconds elapsed
}
