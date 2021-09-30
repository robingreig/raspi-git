cmake_minimum_required(VERSION 3.16)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(serial02
        serial02.c
        )

target_link_libraries(serial02 pico_stdlib hardware_adc)

# create map/bin/hex file etc.
pico_add_extra_outputs(serial02)

# add url via pico_set_program_url
#####example_auto_set_url(serial02)


#cmake_minimum_required(VERSION 3.13)

#include(pico_sdk_import.cmake)

#project(test_project C CXX ASM)
#set(CMAKE_C_STANDARD 11)
#set(CMAKE_CXX_STANDARD 17)
#pico_sdk_init()

#add_executable(serial01
#  serial01.c
#)

#        pico_enable_stdio_usb(serial01 1)
pico_enable_stdio_uart(serial02 1)
#pico_add_extra_outputs(serial01)
#target_link_libraries(serial01 pico_stdlib)
