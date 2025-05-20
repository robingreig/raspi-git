#include <stdio.h>
#include <wiringPi.h>

#define LED_PIN 0 // GPIO17

int main(void)
{
	if (wiringPiSetup() == -1)
	{
		printf("Setup wiringPi failed!");
		return 1;
	}
	pinMode(LED_PIN, OUTPUT);
	while (1)
	{
		digitalWrite(LED_PIN, HIGH); // LED on
		delay(500);
		digitalWrite(LED_PIN, LOW); // LED off
		delay(500);
	}
	return 0;
}
