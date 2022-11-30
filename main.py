# import modbus
# modbus.run()
# import time
import os
import serial

PORT = "/dev/ttyUSB0"
SPEED = 115200


class Lcd:
    def __init__(self, prt):
        self.isBacklite = True
        self.isCursor = False
        self.isBlink = False
        self.x = 0
        self.y = 0
        self.port = prt

# Вспомогательная функция вывода в порт
    def out(self, s):
        self.port.write(bytes(s+'\n', "ascii"))
        print(self.port.readline())

# Вывод строки в текущей позиции
    def print(self, s):
        self.out('la'+s)

# Включить/выключить подсветку
    def backlite(self, flag):
        if flag is True:
            self.isBacklite = True
            self.out("lc")
        else:
            self.isBacklite = False
            self.out("lb")

# Включить/выключить курсор
    def cursor(self, flag):
        if flag is True:
            self.isCursor = True
            self.out("lg")
        else:
            self.isCursor = False
            self.out("lh")

# Включить/выключить мигание символа
    def blink(self, flag):
        if flag is True:
            self.isBlink = True
            self.out("ld")
        else:
            self.isBlink = False
            self.out("le")

# Очистить экран
    def clear(self):
        self.out("lf")

# Переместить курсор
    def cursor_to(self, x, y):
        s = "li"
        if x < 10:
            s = s + "0"

        s = s + str(x) + str(y)
        print(s)
        self.out(s)


result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())
lcd = Lcd(port)
#while True:
    # cmd = input(">")
    # tty.print(cmd)
    # lcd.blink(not lcd.isBlink)
    # time.sleep(3)
#time.sleep(1)
lcd.print("a")
lcd.cursor_to(2, 0)
lcd.print("b")
lcd.cursor_to(1, 1)
lcd.print("c")
