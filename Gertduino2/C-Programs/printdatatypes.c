// Example to print different data types
#include <stdio.h>

int main (){

	// initialize a variable of each type
	int integer;
	float decimal;
	char character;
	char *string;
	int willberounded;

	// assign each variable a value
	integer =1;
	decimal = 2.4;
	character = 'x';
	string = "Hello";
	willberounded = 0.4;

	// print out the contents of each variable
	printf("%s", "This printout contains:\n");
	printf("An integer: %i\na float %f\n", integer, decimal);
	printf("A character: %c\n", character);
	printf("And a string: %s\n", string);
	printf("A common error is trying to store ");
	printf("a variable in an int.\n");
	printf("0.4 = %d\n", willberounded);
	return 0;
}
