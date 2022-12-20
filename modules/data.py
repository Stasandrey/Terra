# Модуль чтения конфигурации и хранения тэгов
import yaml


class Data:

    def __init__(self, name):
        self.name = name
        with open(self.name) as f:
            self.all = yaml.safe_load(f)
        # Чтение списка объектов, разбор на описания тэгов и создание таблиц значений и уставок
        self.objects = self.all['objects']
        self.tags = {}
        self.values = {}
        self.targets = {}
        for i in self.objects:
            object_ = self.objects[i]  # Список объектов
            for j in object_:
                self.tags[j] = object_[j]
                tag = object_[j]
                self.values[j] = tag['value']
# Читает теги узла

        # # Описание всех входов/выходов
        # self.data = {
        #               # Мигание экрана при аварии
        #               'error': 'False',
        #               # Расширительный бак
        #               'bak_levels':  '___',             # Уровни (аварийный, нижний, верхний)
        #               'bak_temp':    0,                 # Температура в баке
        #               'bak_temp_target': 20.0,          # Уставка для поддержания температуры
        #               'bak_heater': 'off',              # Подогрев бака
        #               'bak_heater_on_time': 0,          # Текущее время работы нагрева
        #               'bak_heater_on_time_total': 0,    # Полное время работы нагрева
        #               'bak_fooler_klapan': 'off',       # Наполнение бака клапан
        #               'bak_fooler_kran': 'off',         # Наполнение бака кран
        #               'bak_fooler_time': 5,            # Время закрытия задвижки, сек
        #               'bak_podpitka_on_time': 0,        # Текущее время работы подпитки
        #               'bak_podpitka_on_time_total': 0,  # Полное время работы подпитки
        #               # Теплоаккумулятор
        #               'akkum_level': '_',         # Уровень
        #               'akkum_temp':  0,           # Температура
        #               'akkum_temp_target': 90.0,  # Уставка сигнализации 'Теплоаккумулятор нагрет'
        #               'akkum_power': 0.5,         # Давление
        #               'akkum_power_target': 0.8,  # Уставка давления на аварийный сброс
        #               'akkum_sbros': 'off'}       # Клапан аварийного сброса давления

    # # Установка текущего значения для тэга
    # def set_data(self, name, value):
    #     self.data[nam`e] = value
    #
    # # Чтение текущего значения тэга
    # def get_data(self, name):
    #     return str(self.data[name])
