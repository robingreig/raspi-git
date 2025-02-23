from machine import UART, Pin
import time
 
# Define UART pins
TX_PIN = 0
RX_PIN = 1
 
# Initialize UART for Modbus communication
uart = UART(0, baudrate=9600, tx=Pin(TX_PIN), rx=Pin(RX_PIN))
 
# Define Modbus parameters
slave_address = 0x01          # Address of the Modbus slave device
function_code = 0x03          # Function code to read holding registers
start_address_high = 0x00     # High byte of the starting address
start_address_low = 0x00      # Low byte of the starting address
register_count_high = 0x00    # High byte of the number of registers to read
register_count_low = 0x02     # Low byte of the number of registers to read
 
def calculate_crc(frame):
    crc = 0xFFFF
    for pos in frame:
        crc ^= pos
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc
 
def construct_modbus_request(address, function, start_high, start_low, count_high, count_low):
    frame = [address, function, start_high, start_low, count_high, count_low]
    crc = calculate_crc(frame)
    frame.append(crc & 0xFF)         # CRC low byte
    frame.append((crc >> 8) & 0xFF)  # CRC high byte
    return bytes(frame)
 
def send_modbus_request(frame):
    uart.write(frame)
 
def read_modbus_response(length):
    response = uart.read(length)
    return response
 
def verify_crc(frame):
    received_crc = (frame[-1] << 8) | frame[-2]
    calculated_crc = calculate_crc(frame[:-2])
    return received_crc == calculated_crc
 
def process_modbus_response(frame):
    humidity = (frame[3] << 8) | frame[4]
    temperature = (frame[5] << 8) | frame[6]
    humidity_value = humidity / 10.0
    temperature_value = temperature / 10.0
    print(f"Humidity: {humidity_value} %RH")
    print(f"Temperature: {temperature_value} °C")
    print()
 
def main():
    while True:
        request_frame = construct_modbus_request(slave_address, function_code, start_address_high, start_address_low, register_count_high, register_count_low)
        send_modbus_request(request_frame)
        time.sleep(1)  # Wait for the response
 
        response_length = 9  # Expected response length
        if uart.any():
            response_frame = read_modbus_response(response_length)
            if response_frame and verify_crc(response_frame):
                process_modbus_response(response_frame)
            else:
                print("CRC error.")
        else:
            print("No response from slave.")
 
        time.sleep(2)  # Wait before sending the next request
 
if __name__ == "__main__":
    main()
