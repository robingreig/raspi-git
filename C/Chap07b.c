#include <stdio.h>
void main (void)
{
float a[10] = {1.23, 2.34};
printf ("The first and second elements of a are %.2f and %.2f\n",
			a[0], a[1]);
printf ("Or, as pointers, %d and %d\n", *a, *(a+1));
}
