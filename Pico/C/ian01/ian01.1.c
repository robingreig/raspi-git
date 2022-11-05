#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

int main() {
    // Initialize variable 'buffer'
    char buffer[2];
    // Initialize variable 'voltage' = adc * conversion factor
    float voltage;
    // Initialize variable 'voltageTotal' which will take 3 readings
    // and average them 
    float voltageTotal = 0;
    // Initialize variable 'voltage15' which will take the average
    // voltage and convert it back to the 0 - 15V battery voltage
    float voltage15;
    // Initialize variable voltageCount to count to 3 for the average
    int voltageCount = 0;
    // Initialize variable 'conversion_factor'
    // 12-bit conversion, assume max value == ADC_VREF == 3.3 V
    const float conversion_factor = 3.3f / (1 << 12);
    // Initialize GPIO outputs
    // PICO_DEFAULT_LED_PIN will show visual indication of status
    const uint LED_PIN1 = PICO_DEFAULT_LED_PIN;
    // GPIO pin 16 will be used to control the relay
    const uint LED_PIN2 = 16;
    gpio_init(LED_PIN1);
    gpio_set_dir(LED_PIN1, GPIO_OUT);
    gpio_init(LED_PIN2);
    gpio_set_dir(LED_PIN2, GPIO_OUT);
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
        voltage = result * conversion_factor;
//	wait 5 seconds between the 3 samples
	sleep_ms(5000);
	voltageTotal = voltage + voltageTotal;
//	printf("VoltageTotal = %f\n",voltageTotal);
//	printf("Voltage Count = %d\n", voltageCount);
	// Print the average
	if (voltageCount == 2){
	    voltageTotal = voltageTotal / 3;
	    // Max battery = 15V, max Pico = 3.3V, divider = 15/3/3 = 4.5454545454
	    voltage15 = voltageTotal * 4.5454545454;
	    printf("%f\n", voltage15);
	    voltageCount = 0;
	    voltageTotal = 0;
	    sleep_ms(15000);
	} else {
	    voltageCount++;
	}
	// turn GPIO16 on if below 11V / 4.5454545454 = 2.42
	if (voltage < 2.42) {
	  gpio_put(LED_PIN1, 1);
	  gpio_put(LED_PIN2, 1);
	}
	/* not using else becasue I want the charger to turn on at a
	 * lower value and turn off at a higher value 
	 * turn GPIO16 off if above 14.4V / 4.5454545454 = 3.168*/ 
	if (voltage > 3.168) {
	  gpio_put(LED_PIN1, 0);
  	  gpio_put(LED_PIN2, 0);
	}
    }
    return 0;
}
