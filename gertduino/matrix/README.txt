
The Matrix demo shows how to operate a 5x5 LED matrix
using the gertboard. The demo consists of two programs:
 - matrix.c
This is the real matric demo program
 - matrix_pattern.c
 This is a program to convert a test file into pattern bits
 (Hand coding a 5x5 matrix into a 25-bit vector is non-trivial)



Each can be compiled using:
gcc matrix.c -o matrix
gcc matrix_pattern.c -o matrix_pattern
or by typing 'make' in the command line

The matrix.c program uses default the patterns stored in
an include file called "pattern1.h"


The matrix_pattern program generates a file for the matrix.c program.
This was a quick hack.

Use it as follows:
matrix_pattern <inputfile_in_text> <outputfile>
For example:
matrix_pattern pattern1.txt pattern1.h
Then you must re-compile the matrix program.


For the rest: read the code.



