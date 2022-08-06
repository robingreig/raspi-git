#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

int main() {
    // Initialize variable 'buffer'
    char buffer[2];
    // Initialize variable 'voltage'
    float voltage;
    float voltageTotal = 0;
    int voltageCount = 0;
    // Initialize GPIO outputs
    // PICO_DEFAULT_LED_PIN will show visual indication of status
    const uint LED_PIN1 = PICO_DEFAULT_LED_PIN;
    // AND pin 16 will be used to control the relay
    const uint LED_PIN2 = 16;
    gpio_init(LED_PIN1);
    gpio_set_dir(LED_PIN1, GPIO_OUT);
    gpio_init(LED_PIN2);
    gpio_set_dir(LED_PIN2, GPIO_OUT);
    // Initialize variable 'conversion_factor'
    // 12-bit conversion, assume max value == ADC_VREF == 3.3 V
    const float conversion_factor = 3.3f / (1 << 12);
    // Initialize stdio
    stdio_init_all();
    // Initialize adc
    adc_init();
    // Make sure GPIO is high-impedance, no pullups etc
    adc_gpio_init(26);
    // Select ADC input 0 (GPIO26)
    adc_select_input(0);

    while (true) {
 	// Read the adc input 0
        uint16_t result = adc_read();
        printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
        printf("Voltage: %f V\n", result * conversion_factor);
	voltage = result * conversion_factor;
	sleep_ms(2000);
	voltageTotal = voltage + voltageTotal;
	voltageCount ++;
	
	if (voltageCount == 2){
	    printf("%f\n",voltage);
	    voltageCount = 0;
	}
	if (voltage < 1) {
	  gpio_put(LED_PIN1, 1);
	  gpio_put(LED_PIN2, 1);
	}
	/* not using else becasue I want the charger to turn on at a
	 * lower value and turn off at a higher value */ 
	if (voltage > 2) {
	  gpio_put(LED_PIN1, 0);
  	  gpio_put(LED_PIN2, 0);
	}

        sleep_ms(5000);
    }
    return 0;
}
