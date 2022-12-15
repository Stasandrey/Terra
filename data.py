# Модуль хранения тэгов
class Data:

    def __init__(self):
        # Описание всех входов/выходов
        self.data = {
                      # Расширительный бак
                      'bak_levels':  '___',
                      'bak_temp':    0,
                      # Теплоаккумулятор
                      'akkum_level': '_',
                      'akkum_temp':  0}

    # Установка текущего значения для тэга
    def set_data(self, name, value):
        self.data[name] = value

    # Чтение текущего значения тэга
    def get_data(self, name):
        return str(self.data[name])

    # Чтение значения уставки тэга
    def read_target(self, name):
        pass

    # Запись значения уставки тэга
    def write_target(self, name):
        pass
