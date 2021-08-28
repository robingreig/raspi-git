import ssd1306py as lcd

#lcd.init_i2c(5, 4, 128, 64, 0)
lcd.init_i2c(27, 26, 128, 64, 1)
lcd.text('font8x8', 0, 0, 8)
lcd.text('font16x16', 0, 20, 16)
lcd.text('font24x24', 0, 40, 24)
lcd.show()