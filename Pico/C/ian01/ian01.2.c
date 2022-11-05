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
    // Initialize variable 'voltage5min' which will take the average
    // voltage and convert it to milliseconds for the timer
    // voltage * 1.51515151 = 5 minutes max from 3.3V
    // voltage5min * 60 to make seconds from minutes
    // voltage5min * 1000 to make milliseconds
    float voltage5min;
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
//	wait 1 second between the 3 samples
	sleep_ms(000);
	voltageTotal = voltage + voltageTotal;
	printf("VoltageTotal = %f\n",voltageTotal);
	printf("Voltage Count = %d\n", voltageCount);
	// Print the average
	if (voltageCount == 2){
	    voltageTotal = voltageTotal / 3;
	    // Max Voltage = 3.3V = 5 minutes so voltage * 1.5151515151 = 5 minutes
	    voltage5min = voltageTotal * 1.5151515151;
	    printf("voltage5min = %f\n", voltage5min);
	    // Minutes to seconds
	    voltage5min = voltage5min * 60;
	    printf("voltage5min in seconds = %f\n", voltage5min);
	    // Seconds to milliseconds time_ms
	    voltage5min = voltage5min * 1000;
	    printf("voltage5min in milliSeconds = %f\n", voltage5min);
	    printf("Timing starting now\n");
	    gpio_put(LED_PIN1, 1);
	    gpio_put(LED_PIN2, 1);
	    voltageCount = 0;
	    voltageTotal = 0;
	    sleep_ms(voltage5min);
	    printf("Timing ending now\n");
	    gpio_put(LED_PIN1, 0);
	    gpio_put(LED_PIN2, 0);
	    sleep_ms(2000);
	    
	} else {
	    voltageCount++;
	}
    }
    return 0;
}
