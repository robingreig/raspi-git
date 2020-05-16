import smbus

bus = smbus.SMBus(1)

DS3231 = 0x68

SECONDS_REG = 0x00
ALARM1_SECONDS_REG = 0x07

CONTROL_REG = 0x0E
STATUS_REG = 0x0F

def int_to_bcd(x):
    return int(str(x)[-2:], 0x10)

def write_time_to_clock(pos, hours, minutes, seconds):
    bus.write_byte_data(DS3231, pos, int_to_bcd(seconds))
    bus.write_byte_data(DS3231, pos + 1, int_to_bcd(minutes))
    bus.write_byte_data(DS3231, pos +2, int_to_bcd(hours))

def set_alarm1_mask_bits(bits):
    pos = ALARM1_SECONDS_REG
    for bit in reversed(bits):
        reg = bus.read_byte_data(DS3231, pos)
        if bit:
            reg = reg | 0x80
        else:
            reg = reg & 0x7F
        bus.write_byte_data(DS3231, pos, reg)
        pos = pos + 1

def enable_alarm1():
    reg = bus.read_byte_data(DS3231, CONTROL_REG)
    bus.write_byte_data(DS3231, CONTROL_REG, reg | 0x05)

def clear_alarm1_flag():
    reg = bus.read_byte_data(DS3231, STATUS_REG)
    bus.write_byte_data(DS3231, STATUS_REG, reg & 0xFE)

def check_alarm1_triggered():
    return bus.read_byte_data(DS3231, STATUS_REG) & 0x01 != 0

def set_timer(hours, minutes, seconds):
    # zero the clock
    write_time_to_clock(SECONDS_REG, 0, 0, 0)
    # set the alarm
    write_time_to_clock(ALARM1_SECONDS_REG, hours, minutes, seconds)
    # set the alarm to match hours minutes and seconds
    # need to set some flags
    set_alarm1_mask_bits((True, False, False, False))
    enable_alarm1()
    clear_alarm1_flag()

#
# Your sensor behaviour goes here
print("Program Running")
#
set_timer(1,30,0)
