#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/watchdog.h"

int main() {
	stdio_init_all();

	if (watchdog_caused_reboot()) {
		printf("Rebooted by Watchdog!\n");
//		return 0;
	} else {
		printf("Clean boot\n");
	}

// Enable the watchdog, requiring update every 100mS or chip will reboot
// Second arg is pause on debug
	watchdog_enable(2000, 1);

	for (uint i = 0; i < 5; i++ ) {
		printf("Updating watchdog %d\n", i);
		watchdog_update();
		sleep_ms(500);
	}

// Wait in infinite loop and don't update watchdog
	printf("Waiting to be rebootd by Watchdog\n");
	while(1);
}
