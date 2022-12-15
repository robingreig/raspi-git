#include <stdio.h>

int sum_and_diff (float a, int b, int *ans1, int *ans2, float *ans3)
{
  int sum;
  sum = a + b;
  *ans1 = a - b;
  *ans2 = a * b;
  *ans3 = a / b;
  return sum;
}

void main (void)
{
  float a;
  int b;
  printf("Enter first number: ");
  scanf("%f", &a);
  printf("You entered %.0f\n",a);
  printf("Enter second number: ");
  scanf("%d", &b);
  printf("You entered %d\n",b);
  int diff;
  int mult;
  float div;
  printf ("The sum of %.0f and %d is %d\n", a, b, sum_and_diff (a, b, &diff, &mult, &div));
  printf("The differenece of %.0f and %d is %d\n", a, b, diff);
  printf("The multiplication of %.0f & %d is %d\n", a, b, mult);
  printf("The division of %.0f & %d is %.2f\n", a, b, div);
}
