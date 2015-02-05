#
# Simplest makefile
#

matrix: matrix.c pattern1.h
	gcc matrix.c -o matrix
	@echo use \'sudo ./matrix\' to run

pattern1.h : pattern1.txt matrix_pattern
	./matrix_pattern pattern1.txt pattern1.h

matrix_pattern: matrix_pattern.c
	gcc matrix_pattern.c -o matrix_pattern
