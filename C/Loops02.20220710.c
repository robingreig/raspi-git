#include <stdio.h>

void main (void)
{
	int a = 5;
	
	do
	{
		printf("a is equal to %d\n", a);
		a++;
	} while (a < 5);
	printf ("a is equal to %d and I've finished!\n", a);
}
