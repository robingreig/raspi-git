#!/usr/bin/python3

import board
import digitalio
import busio

print("Hello Blinka!")

# Try to create a Digital Input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO OK!")

# Try to create an i2c device
i2c = busio.I2C(board.SCL, board.SDA)
print("i2c OK!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI OK!")

print("Done!")


