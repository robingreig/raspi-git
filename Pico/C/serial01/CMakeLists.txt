cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(serial01
  serial01.c
)
pico_enable_stdio_usb(serial01 1)
pico_enable_stdio_uart(serial01 1)
pico_add_extra_outputs(serial01)
target_link_libraries(serial01 pico_stdlib)
