#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

int main() {
    // Initialize variable 'buffer'
    char buffer[5];
    // Initialize variables for ADC inputs
    float voltage0;
    float voltage1;
    float voltage2;
    // Initialize variable 'conversion_factor'
    // 12-bit conversion, assume max value == ADC_VREF == 3.3 V
    const float conversion_factor = 3.3f / (1 << 12);

    // Initialize stdio
    stdio_init_all();

    //printf("ADC Example, measuring GPIO26\n");

    adc_init();

    // Make sure GPIO is high-impedance, no pullups etc
    adc_gpio_init(26);
    adc_gpio_init(27);
    adc_gpio_init(28);


    while (true) {
        //setup buffer to accept serial input
        fgets(buffer, 2, stdin);
        //printf(buffer);
	if (strcmp(buffer,"A") == 0) {
          // Select ADC input 0 (GPIO26)
          adc_select_input(0);
          uint16_t result = adc_read();
          //printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
          //printf("Voltage: %f V\n", result * conversion_factor);
	  voltage0 = result * conversion_factor;
	  //printf("Voltage variable: %f V\n", voltage);
	  printf("%f V\n", voltage0);
	}
	//if (strcmp(buffer,"B") == 0) {
	//  printf("4.54");
	//}
	if (strcmp(buffer, "B") == 0) {
          // Select ADC input 1 (GPIO27)
          adc_select_input(1);
          uint16_t result = adc_read();
          //printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
          //printf("Voltage: %f V\n", result * conversion_factor);
	  voltage1 = result * conversion_factor;
	  //printf("Voltage variable: %f V\n", voltage);
	  printf("%f V\n", voltage1);
	}
	if (strcmp(buffer, "C") == 0) {
          // Select ADC input 2 (GPIO27)
          adc_select_input(2);
          uint16_t result = adc_read();
          //printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
          //printf("Voltage: %f V\n", result * conversion_factor);
	  voltage2 = result * conversion_factor;
	  //printf("Voltage variable: %f V\n", voltage);
	  printf("%f V\n", voltage2);
	}
        sleep_ms(500);
    }
    return 0;
}
