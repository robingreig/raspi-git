#!/usr/bin/env python3
import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(0, 1)  # Registernumber, number of decimals
print("Temp1: ")
print(temperature)

