import board
import time
import busio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20


# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.GP22)

# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

displayio.release_displays()

#i2c = busio.I2C (scl=board.GP5, sda=board.GP4) # This RPi Pico way to call I2C
i2c = busio.I2C (scl=board.GP27, sda=board.GP26) # This RPi Pico way to call I2C

display_bus = displayio.I2CDisplay (i2c, device_address = 0x3C) # The address of my Board

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

font_file = "fonts/Roboto48.bdf"

# Main loop to print the temperature every second.
while True:
    #print("Temperature: {0:0.1f}C".format(ds18.temperature))
    temp = (ds18.temperature)
    #print (temp)
    nofloat = ('%.0f' %temp)
    #print('%.0f' %temp)
    #print(nofloat)
    font = bitmap_font.load_font(font_file)
    color=0xFFFF00
    text_area = label.Label(font, text=nofloat, color=color, x=25, y=25)
    display.show(text_area)
    time.sleep(30)
