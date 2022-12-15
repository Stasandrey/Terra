# Навигация по меню. Самый верхний уровень работы с пользователем.

import screen
import yaml


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
        s = ' ' * ((16 - len(item['text'])) // 2) + item['text']
        self.screen.lcd.printxy(0, 0, s)
        if item['link'] is True:
            self.screen.lcd.printxy(0, 1, '      >>>>      ')
        else:
            s = self.data.get_data(item['data']) + ' ' + item['inch']
            s = ' ' * ((16-len(s)) // 2) + s
            self.screen.lcd.printxy(0, 1, s)

    def run(self, head):
        self.draw_item(head['data'][head['item']])
        work = True
        number = len(head['data'])
        count = 0
        while work is True:
            count += 1
            # Получение информации с датчиков
            if count > 10:
                count = 0
                levels_all = self.screen.lcd.get_levels()
                self.data.set_data('bak_levels', levels_all[0:3])
                self.data.set_data('akkum_level', levels_all[3])
                self.data.set_data('bak_temp', self.screen.lcd.get_1_wire())
                self.draw_item(head['data'][head['item']])
            self.screen.lcd.wait(200)
            # Обработка нажатия кнопок
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
