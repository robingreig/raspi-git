#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: alarm05.py
# Author: Robin Greig
# Date 2017.06.12
# Check for input every 0.1 seconds.
# Respond to an available input immediately, but do something else if idle.
#-------------------------------------------------------------------
import os, select, subprocess, sys, time

# files monitored for input
read_list = [sys.stdin]
# select() should wait for this many seconds for input.
# A smaller number means more cpu usage, but a greater one
# means a more noticeable delay between input becoming
# available and the program starting to work on it.
timeout = 0.1 # seconds
last_work_time = time.time()
alarm_status = 0
DEBUG = 0
os.system("stty -echo")

def treat_input(linein):
  global last_work_time
  global alarm_status
#  print("Workin' it!", linein, end="")
  if DEBUG > 0:
    print("linein = ", linein)
  try:
    keyboard_press = int(linein)
    if DEBUG > 0:
      print('Is a number')
    if int(linein)==1234:
      subprocess.call(["sudo", "shutdown", "-r", "now"])
    if int(linein)==8980:
      if alarm_status == 0:
        alarm_status = 1
        print('Alarm Status = ',alarm_status)
        print('Alarm Armed')
      else:
        alarm_status = 0
        print('Alarm Status = ',alarm_status)
        print('Alarm Disarmed')
  except ValueError:
    pass
    if DEBUG > 0:
      print('Incorrect, try again')
  time.sleep(1) # working takes time
  last_work_time = time.time()

def idle_work():
  global last_work_time
  now = time.time()
  # do some other stuff every 2 seconds of idleness
  #  if now - last_work_time > 2:
  if now - last_work_time > 1:
    if DEBUG > 0:
      print('Idle for too long; doing some other stuff.')
    last_work_time = now

def main_loop():
  global read_list
  # while still waiting for input on at least one file
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
      idle_work()
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
  os.system("stty echo")
  pass
