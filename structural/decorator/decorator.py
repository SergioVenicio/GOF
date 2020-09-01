class Car:
    def accelerate(self):
        print('Run...')


class Decorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def run(self):
        print('Before')
        self._wrapped.accelerate()
        print('After')


if __name__ == '__main__':
    car = Car()
    decorator = Decorator(car)
    decorator.run()
