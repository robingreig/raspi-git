#include <stdio.h>

int sum (int a, int b)
{
int res;
res = a + b;
return res;
}

void main (void)
{
int y = 2;
int z = sum (5,y);

printf("The sum of 5 and %d is %d\n", y, z);
}
