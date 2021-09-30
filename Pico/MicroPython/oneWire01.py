import machine, onewire, ds18x20, time
 
ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found a ds18x20 device')
 
while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    #print(ds_sensor.read_temp(rom))
    temp = (ds_sensor.read_temp(rom))
    print (temp)
    nofloat = ('%.0f' %temp)
    #print('%.0f' %temp)
    print(nofloat)
  time.sleep(2)