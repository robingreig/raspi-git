#!/usr/bin/env python

import time
import RPi.GPIO as io
io.setmode(io.BCM)

relay01_pin = 23

io.setup(relay01_pin, io.OUT)
io.output(relay01_pin, False)

while True:
  io.output(relay01_pin, True)
  time.sleep(2)
  io.output(relay01_pin, False)
  time.sleep(2)

