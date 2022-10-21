""" Загрузка конфигурации приложения и доступ к параметрам """


class Config:
    def __init__(self):
        print("Configuration")
        self.ip = ""

    def hello(self):
        print("Hello")
        print(self.ip)
