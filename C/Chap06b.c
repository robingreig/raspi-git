#include <stdio.h>

# declare function
int sum_and_diff (int a, int b, int *res);

void main (void)
{
int b = 2;
int diff;
printf ("The sum of 5 and %d is %d\n", b, sum_and_diff (5, b, &diff));
printf ("The difference of 5 and %d is %d\n", b, diff);
}
# define function
int sum_and_diff (int a, int b, int *res)
{
	int sum;
	sum = a + b;
	*res = a - b;
	return sum;
}
