#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: alarm09.py
# Author: Robin Greig
# Date 2017.06.17
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
delay_time_count = 5 # amount of entry or exit time
entry_delay_status = 0 # 0 = not started or running, 1 = completed
exit_delay_status = 0 # 0 = not started or running, 1 = completed
PIR_status = 0 # 0 = no movement, 1 = movement

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
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(Alarm_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Alarm_LED, GPIO.LOW)
GPIO.setup(Armed_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Armed_LED, GPIO.LOW)
GPIO.setup(Beeper,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Beeper, GPIO.LOW)
GPIO.setup(PIR_Sensor,GPIO.IN) # Set GPIO to input for PIR Sensors
GPIO.setup(Ready_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Ready_LED, GPIO.LOW)
GPIO.setup(Siren,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Siren, GPIO.LOW)


def treat_input(linein):
  global last_code_time
  global armed_status
  global delay_time_count
  global exit_delay_status
#  print("Workin' it!", linein, end="")
  if DEBUG > 0:
    print("linein = ", linein)
  try:
    keyboard_press = int(linein)
    if DEBUG > 0:
      print('Is a number')
    if int(linein)==4038197350: # exit progrm
       os.system("stty echo")
       GPIO.cleanup()
       sys.exit()
    if int(linein)==4032572556: # shutdown raspi
       os.system("stty echo")
       GPIO.cleanup()
       subprocess.call(["sudo", "shutdown", "-h", "now"])
    if int(linein)==8980: # correct alarm code
      if armed_status == 0:
        armed_status = 1
        print('Alarm Armed')
        if DEBUG > 0:
          print('Armed Status = ',armed_status)
          print('Delay Time Count = ',delay_time_count)
          print('Exit Delay Status = ',exit_delay_status)
          time.sleep(1)
        GPIO.output(Armed_LED, GPIO.HIGH)
        delay_time_count = 5
        exit_delay_status = 0
      else:
        armed_status = 0
        print('Alarm Disarmed')
        if DEBUG > 0:
          print('Armed Status = ',armed_status)
          print('Delay Time Count = ',delay_time_count)
        GPIO.output(Armed_LED, GPIO.LOW)
        delay_time_count = 5
  except ValueError:
    pass
    if DEBUG > 0:
      print('Incorrect, try again')
  time.sleep(1) # working takes time
  last_code_time = time.time()

def entry_delay():
  global delay_time_count
  global entry_delay_status
  if DEBUG > 0:
    print('Running entry_delay function')
  if delay_time_count%2 == 0:
    GPIO.output(Beeper,GPIO.HIGH)
  else:
    GPIO.output(Beeper,GPIO.LOW)
  delay_time_count = delay_time_count - 1
  if DEBUG > 0:
    print('End of entry_delay function')
  time.sleep(1)

def exit_delay():
  global delay_time_count
  global exit_delay_status
  if DEBUG > 0:
    print('Running exit_delay function')
  if delay_time_count%2 == 0:
    GPIO.output(Beeper,GPIO.HIGH)
  else:
    GPIO.output(Beeper,GPIO.LOW)
  delay_time_count = delay_time_count - 1
  if delay_time_count == 0:
    exit_delay_status = 1
  if DEBUG > 0:
    print('delay_time_count: ',delay_time_count)
    print('exit_delay_status: ',exit_delay_status)
    print('End of exit_delay function')
  time.sleep(1)

def monitor_PIR():
  global last_code_time
  global PIR_status
  now = time.time()
  # do some other stuff every second of idleness
  if now - last_code_time > 1:
    if DEBUG > 0:
      print('Monitor PIR')
      print('PIR Status: ',PIR_status)
      time.sleep(1)
    last_code_time = now

def main_loop():
  global armed_status
  global exit_delay
  global delay_time_count
  global read_list
  # while still waiting for input on at least one file
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
      if (armed_status == 1 and delay_time_count > 0 and exit_delay_status == 0):
        print('main_loop > exit_delay')
        exit_delay()
      if (armed_status == 1 and exit_delay_status == 1):
        monitor_PIR()      
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
  GPIO.cleanup()
  pass
