""" Главный модуль всего приложения """

global cfg


def init_ini_configuration():
    global cfg
    import configuration
    cfg = configuration.Config()


def main():
    init_ini_configuration()
    global cfg
    cfg.hello()

if __name__ == "__main__":
    main()
else:
    print("This module can't be exported")
