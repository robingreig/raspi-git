import smbus

bus = smbus.SMBus(1)

DS3231 = 0x68

#SECONDS_REG = 0x00
#ALARM1_SECONDS_REG = 0x07

#CONTROL_REG = 0x0E
STATUS_REG = 0x0F

# clear_alarm1_flag():
reg = bus.read_byte_data(DS3231, STATUS_REG)
bus.write_byte_data(DS3231, STATUS_REG, reg & 0xFE)
print("Alarm1 Flag Cleared")
