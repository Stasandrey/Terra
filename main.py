import os
import serial
from screen import Screen

PORT = "/dev/ttyUSB0"
SPEED = 115200

result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())

screen = Screen(port)
screen.lcd.clear()
screen.lcd.print("Temperature ")

temp = 44.5

print(screen.edit_float(12, 0, temp, 4))

port.close()
