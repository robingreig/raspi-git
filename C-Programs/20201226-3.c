#include <stdio.h>

void main (void)
{
int intval = 4033998788;
void *vptr = &intval;

printf("The value at vptr as in int is %d\n", *((int *) vptr));
printf("The vlue at vptr as a char is %d\n", *((char *) vptr));
}
