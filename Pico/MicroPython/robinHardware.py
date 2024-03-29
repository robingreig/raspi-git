from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
#import ascii48

i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
#i2c=I2C(1,sda=Pin(26), scl=Pin(27), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Robin's Hardware", 0, 0, 48)
oled.show()