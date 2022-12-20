# import os

# import serial

# from modules.console import Console
from modules.data import Data


data = Data('conf/config.yaml')

print(data.objects)

print(data.tags)

print(data.values)
# PORT = "/dev/ttyUSB0"
# SPEED = 115200
# result = os.system('echo baziliy | sudo -S chmod 666 %s' % PORT)
# port = serial.Serial(port=PORT, baudrate=SPEED)
# print(port.readline())


# console = Console("conf/screen.yaml", port, data)
# console.run(console.head)
