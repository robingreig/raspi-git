set(PROJECT  ds18b20)
cmake_minimum_required(VERSION 3.12)
set(PICO_BOARD pico)
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)
project(${PROJECT} C CXX)
pico_sdk_init()
add_executable(${PROJECT} ${PROJECT}.cpp)

target_sources(${PROJECT} PRIVATE
        ${PROJECT}.cpp
        one_wire.cpp
        one_wire.h
        )

target_include_directories(${PROJECT} PRIVATE ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(${PROJECT}
     pico_stdlib
)
pico_add_extra_outputs(${PROJECT})
pico_enable_stdio_usb(${PROJECT} 1)
pico_enable_stdio_uart(${PROJECT} 0)
