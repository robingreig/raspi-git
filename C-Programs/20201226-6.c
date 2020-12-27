#include <stdio.h>

int sum_and_diff (int a, int b, int *res, int *prod)
{
int sum;
sum = a + b;
*res = a - b;
*prod = a * b;
return sum;
}

void main (void)
{
int a = 9;
int b = 2;
int diff;
int prod;

printf("The sum of %d and %d is %d\n",a, b, sum_and_diff(a, b, &diff, &prod));
printf("The difference of %d and %d is %d\n",a, b, diff);
printf("The product of %d and %d is %d\n",a, b, prod);
}
