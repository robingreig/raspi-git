import serial, time

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)


while True:
	print "Printing"
	serial_line = ser.readline()
	print(serial_line)
	print serial_line
	time.sleep(2)

ser.close()
