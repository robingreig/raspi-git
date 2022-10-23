#!/usr/bin/env python3
#
# Vendor:Product ID for Raspberry Pi Pico is 2E8A:0005
#
# see section 4.8 RTC of https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf and in particular section 4.8.6 
# for the RTC_BASE address (0x4005C000) and details of the RD2040 setup registers used to program the RT (also read
# 2.1.2. on Atomic Register Access)
#
from serial.tools import list_ports
import serial, time

picoPorts = list(list_ports.grep("2E8A:0005"))
utcTime = str( int(time.time()) )
pythonInject = [
    'import machine',
    'import utime',
    'rtc_base_mem = 0x4005c000',
    'atomic_bitmask_set = 0x2000',
    'led_onboard = machine.Pin(25, machine.Pin.OUT)',
    '(year,month,day,hour,minute,second,wday,yday)=utime.localtime('+utcTime+')',
    'machine.mem32[rtc_base_mem + 4] = (year << 12) | (month  << 8) | day',
    'machine.mem32[rtc_base_mem + 8] = ((hour << 16) | (minute << 8) | second) | (((wday + 1) % 7) << 24)',
    'machine.mem32[rtc_base_mem + atomic_bitmask_set + 0xc] = 0x10',
    'for i in range(5):',
    '    led_onboard.toggle()',
    '    utime.sleep(0.03)',
    'led_onboard.value(0)'
    ]

if not picoPorts:
    print("No Raspberry Pi Pico found")
else:
    picoSerialPort = picoPorts[0].device
    with serial.Serial(picoSerialPort) as s:
        
        s.write(b'\x03')   # interrupt the currently running code
        s.write(b'\x03')   # (do it twice to be certain)
        
        s.write(b'\x01')   # switch to raw REPL mode & inject code
        for code in pythonInject:
            s.write(bytes(code+'\r\n', 'ascii'))
            time.sleep(0.01)
        time.sleep(0.25)
        s.write(b'\x04')   # exit raw REPL and run injected code
        time.sleep(0.25)   # give it time to run (observe the LED pulse)

        s.write(b'\x02')   # switch to normal REPL mode
        time.sleep(0.5)    # give it time to complete
        s.write(b'\x04')   # execute a 'soft reset' and trigger 'main.py'

    print( 'Raspberry Pi Pico found at '+str(picoSerialPort)+'\r' )
    print( 'Host computer epoch synchronised over USB serial: '+utcTime+'\r' )
