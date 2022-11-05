cmake_minimum_required(VERSION 3.16)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(ian01
        ian01.c
        )

target_link_libraries(ian01 pico_stdlib hardware_adc)

# create map/bin/hex file etc.
pico_add_extra_outputs(ian01)

#pico_enable_stdio_usb(serial01 1)
pico_enable_stdio_uart(ian01 1)
