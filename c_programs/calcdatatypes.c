/*
 * calcdatatypes.c
 * 
 * Copyright 2014.12.29 robin <robin@raspi24>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdio.h>

int main(int argc, char **argv)
{
	float a=3;
	float b=4;
	float c=a+b;
	float product=a*b;
	float divisor=a/b;
	printf("a + b = %.02f\n", c);
	printf("a + b = %.02f\n", a+b);
	printf("a * b = %.02f\n", product);
	printf("a / b = %.02f\n", divisor);
	return 0;
}

