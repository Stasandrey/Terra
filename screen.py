# Высокоуровневые функции для работы с консолью

import time
from lcd import Lcd

LEFT = '0'
RIGHT = '1'
UP = '2'
DOWN = '3'
OK = '4'
ESC = '5'
SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ']
SYMBOLS_CODES = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                 '6': 6, '7': 7, '8': 8, '9': 9, '.': 10, ' ': 11}
SYM_NUM = 12


class Screen:
    def __init__(self, prt):
        self.port = prt
        self.lcd = Lcd(prt)

# Редактирование вещественного числа
# x, y   - координаты
# number - стартовое число
# field  - длина поля редактирования
    def edit_float(self, x, y, number, field):
        f = str(number)
        symbols = []
        for item in f:
            symbols.append(SYMBOLS_CODES[item])
        now = f
        start = 0
        res = [False, now]
        self.lcd.cursor_to(x, y)
        s = str(now)
        self.lcd.print(s)
        self.lcd.cursor(True)
        self.lcd.cursor_to(x + start, y)
        work = True
        while work:
            time.sleep(1)
            ans = self.lcd.get_keys()
            button = ans[0]
            print(button)
            if ans == '-1':
                continue
            if button == ESC:
                work = False
                continue
            if button == OK:
                work = False
                res = [True, now]
                continue
            if button == RIGHT:
                start += 1
                if start > field - 1:
                    start = 0
                    self.lcd.cursor_to(x + start, y)
                    continue
            if button == LEFT:
                start -= 1
                if start < 0:
                    start = field - 1
                    self.lcd.cursor_to(x + start, y)
                continue
            if button == UP:
                symbols[start] += 1
                if symbols[start] >= SYM_NUM:
                    symbols[start] = 0
            if button == DOWN:
                symbols[start] -= 1
                if symbols[start] < 0:
                    symbols[start] = SYM_NUM - 1
            now = ''
            for item in symbols:
                now += SYMBOLS[item]
            self.lcd.cursor_to(x, y)
            self.lcd.print(now)
            self.lcd.cursor_to(x + start, y)
        if res[0]:
            try:
                res[1] = float(res[1])
            except (Exception,):
                res[0] = False
        self.lcd.cursor(False)
        return res


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
