# Модуль автоматизаций
import datetime
import time


class Automation:
    def __init__(self, data):
        self.data = data
        self.heater_on_last = None
        self.heater_start = 0.0
        self.heater_total = 0.0

    # Автоматика расширительного бака
    def bak(self):
        # Защита от замерзания и учет времени подогрева
        if self.data.get_data('bak_temp') < self.data.get_data('bak_temp_target'):
            self.data.set_data('bak_heater', 'on')
            if self.heater_on_last is None:
                self.heater_on_last = datetime.datetime.now()
                self.heater_start = int(self.data.get_data('bak_heater_on_time_total'))
                self.heater_total = 0.0
            else:
                period = datetime.datetime.now() - self.heater_on_last
                period = period.total_seconds()
                self.heater_total += period
                self.data.set_data('bak_heater_on_time_total',
                                   int(self.heater_start + self.heater_total))
                self.data.set_data('bak_heater_on_time',
                                   int(self.heater_total))
                self.heater_on_last = datetime.datetime.now()
        else:
            self.data.set_data('bak_heater', 'off')
            self.data.set_data('bak_heater_on_time', 0)
            self.heater_on_last = None
        # Пополнение бака и учет времени работы подпитки
        levels = self.data.get_data('bak_levels')
        alarm = False
        low = False
        high = False
        if levels[0] == '#':
            alarm = True
        if levels[1] == '#':
            low = True
        if levels[2] == '#':
            high = True
        # Включение подпитки
        if low is False:
            self.data.set_data('bak_fooler_klapan', 'on')
            self.data.set_data('bak_fooler_kran', 'on')

        if (low is True) and (high is True):
            if self.data.get_data('bak_fooler_klapan') == 'on':
                self.data.set_data('bak_fooler_kran', 'off')
                time.sleep(int(self.data.get_data('bak_fooler_time')))
                self.data.set_data('bak_fooler_klapan', 'off')

        # Авария, если не сработан нижний аварийный уровень
        if alarm is False:
            self.data.set_data('error', 'True')

    def run(self):
        self.bak()


if __name__ == "__main__":
    print("Этот модуль не может быть запущен самостоятельно.")
