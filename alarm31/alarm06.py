#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: alarm06.py
# Author: Robin Greig
# Date 2017.06.13
# Check for input every 0.1 seconds.
# Respond to an available input immediately, but do something else if idle.
#-------------------------------------------------------------------
import os, select, subprocess, sys, time
import RPi.GPIO as GPIO

# files monitored for input
read_list = [sys.stdin]
# select() should wait for this many seconds for input.
# A smaller number means more cpu usage, but a greater one
# means a more noticeable delay between input becoming
# available and the program starting to work on it.
timeout = 0.1 # seconds

# Set time references
exit_delay_time = time.time()
last_work_time = time.time()

# Set Variables
delay_time_count = 30

# Alarm Status 0 = Disarmed, 1 = Armed
alarm_status = 0

# For troubleshooting, set DEBUG to 1
DEBUG = 0

# Don't echo password to screen
os.system("stty -echo")

if DEBUG > 0:
  print(time.time())
# Set GPIO pins
Armed_LED = 23
Exit_Delay_LED = 24
PIR_Sensor = 25

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #numbering scheme that matches Cobbler
GPIO.setup(Armed_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.setup(Exit_Delay_LED,GPIO.OUT) # Set GPIO to output for Exit_Delay_LED
GPIO.setup(PIR_Sensor,GPIO.IN) # Set GPIO to input for PIR Sensors

def treat_input(linein):
  global last_work_time
  global alarm_status
  global Armed_LED
#  print("Workin' it!", linein, end="")
  if DEBUG > 0:
    print("linein = ", linein)
  try:
    keyboard_press = int(linein)
    if DEBUG > 0:
      print('Is a number')
    if int(linein)==4032572556:
       os.system("stty echo")
       GPIO.output(Armed_LED, GPIO.LOW)
       sys.exit()
    if int(linein)==4038197350:
       os.system("stty echo")
       GPIO.output(Armed_LED, GPIO.LOW)
#       sys.exit()
       subprocess.call(["sudo", "shutdown", "-r", "now"])
    if int(linein)==8980:
      if alarm_status == 0:
        alarm_status = 1
        if DEBUG > 0:
          print('Alarm Status = ',alarm_status)
        print('Alarm Armed')
        GPIO.output(Armed_LED, GPIO.HIGH)
      else:
        alarm_status = 0
        if DEBUG > 0:
          print('Alarm Status = ',alarm_status)
        print('Alarm Disarmed')
        GPIO.output(Armed_LED, GPIO.LOW)
  except ValueError:
    pass
    if DEBUG > 0:
      print('Incorrect, try again')
  time.sleep(1) # working takes time
  last_work_time = time.time()

def delay_timer():
  global exit_delay_time
  global delay_time_count
  global alarm_status
  now = time.time()
  # do some other stuff every second of idleness
  if alarm_status > 0:
    GPIO.output(Exit_Delay_LED,GPIO.HIGH)
  #  if now - last_work_time > 2:
  if now - exit_delay_time > 1:
    if DEBUG > 0:
      print('Running Delay Timer function')
    exit_delay_time = now

def monitor_PIR():
  global last_work_time
  global alarm_status
  now = time.time()
  # do some other stuff every second of idleness
  if alarm_status > 0:
    GPIO.output(Exit_Delay_LED,GPIO.HIGH)
  #  if now - last_work_time > 2:
  if now - last_work_time > 1:
    if DEBUG > 0:
      print('her stuff.')
    last_work_time = now

def main_loop():
  global read_list
  # while still waiting for input on at least one file
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
      if (alarm_status > 0 and delay_time_count < 30):
        delay_timer()
      if (alarm_status > 0 and delay_time_count > 30):
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
