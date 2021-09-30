#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

int main() {
    // Initialize variable 'buffer'
    char buffer[5];
    // Initialize variable 'voltage'
    float voltage;
    // Initialize variable 'conversion_factor'
    // 12-bit conversion, assume max value == ADC_VREF == 3.3 V
    const float conversion_factor = 3.3f / (1 << 12);

    // Initialize stdio
    stdio_init_all();

    printf("ADC Example, measuring GPIO26\n");

    adc_init();

    // Make sure GPIO is high-impedance, no pullups etc
    adc_gpio_init(26);
    // Select ADC input 0 (GPIO26)
    adc_select_input(0);


    while (true) {
        //printf("Hello, world!\n");
        //putchar('z');
        fgets(buffer, 2, stdin);
        //printf(buffer);
	if (strcmp(buffer,"A") == 0) {
	  printf("123");
	}
	if (strcmp(buffer,"B") == 0) {
	  printf("4.54");
	}
        uint16_t result = adc_read();
        //printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
        //printf("Voltage: %f V\n", result * conversion_factor);
	voltage = result * conversion_factor;
	if (strcmp(buffer, "C") == 0) {
	  //printf("Voltage variable: %f V\n", voltage);
	  printf("%f V\n", voltage);
	}
        sleep_ms(500);
    }
    return 0;
}
