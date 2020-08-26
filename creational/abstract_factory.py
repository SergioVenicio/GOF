import random
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        return NotImplementedError('Implement speak')


class AbstractFactory(ABC):
    def __init__(self, instance_factory=None):
        self.instance_factory = instance_factory

    @abstractmethod
    def create(self):
        raise NotImplementedError('Implement create')


class AnimalFactory(AbstractFactory):
    def create(self):
        new_instance = self.instance_factory()
        return new_instance


class Dog(Animal):
    def speak(self):
        return '[DOG] Auuu auuu'


class Cat(Animal):
    def speak(self):
        return '[CAT] Miauuuu'


class Tiger(Animal):
    def speak(self):
        return '[TIGER] Uauu Uauu'


class Human(Animal):
    def speak(self):
        return '[HUMAN] Hello'


if __name__ == '__main__':
    animals = [Cat, Dog, Tiger, Human]

    for _ in range(10):
        instance_to_create = random.choice(animals)

        animal_factory = AnimalFactory(instance_factory=instance_to_create)
        animal = animal_factory.create()

        print(animal.speak())
