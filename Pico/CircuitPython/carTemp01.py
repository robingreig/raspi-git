import board
import busio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import machine, onewire, ds18x20, time
#import ssd1306py as lcd

displayio.release_displays()

i2c = busio.I2C (scl=board.GP5, sda=board.GP4) # This RPi Pico way to call I2C

display_bus = displayio.I2CDisplay (i2c, device_address = 0x3C) # The address of my Board

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

font_file = "fonts/Roboto48.bdf"

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found a ds18x20 device')

# Draw a label
#text = "32"
#font = bitmap_font.load_font(font_file)
#color=0xFFFF00
#text_area = label.Label(font, text=text, color=color, x=25, y=25)

#display.show(text_area)

while True:
    #pass
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  lcd.init_i2c(27, 26, 128, 64, 1)
  for rom in roms:
    #print(ds_sensor.read_temp(rom))
    temp = (ds_sensor.read_temp(rom))
    print (temp)
    nofloat = ('%.0f' %temp)
    #print('%.0f' %temp)
    print(nofloat)
    font = bitmap_font.load_font(font_file)
    color=0xFFFF00
    text_area = label.Label(font, text=nofloat, color=color, x=25, y=25)
    display.show(text_area)
  time.sleep(2)