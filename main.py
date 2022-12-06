import os
import serial
from lcd import Lcd


PORT = "/dev/ttyUSB0"
SPEED = 115200

result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())
lcd = Lcd(port)
for i in range(1000):
    lcd.cursor_to(2,0)

    lcd.print(str(i))
