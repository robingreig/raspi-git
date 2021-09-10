from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c=I2C(0,sda=Pin(4), scl=Pin(5), freq=400000)
#i2c=I2C(1,sda=Pin(26), scl=Pin(27), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
#TH = bytearray(b'')
str = 3
array = bytearray(str, 'utf-16')
print(array)

fb = framebuf.FrameBuffer(array,128,64, framebuf.MONO_HLSB)
#fb = framebuf.FrameBuffer(TH,64,64, framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fb,32,0)
#oled.text("Robin's Hardware", 0, 0, 48)
oled.show()