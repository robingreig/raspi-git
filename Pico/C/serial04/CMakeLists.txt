cmake_minimum_required(VERSION 3.16)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(serial04
        serial04.c
        )

target_link_libraries(serial04 pico_stdlib hardware_adc)

# create map/bin/hex file etc.
pico_add_extra_outputs(serial04)

# add url via pico_set_program_url
#####example_auto_set_url(serial02)

#pico_enable_stdio_usb(serial01 1)
pico_enable_stdio_uart(serial04 1)
