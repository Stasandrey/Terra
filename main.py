import os
import serial
from console import Console


class Data:
    def __init__(self):
        self.data = {'levels': '0000', 'akkum_temp': 0, 'sensor': 45.5}

    def set_data(self, name, value):
        self.data[name] = value

    def get_data(self, name):
        return str(self.data[name])

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
# print(console.head)
console.run(console.head)
