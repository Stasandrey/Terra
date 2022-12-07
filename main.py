import time
import os
import serial
from lcd import Lcd


PORT = "/dev/ttyUSB0"
SPEED = 115200

result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())
lcd = Lcd(port)
# lcd.print("1234")
while True:

    print(lcd.get_keys())
    time.sleep(1)



