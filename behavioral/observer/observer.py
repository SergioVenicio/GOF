from abc import ABC, abstractmethod
from datetime import datetime
from random import random, randint


class SubjectInterface(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass


    @abstractmethod
    def notify(self):
        pass


class Subject(SubjectInterface):
    _state = None
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def generate_int(self):
        self._state = randint(0, 1000)
        self.notify()


class ObserverInterface(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Number(ObserverInterface):
    _id = 1

    def __init__(self):
        self._id = Number._id
        Number._id += 1
        
    def update(self, subject):
        if subject._state % 2 == 0:
            print(f"[{self._id}] {subject._state} IS PAIR")
        else:
            print(f"[{self._id}] {subject._state} IS ODD")


if __name__ == '__main__':
    subject = Subject()

    for _ in range(10):
        observer = Number()
        subject.attach(observer)

    for _ in range(5):
        print('***')
        subject.generate_int()
    