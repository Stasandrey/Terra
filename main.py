import os
import serial
from console import Console
from data import Data


PORT = "/dev/ttyUSB0"
SPEED = 115200
result = os.system('echo baziliy | sudo -S chmod 666 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())

data = Data()
console = Console("screen.yaml", port, data)
console.run(console.head)
