#!/usr/bin/python3

import os
import time

cht = open("/home/robin/CurrentAdc0Volts", "r")
Adc0 = cht.read()
cht.close()
print("ADC0 = ", Adc0)

