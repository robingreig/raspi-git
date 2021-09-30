import serial
import time


class TPutComp:
    def __init__(self, runs):
#        self.serial_port = serial.Serial('/dev/ttyACM0', 115200,
#                                         timeout=1, writeTimeout=0)
        self.serial_port = serial.Serial('/dev/serial0', 115200,
                                         timeout=1, writeTimeout=0)

        start_time = time.time()
        for i in range(runs):
            self.serial_port.write('abcde\n'.encode())
            data = self.serial_port.readline(7).decode()
            if data != 'abcde\r\n':
                raise RuntimeError
        elapsed = time.time() - start_time
        print(f'{i+1} Iterations elapsed time: {elapsed}')
        print(f'Calculated single iteration: {elapsed / runs}')


TPutComp(100)
