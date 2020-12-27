#include <stdio.h>

void main (void)
{
float a = 9;
float b = 2;
float sum = a+b;
float diff = a-b;
float prod = a*b;
float div = a/b;

printf("The sum of %.0f and %.0f is %.2f\n",a, b, sum);
printf("The difference of %.0f and %.0f is %.2f\n",a, b, diff);
printf("The product of %.0f and %.0f is %.2f\n",a, b, prod);
printf("The division of %.0f and %.0f is %.2f\n",a, b, div);
}
