import serial, time

ser = serial.Serial("/dev/ttyAMA0", 9600)

count = 0
while (count < 10):
	serial_line = ser.readline()
	print "Printing line : ",(count)
	print (serial_line)
	count = count + 1
	time.sleep(1)
ser.close()
