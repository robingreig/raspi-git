import machine, onewire, ds18x20, time
import ssd1306py as lcd

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found a ds18x20 device')
 
while True:
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
    hor = 40
    lcd.text(nofloat, hor, 10, 32)
    lcd.show()
  time.sleep(60)