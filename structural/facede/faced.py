class Window:
    def __str__(self):
        return 'Window'


class Port:
    def __str__(self):
        return 'PORT'


class House:
    def __init__(self):
        self._window = Window()
        self._port = Port()

    def __str__(self):
        return f'''\
        HOUSE:
            {self._port}
            {self._window}'''


if __name__ == '__main__':
    house = House()
    print(house)
