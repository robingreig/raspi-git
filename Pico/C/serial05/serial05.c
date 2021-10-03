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
    // Initialize GPIO output
    //const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    const uint LED_PIN = 16;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
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
        // Wait for the serial input
        //if (fgets(buffer, 2, stdin) != NULL) {
	//  puts(buffer);
	//}
        //printf(buffer);
        uint16_t result = adc_read();
        //printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
        //printf("Voltage: %f V\n", result * conversion_factor);
	voltage = result * conversion_factor;
	if (voltage > 1.5) {
	  gpio_put(LED_PIN, 0);
//	  printf ("Voltage >  & LED off\n");
	}
	if (voltage < 1) {
	  gpio_put(LED_PIN, 1);
//	  printf ("Voltage < 0 & LED on\n");
	}
	if (voltage < 1.5) {
	  printf("%f V\n", voltage);
	}
	if (strcmp(buffer, "A") == 0) {
	  //printf("Voltage variable: %f V\n", voltage);
	  printf("%f V\n", voltage);
	  if (voltage > 1) {
	  printf ("Voltage > 1 & LED off\n");
	  } else {
	  printf ("Voltage < 1 & LED on\n");
	  }
	}
        sleep_ms(500);
    }
    return 0;
}
