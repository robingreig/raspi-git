#include <stdio.h>
void main (void)
{
int val = 12;
char string[30];
char * ptr_to_string = "Test_string";

sprintf(string, "The value of val is %d\n", val);
printf("%s", string);
printf("The variable locations for string is: %d\n",&string);
printf("The address of the pointer is: %s\n",ptr_to_string);
ptr_to_string = "Something";
printf("The address of the pointer is: %d\n",&ptr_to_string);
}
