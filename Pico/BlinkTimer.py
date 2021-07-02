import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # The temperature sensro measures the Vbe voltage of a biased bipolar diode,
    # Connecte to the fifth ADC Channel
    # Typically Vbe = 0.706V @ 27C with a slope of -1.721mV (0.001721) per degree
    
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(2)
    