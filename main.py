#import modbus
#modbus.run()
import time
import serial

PORT = "/dev/ttyUSB0"

port = serial.Serial(port=PORT,baudrate=9600)

print(port.readline())
port.write(bytes("b","ascii"))

