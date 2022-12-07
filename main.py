import yaml
import time
import os
import serial
import screen


class Console:
    def __init__(self, name, prt):
        self.port = prt
        self.name = name
        self.screen = screen.Screen(port)
        self.screen.lcd.print("Reading YAML file.")
        # time.sleep(3)

        with open(self.name) as f:
            self.head = yaml.safe_load(f)
        self.num = 0

    def draw_item(self, item):
        self.screen.lcd.clear()
        self.screen.lcd.printxy(0, 0, item['text'])
        if item['link'] is True:
            self.screen.lcd.printxy(0, 1, '>>>>>>>>>>>>>>>>')

    def run(self, head):
        self.draw_item(head['data'][head['item']])
        work = True
        number = len(head['data'])
        while work is True:
            time.sleep(1)
            button = self.screen.lcd.get_keys()
            if button == '-1':
                continue
            button = button[0]
            if button == screen.ESC:
                work = False
                continue
            if button == screen.OK:
                if head['data'][head['item']]['link'] is True:
                    self.run(head['data'][head['item']])
                else:
                    pass
            if button == screen.DOWN:
                head['item'] += 1
                if head['item'] > number - 1:
                    head['item'] = 0
            if button == screen.UP:
                head['item'] -= 1
                if head['item'] < 0:
                    head['item'] = number - 1
            self.draw_item(head['data'][head['item']])


PORT = "/dev/ttyUSB0"
SPEED = 115200
result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
port = serial.Serial(port=PORT, baudrate=SPEED)
print(port.readline())

console = Console("screen.yaml", port)
print(console.head)
console.run(console.head)
# import os
# import serial
# from screen import Screen
# PORT = "/dev/ttyUSB0"
# SPEED = 115200
# result = os.system('echo baziliy | sudo -S chmod 777 %s' % PORT)
# port = serial.Serial(port=PORT, baudrate=SPEED)
# print(port.readline())
# screen = Screen(port)
# screen.lcd.clear()
# screen.lcd.print("Temperature ")
# temp = 44.5
# print(screen.edit_float(12, 0, temp, 4))
# port.close()
