#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: alarm08.py
# Author: Robin Greig
# Date 2017.06.16
# Check for input every 0.1 seconds.
# Respond to an available input immediately, but do something else if idle.
#-------------------------------------------------------------------
import os, select, subprocess, sys, time
import RPi.GPIO as GPIO

##### files monitored for input
read_list = [sys.stdin]
# select() should wait for this many seconds for input.
# A smaller number means more cpu usage, but a greater one
# means a more noticeable delay between input becoming
# available and the program starting to work on it.
timeout = 0.1 # seconds

##### Set time references
delay_time = time.time() # time for exit or entry delay
last_code_time = time.time() # timer for keyboard check

##### Set Variables
alarm_time = 60 # how long for alarm to sound before reset
armed_status = 0 # 0 = disarmed, 1 = armed
correct_code = 0 # 0 = wrong code, 1 = correct code
delay_time_count = 30 # amount of entry or exit time
entry_delay = 0 # 0 = not started or running, 1 = completed
exit_delay = 0 # 0 = not started or running, 1 = completed
delay_time_count = 30 # exit or entry delay time
PIR_sensor = 0 # 0 = no movement, 1 = movement

##### For troubleshooting, set DEBUG to 1
DEBUG = 1

##### Don't echo password to screen
os.system("stty -echo")

if DEBUG > 0:
  print(time.time())
  os.system("stty echo")

##### Set GPIO pins
Alarm_LED = 24
Armed_LED = 23
Beeper = 20
PIR_Sensor = 25
Ready_LED = 18
Siren = 21

##### Setup GPIO
GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(Alarm_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.setup(Armed_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.setup(Beeper,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.setup(PIR_Sensor,GPIO.IN) # Set GPIO to input for PIR Sensors
GPIO.setup(Ready_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.setup(Siren,GPIO.OUT) # Set GPIO to output for Armed_LED

def treat_input(linein):
  global last_code_time
  global armed_status
  global Armed_LED
#  print("Workin' it!", linein, end="")
  if DEBUG > 0:
    print("linein = ", linein)
  try:
    keyboard_press = int(linein)
    if DEBUG > 0:
      print('Is a number')
    if int(linein)==4038197350: # exit progrm
       os.system("stty echo")
       GPIO.output(Armed_LED, GPIO.LOW)
       sys.exit()
    if int(linein)==4032572556: # shutdown raspi
       os.system("stty echo")
       GPIO.output(Armed_LED, GPIO.LOW)
       subprocess.call(["sudo", "shutdown", "-h", "now"])
    if int(linein)==8980: # correct alarm code
      if armed_status == 0:
        armed_status = 1
        if DEBUG > 0:
          print('Armed Status = ',armed_status)
        print('Alarm Armed')
        GPIO.output(Armed_LED, GPIO.HIGH)
      else:
        alarm_status = 0
        if DEBUG > 0:
          print('Armed Status = ',armed_status)
        print('Alarm Disarmed')
        GPIO.output(Armed_LED, GPIO.LOW)
  except ValueError:
    pass
    if DEBUG > 0:
      print('Incorrect, try again')
  time.sleep(1) # working takes time
  last_code_time = time.time()

def exit_delay():
  global armed_status
  global exit_delay
  global delay_time_count
  now = time.time()
  # do some other stuff every second of idleness
  if armed_status == 1:
    GPIO.output(Exit_Delay_LED,GPIO.HIGH)
  #  if now - last_code_time > 2:
  if now - exit_delay_time > 1:
    if DEBUG > 0:
      print('Running Delay Timer function')
    exit_delay_time = now

def monitor_PIR():
  global last_code_time
  global armed_status
  now = time.time()
  # do some other stuff every second of idleness
  if armed_status > 0:
    GPIO.output(Exit_Delay_LED,GPIO.HIGH)
  #  if now - last_code_time > 2:
  if now - last_code_time > 1:
    if DEBUG > 0:
      print('do other stuff.')
    last_code_time = now

def main_loop():
  global read_list
  # while still waiting for input on at least one file
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
      if (armed_status > 0 and delay_time_count < 30):
        delay_timer()
      if (armed_status > 0 and delay_time_count > 30):
        monitor_PIR()      
#      idle_work()
    else:
      for file in ready:
        line = file.readline()
        if not line: # EOF, remove file from input list
          read_list.remove(file)
        elif line.rstrip(): # optional: skipping empty lines
          treat_input(line)

try:
    main_loop()
except KeyboardInterrupt:
  GPIO.output(Armed_LED, GPIO.LOW)
  os.system("stty echo")
  pass
