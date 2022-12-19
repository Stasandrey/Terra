# Высокоуровневые функции для работы с консолью

from modules.lcd import Lcd

SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ']
SYMBOLS_CODES = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                 '6': 6, '7': 7, '8': 8, '9': 9, '.': 10, ' ': 11}
SYM_NUM = 12
MAX_EDIT_TIME = 50  # Время до выхода, если не нажимаются кнопки


class Screen:
    def __init__(self, prt):
        self.LEFT = '0'
        self.RIGHT = '1'
        self.UP = '2'
        self.DOWN = '3'
        self.OK = '4'
        self.ESC = '5'

        self.port = prt
        self.lcd = Lcd(prt)

# Редактирование вещественного числа
# x, y   - координаты
# number - стартовое число
# field  - длина поля редактирования
    def edit_float(self, number):
        f = str(number)
        field = len(f) + 4
        f = 4 * ' ' + f
        symbols = []
        for item in f:
            symbols.append(SYMBOLS_CODES[item])
        now = f
        start = 0
        res = [False, now]
        self.lcd.printxy(0, 1, "                ")
        self.lcd.cursor_to(0, 1)
        s = str(now)
        self.lcd.print(s)
        self.lcd.cursor(True)
        self.lcd.cursor_to(start, 1)
        count = 0
        work = True
        while work:
            count += 1
            if count > MAX_EDIT_TIME:
                work = False
            self.lcd.wait(200)
            ans = self.lcd.get_keys()
            button = ans[0]
            if ans == '-1':
                continue
            count = 0
            if button == self.ESC:
                work = False
                continue
            if button == self.OK:
                work = False
                res = [True, now]
                continue
            if button == self.RIGHT:
                start += 1
                if start > field - 1:
                    start = 0
                    self.lcd.cursor_to(start, 1)
                    continue
            if button == self.LEFT:
                start -= 1
                if start < 0:
                    start = field - 1
                    self.lcd.cursor_to(start, 1)
                    continue
            if button == self.UP:
                symbols[start] += 1
                if symbols[start] >= SYM_NUM:
                    symbols[start] = 0
            if button == self.DOWN:
                symbols[start] -= 1
                if symbols[start] < 0:
                    symbols[start] = SYM_NUM - 1
            now = ''
            for item in symbols:
                now += SYMBOLS[item]
            self.lcd.cursor_to(0, 1)
            self.lcd.print(now)
            self.lcd.cursor_to(start, 1)
        if res[0]:
            try:
                res[1] = float(res[1])
            except (Exception,):
                res[0] = False
        self.lcd.cursor(False)
        return res


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
