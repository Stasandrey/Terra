# Навигация по меню. Самый верхний уровень работы с пользователем.

import screen
import yaml
import time


class Console:
    def __init__(self, name, prt, data):
        self.data = data
        self.port = prt
        self.name = name
        self.screen = screen.Screen(prt)
        self.screen.lcd.print("Reading YAML file.")
        with open(self.name) as f:
            self.head = yaml.safe_load(f)
        self.num = 0

    def draw_item(self, item):
        self.screen.lcd.clear()
        self.screen.lcd.printxy(0, 0, item['text'])
        if item['link'] is True:
            self.screen.lcd.printxy(0, 1, '      >>>>      ')
        else:
            pass

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


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
