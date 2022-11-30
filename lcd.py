# Модуль для работы с LCD экраном 1602а (16x2)
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
        self.port.write(bytes(s + '\n', "ascii"))
        print(self.port.readline())

    # Вывод полного экрана
    def print_screen(self, data):
        self.clear()
        self.print(data[0])
        self.printxy(0, 1, data[1])

    # Вывод строки в текущей позиции
    def print(self, s):
        self.out('la' + s)

    # Вывод строки в заданной точке
    def printxy(self, x, y, s):
        self.cursor_to(x, y)
        self.print(s)

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
        self.out(s)


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
