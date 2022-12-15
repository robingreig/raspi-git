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
  int b = 2;
  int diff;
  int mult;
  float div;
  printf ("The sum of 5 and %d is %d\n", b, sum_and_diff (5, b, &diff, &mult, &div));
  printf("The differenece of 5 and %d is %d\n", b, diff);
  printf("The multiplication of 5 & %d is %d\n", b, mult);
  printf("The division of 5 & %d is %.2f\n", b, div);
}
