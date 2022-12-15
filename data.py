# Модуль хранения тэгов
class Data:

    def __init__(self):
        # Описание всех входов/выходов
        self.data = {
                      # Расширительный бак
                      'bak_levels':  '___',        # Уровни (аварийный, нижний, верхний)
                      'bak_temp':    0,            # Температура в баке
                      'bak_temp_target': 5.0,      # Уставка для поддержания температуры
                      'bak_heater': 'off',         # Подогрев бака
                      'bak_fooler_klapan': 'off',  # Наполнение бака клапан
                      'bak_fooler_kran': 'off',    # Наполнение бака кран
                      'bak_fooler_time': 15,       # Время закрытия задвижки
                      # Теплоаккумулятор
                      'akkum_level': '_',         # Уровень
                      'akkum_temp':  0,           # Температура
                      'akkum_temp_target': 90.0,  # Уставка сигнализации 'Теплоаккумулятор нагрет'
                      'akkum_power': 0.5,         # Давление
                      'akkum_power_target': 0.8,  # Уставка давления на аварийный сброс
                      'akkum_sbros': 'off'}       # Клапан аварийного сброса давления

    # Установка текущего значения для тэга
    def set_data(self, name, value):
        self.data[name] = value

    # Чтение текущего значения тэга
    def get_data(self, name):
        return str(self.data[name])
