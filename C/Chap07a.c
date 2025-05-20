#include <stdio.h>
void main (void)
{
int a[10];
int count;
for (count = 0; count < 10; count++)
{
		 a[count] = count * 10 + count;
}
printf ("The first and second elements of a are %d and %d\n",
			a[0], a[1]);
printf ("Or, as pointers, %d and %d\n", *a, *(a+1));
}
