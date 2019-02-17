// comment: Adding 2 numbers together
#include <stdio.h>

void main (void)
{
    int a[10];
    int count;
    
    for (count = 0; count < 10; count++)
    {
		a[count] = count * 10 + count;
	}
    printf ("The first % second elements of a are %d and %d\n", a[0], a[1]);
    printf ("The third & fourth elements of a are %d and %d\n", a[2], a[3]);
    printf ("The fifth & sixth elements of a are %d and %d\n", a[4], a[5]);
    printf ("The seventh & eighth elements of a are %d and %d\n", a[6], a[7]);
    printf ("The ninth & tenth elements of a are %d and %d\n", a[8], a[9]);
    printf ("Or as pointers,  %d and %d\n", *a, *(a+1));
}
