This Tar ball contains demo and example programs for the Gertduino,
as well as a LED matrix program for the Gertboard.
 - blink
   contains the example blink program for the 328p
   as found in the gertduino manual.
 - low_power
   contains the example low power program for the 48pa
   as found in the gertduino manual.
 - arduino_sketchbook
   contains 4 programs in the arduino GUI/sketchbook format.
   o blink
     An led blink program like the C-blink but without buttons
   o Motor_demo
     A program which uses RS232 and a P3 motor shield to control two motors
   o Motor-test
     A simple program to see if your P3 shield is working
   o Serial_startup
     A simple program to test your serial link.

It also has some shell scripts to make life easier:
 - reset_off
   Remove reset from the Atmega so it can run.
   (Sets GPIO pin 8 high, which is the reset of the Atmega chip when
   the programming jumpers are in place.)
 - reset_on
   Asserts the reset on the Atmega so it stops running.
   (Sets GPIO pin 8 low, which is the reset of the Atmega chip when
   the programming jumpers are in place.)
 - progam_48
 - program_328
   These program the 328 or 48 chip.
   For details see the gertduino manual






