# Навигация по меню. Самый верхний уровень работы с пользователем.

from modules.screen import Screen
from modules.automation import Automation
import yaml


class Console:
    def __init__(self, name, prt, data):
        self.data = data
        self.port = prt
        self.name = name
        self.screen = Screen(prt)
        self.automation = Automation(self.data)
        self.screen.lcd.print("Reading YAML file.")
        self.error = False

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
        cycle = 0
        while work is True:
            self.data.set_data('error', 'False')
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

            # Запуск автоматизаций
            self.automation.run()

            # Индикация аварии
            error = self.data.get_data('error')
            if error == 'True':
                if self.error is False:
                    self.error = True
                    cycle = 0
                else:
                    cycle += 1
                    if cycle > 7:
                        cycle = 0
                        if self.screen.lcd.isBacklite is True:
                            self.screen.lcd.backlite(False)
                        else:
                            self.screen.lcd.backlite(True)

            else:
                cycle = 0
                self.error = False
                self.screen.lcd.backlite(True)

            # Обработка нажатия кнопок
            button = self.screen.lcd.get_keys()
            if button == '-1':
                continue
            button = button[0]
            if button == self.screen.ESC:
                work = False
                continue
            if button == self.screen.OK:
                if head['data'][head['item']]['link'] is True:
                    self.run(head['data'][head['item']])
                else:
                    if head['data'][head['item']]['edit'] is True:
                        result = self.screen.edit_float(
                                        self.data.get_data(head['data'][head['item']]['target']))
                        if result[0] is True:
                            self.data.set_data(head['data'][head['item']]['target'], result[1])
                        print(self.data.data)
            if button == self.screen.DOWN:
                head['item'] += 1
                if head['item'] > number - 1:
                    head['item'] = 0
            if button == self.screen.UP:
                head['item'] -= 1
                if head['item'] < 0:
                    head['item'] = number - 1
            self.draw_item(head['data'][head['item']])


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
