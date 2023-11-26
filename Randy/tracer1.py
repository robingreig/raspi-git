#!/usr/bin/env python

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
 
client = ModbusClient(method = 'rtu', port = '/dev/ttyXRUSB0', baudrate = 115200)
client.connect()
 
result = client.read_input_registers(0x3100,6,unit=1)
solarVoltage = float(result.registers[0] / 100.0)
solarCurrent = float(result.registers[1] / 100.0)
batteryVoltage = float(result.registers[4] / 100.0)
chargeCurrent = float(result.registers[5] / 100.0)
 
# Do something with the data
solarVoltage
solarCurrent
batteryVoltage
chargeCurrent

import MySQLdb
db = MySQLdb.connect("192.168.1.105", "pidata", "Rasp!data99", "home_data")

sqlcmd = "insert into tracer1(solarVoltage, solarCurrent, batteryVoltage, chargeCurrent) values (" + str(solarVoltage) + ", " + str(solarCurrent) + ", " +str(batteryVoltage) + ", " + str(chargeCurrent) + ")"

# print (sqlcmd)
cursor = db.cursor()
cursor.execute(sqlcmd)
db.commit()
db.close()

client.close()

