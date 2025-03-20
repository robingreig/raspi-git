#include <cstdio>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "one_wire.h"

#define TEMP_SENSE_GPIO_PIN 28
#define EXIT_GPIO_PIN 15

int main() {
  stdio_init_all();
  One_wire one_wire(TEMP_SENSE_GPIO_PIN);
  one_wire.init();
  gpio_init(EXIT_GPIO_PIN);
  gpio_set_dir(EXIT_GPIO_PIN, GPIO_IN);
  gpio_pull_up(EXIT_GPIO_PIN);
  sleep_ms(1);
  while (gpio_get(EXIT_GPIO_PIN)) {
    int count = one_wire.find_and_count_devices_on_bus();
    rom_address_t null_address{};
    one_wire.convert_temperature(null_address, true, true);
                sleep_ms(750);
    for (int i = 0; i < count; i++) {
      auto address = One_wire::get_address(i);
      printf("Address: %02x%02x%02x%02x%02x%02x%02x%02x\r\n", address.rom[0], address.rom[1], address.rom[2],
           address.rom[3], address.rom[4], address.rom[5], address.rom[6], address.rom[7]);
      printf("Temperature: %3.1foC\n", one_wire.temperature(address));
    }
  }
  return 0;
}
