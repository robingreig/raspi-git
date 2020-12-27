#include <stdio.h>

int sum_and_diff (int a, int b, int *res, int *prod, float *div)
{
int sum;
sum = a + b;
*res = a - b;
*prod = a * b;
*div = a / b;
printf("Location of div = %d\n",&div);
printf("Value of div = %f\n",*div);

return sum;
}

void main (void)
{
int a = 9;
int b = 2;
int diff;
int prod;
float div;

printf("The sum of %d and %d is %d\n",a, b, sum_and_diff(a, b, &diff, &prod, &div));
printf("The difference of %d and %d is %d\n",a, b, diff);
printf("The product of %d and %d is %d\n",a, b, prod);
printf("The division of %d and %d is %f\n",a, b, div);
}
