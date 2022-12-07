
import os
import serial
from console import Console


class Data:
    def __init__(self):
        pass

    def get_data(self, name):
        pass

    def read_target(self, name):
        pass

    def write_target(self, name):
        pass


PORT = "/dev/ttyUSB0"
SPEED = 115200
result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())

data = Data()
console = Console("screen.yaml", port, data)
print(console.head)
console.run(console.head)
