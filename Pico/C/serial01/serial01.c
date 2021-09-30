#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"

int main() {
    char buffer[5];
    stdio_init_all();
    while (true) {
        //printf("Hello, world!\n");
        //putchar('z');
        //sleep_ms(1000);
        fgets(buffer, 2, stdin);
        //printf(buffer);
	if (strcmp(buffer,"A") == 0) {
	  printf("123");
	}
	if (strcmp(buffer,"B") == 0) {
	  printf("4.54");
	}
    }
    return 0;
}
