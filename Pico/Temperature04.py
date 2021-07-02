import machine
import utime

sensor_temp = machine.ADC(4)

conversion_factor = 3.3 / (65535)

file = open("temps.txt", "w")

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    file.write(str(temperature) + "\n")
    file.flush()
    utime.sleep(10)