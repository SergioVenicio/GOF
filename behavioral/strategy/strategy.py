from abc import ABC, abstractmethod

class StrategyInterface(ABC):
    @abstractmethod
    def run(self):
        pass

class Cat(StrategyInterface):
    def run(self):
        return 'Miauuu'


class Dog(StrategyInterface):
    def run(self):
        return 'Auauau'


class Animal:
    def __init__(self, strategy: StrategyInterface):
        self.strategy = strategy

    def hello(self):
        print(self.strategy.run())


if __name__ == '__main__':
    strategies = [Animal(strategy=Cat()), Animal(strategy=Dog())]

    for strategy in strategies:
        strategy.hello()
    