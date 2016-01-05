#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = ('Goran Poprzen')
__license__ = 'Private'
__version__ = '2015.12.26'

import os
from datetime import datetime
import time

# ==========================================================================
# Function Definitions
# ==========================================================================

def read(sensor):
    '''
    Reads temperature sensor
    
    Input:  sensor's serial number
    Output: crc_good (string YES/NO), 
            temp_c (float, temperature in Celsius)
            None if there is no sensor in file system
    
    Note:   When sensor is hot-removed, there is about 100 seconds delay
            before sensor disappear from file system. If this function is
            executed in that interval, it will return ['NO', -0.062]
            After ~100 seconds it will return None
    '''
    sensor_path = "/sys/bus/w1/devices/" + sensor
    if os.path.isdir(sensor_path):
        sensor_file = sensor_path + "/w1_slave"
        lines = read_lines(sensor_file)
        
        crc_pos = lines[0].find("crc=")
        if crc_pos != -1:
            crc_good = lines[0][crc_pos+7:]
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
        return [crc_good, temp_c]
    else:
        return None
        

def read_lines(file_path):
    '''
    Takes path to the file as an input, 
    returns list of lines with stripped '\n' character
    '''
    f = open(file_path)
    lines = f.readlines()
    f.close()
    list_of_lines = []
    for line in lines:
        stripped_line = line.rstrip('\n')
        list_of_lines.append(stripped_line)
    return list_of_lines

    
def current_date():
    '''
    No input parameters.
    Returns current date, format YYYY-MM-DD.
    '''
    return datetime.now().strftime('%Y-%m-%d')
    
def current_time():
    '''
    No input parameters.
    Returns current time, format hh:mm.
    '''
    return datetime.now().strftime('%H:%M')

# ==========================================================================

if __name__ == "__main__":
    print "Don't execute, import!"
