#! /usr/bin/python3

#-------------------------------------------------------------------
# Name: alarm20.py
# Author: Robin Greig
# Date 2017.07.08
# Monitor Keypad for correct code
# Respond to PIR motion sensor input immediately
# Utilize Entry and Exit delays
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
armed_status = 0 # 0 = disarmed, 1 = entry or exit delay, 2 = armed
entry_time = 16 # amount of entry time
entry_delay_time = entry_time # entry delay time variable
exit_time = 16 # amount of exit time
exit_delay_time = exit_time # exit delay time variable
entry_delay_status = 0 # 0 = not started, 1 = running, 2 = completed
exit_delay_status = 0 # 0 = not started, 1 = running, 2 = completed
PIR_status = 0 # 0 = no movement, 1 = movement

##### For troubleshooting, set DEBUG to 1
DEBUG = 0

##### Don't echo password to screen
os.system("stty -echo")

if DEBUG > 0:
  print(time.time())
  os.system("stty echo")

##### Set GPIO pins
Armed_LED = 24 # Green
Beeper = 17 # Brown
Delay_LED = 23 # Green/White
PIR_Sensor = 22 # Blue
Ready_LED = 18 # Blue/White
Siren = 27 # Brown/White

##### Setup GPIO
#GPIO.setwarnings(False) # Ignore GPIO warnings
GPIO.setmode(GPIO.BCM) # numbering scheme that matches Cobbler
GPIO.setup(Armed_LED,GPIO.OUT) # Set GPIO to output for Armed_LED
GPIO.output(Armed_LED, GPIO.HIGH)
GPIO.setup(Beeper,GPIO.OUT) # Set GPIO to output for Beeper_LED
GPIO.output(Beeper, GPIO.HIGH)
GPIO.setup(Delay_LED,GPIO.OUT) # Set GPIO to output for Delay_LED
GPIO.output(Delay_LED, GPIO.HIGH)
#GPIO.setup(PIR_Sensor,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set GPIO Pull Up to UP for PIR Sensors
GPIO.setup(PIR_Sensor,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set GPIO Pull Up to UP for PIR Sensors
GPIO.setup(Ready_LED,GPIO.OUT) # Set GPIO to output for Ready_LED
GPIO.output(Ready_LED, GPIO.LOW)
GPIO.setup(Siren,GPIO.OUT) # Set GPIO to output for Siren
GPIO.output(Siren, GPIO.HIGH)

def PIR_Movement(PIR_Sensor): # Detect movement from PIR sensor
  global PIR_status
  if DEBUG > 0: # PIR sensor very sensitive
    print('**************************** PIR Movement Function called')
  time.sleep(0.5) # Wait 0.5 seconds and see if the sensor is still active to minimize false signals
#  if GPIO.input(PIR_Sensor) == 1: # if sensor is still high, then set PIR status to 1
  if GPIO.input(PIR_Sensor) == 0: # if sensor is still low, then set PIR status to 1
    PIR_status = 1
    print('PIR Movement')
    if DEBUG > 0:
      print('********************** Time Delay 0.5 and input is still high')

#GPIO.add_event_detect(PIR_Sensor, GPIO.RISING, callback=PIR_Movement, bouncetime=500)
GPIO.add_event_detect(PIR_Sensor, GPIO.FALLING, callback=PIR_Movement, bouncetime=500)

def treat_input(linein):
  global armed_status
  global entry_delay_time
  global exit_delay_time
  global exit_delay_status
  global last_code_time
  if DEBUG > 0:
    print("linein = ", linein)
  try:
    keyboard_press = int(linein)
    if DEBUG > 0:
      print('Is a number')
    if int(linein)==4032572556: # shutdown raspi
       count = 0
       os.system("stty echo")
       GPIO.cleanup()
       if DEBUG > 0:
         while (count < 20):
           print('***** Raspberry Pi Shutting Down!!! *****')
           count = count + 1
         time.sleep(2.0)
       subprocess.call(["sudo", "shutdown", "-h", "now"])
    elif int(linein)==4033998788: # reboot raspi
       count = 0
       os.system("stty echo")
       GPIO.cleanup()
       if DEBUG > 0:
         while (count < 20):
           print('***** Raspberry Pi Rebooting!!! *****')
           count = count + 1
         time.sleep(2.0)
       subprocess.call(["sudo", "reboot", "-h", "now"])
    elif int(linein)==4038197350: # exit program
       count = 0
       os.system("stty echo")
       GPIO.cleanup()
       if DEBUG > 0:
         while (count < 20):
           print('***** Exiting Program!!! *****')
           count = count + 1
       sys.exit()
    elif int(linein)==8788: # correct alarm code
      if armed_status == 0: # If alarm disarmed, start exit delay
        armed_status = 1
      else:
        alarm_disarmed()
    else:
      print('Incorrect Entry')
  except ValueError:
    pass
    print('Non-Char Input')
  last_code_time = time.time()

def alarm_activated():
  GPIO.output(Siren, GPIO.LOW)
  GPIO.output(Beeper, GPIO.LOW)
  GPIO.output(Armed_LED, GPIO.LOW)
  GPIO.output(Delay_LED, GPIO.LOW)
  GPIO.output(Ready_LED, GPIO.LOW)
  time.sleep(0.3)
  GPIO.output(Armed_LED, GPIO.HIGH)
  GPIO.output(Delay_LED, GPIO.HIGH)
  GPIO.output(Ready_LED, GPIO.HIGH)
  time.sleep(0.3)
  print('*** ALARM ***')

def alarm_armed():
  if DEBUG > 0:
    global armed_status
    global entry_delay_status
    global exit_delay_status
    global PIR_status
  global entry_delay_time
  global entry_time
  global exit_delay_time
  global exit_time
  entry_delay_time = entry_time
  exit_delay_time = exit_time
  GPIO.output(Armed_LED, GPIO.LOW)
  GPIO.output(Delay_LED, GPIO.HIGH)
  GPIO.output(Ready_LED, GPIO.HIGH)
  print('Alarm Armed')
  if DEBUG > 0:
    print('Running alarm_armed function')
    print('Armed Status = ',armed_status)
    print('Entry Delay Time: ', entry_delay_time)
    print('Entry Delay Status: ',entry_delay_status)
    print('Exit Delay Time: ',exit_delay_time)
    print('Exit Delay Status: ',exit_delay_status)
    print('PIR Status: ',PIR_status)
    time.sleep(1)

def alarm_disarmed():
  global armed_status
  global entry_time
  global entry_delay_status
  global entry_delay_time
  global exit_time
  global exit_delay_status
  global exit_delay_time
  global PIR_status
  GPIO.output(Armed_LED, GPIO.HIGH)
  GPIO.output(Delay_LED, GPIO.HIGH)
  GPIO.output(Ready_LED, GPIO.LOW)
  GPIO.output(Beeper, GPIO.HIGH)
  GPIO.output(Siren, GPIO.HIGH)
  GPIO.output(Beeper, GPIO.HIGH)
  count = 4
  while count > 0:
    GPIO.output(Beeper, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(Beeper, GPIO.HIGH)
    time.sleep(0.1)
    count = count - 1
  armed_status = 0
  entry_delay_time = entry_time
  entry_delay_status = 0
  exit_delay_time = exit_time
  exit_delay_status = 0
  PIR_status = 0
  print('Alarm Disarmed')
  if DEBUG > 0:
    print('Running alarm_disarmed function')
    print('Armed Status = ',armed_status)
    print('Exit Delay Time: ',exit_delay_time)
    print('Entry Delay Time: ',entry_delay_time)

def entry_delay():
  global armed_status
  global entry_time
  global entry_delay_time
  global entry_delay_status
  if entry_delay_time%2 == 0:
    GPIO.output(Beeper,GPIO.LOW)
    GPIO.output(Delay_LED,GPIO.LOW)
  else:
    GPIO.output(Beeper,GPIO.HIGH)
    GPIO.output(Delay_LED,GPIO.HIGH)
  entry_delay_time = entry_delay_time - 1
  time.sleep(1.0)
  if entry_delay_time < entry_time:
    entry_delay_status = 1
  if entry_delay_time == 0:
    entry_delay_status = 2
  print('Entry Delay')
  if DEBUG > 0:
    print('Running entry_delay function')
    print('Armed Status: ', armed_status)
    print('Entry Delay Time: ', entry_delay_time)
    print('Entry Delay Status: ', entry_delay_status)
    print('Entry Time: ', entry_time)

def exit_delay():
  global armed_status
  global entry_delay_status
  global exit_time
  global exit_delay_time
  global exit_delay_status
  global PIR_status
  if exit_delay_time%2 == 0:
    GPIO.output(Beeper,GPIO.LOW)
    GPIO.output(Delay_LED,GPIO.LOW)
  else:
    GPIO.output(Beeper,GPIO.HIGH)
    GPIO.output(Delay_LED,GPIO.HIGH)
  exit_delay_time = exit_delay_time - 1
  time.sleep(1.0)
  if exit_delay_time < exit_time:
    exit_delay_status = 1
    PIR_status = 0
  if exit_delay_time == 0:
    exit_delay_status = 2
    armed_status = 2
    PIR_status = 0
  print('Exit Delay')
  if DEBUG > 0:
    print('Running exit_delay function')
    print('Armed_Status: ',armed_status)
    print('Entry Delay Status: ',entry_delay_status)
    print('Exit Delay Time: ',exit_delay_time)
    print('Exit Delay Status: ',exit_delay_status)
    print('Exit Time: ',exit_time)
    print('PIR Status: ',PIR_status)
    time.sleep(0.5)

def main_loop():
  global armed_status
  global entry_delay_status
  global exit_delay_status
  global read_list
  global PIR_status
  # while still waiting for input
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
#      if (armed_status == 1 and exit_delay_time > 0 and exit_delay_status == 0):
      if (armed_status == 1 and exit_delay_status < 2): # Run Exit Delay
        exit_delay()
      if (armed_status == 2 and exit_delay_status == 2 and entry_delay_status == 0): # Run Alarm Armed
        alarm_armed()
      if (armed_status == 2 and PIR_status == 1 and exit_delay_status == 2 and entry_delay_status < 2): # Run Entry Delay
        entry_delay()      
      if (armed_status == 2 and PIR_status == 1 and exit_delay_status == 2 and entry_delay_status == 2): # Run Alarm Activated
        alarm_activated()      
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
  alarm_disarmed()
  os.system("stty echo")
  GPIO.cleanup()
  pass
