from abc import ABC, abstractmethod
import random


class Animal(ABC):
    @abstractmethod
    def speak(self):
        return NotImplementedError('Implement speak')


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


class Creator(ABC):
    @abstractmethod
    def factory(self):
        raise NotImplementedError()

    def speak(self):
        instance = self.factory()
        return instance.speak()


class DoCreateAnimal(Creator):
    def __init__(self, animal: Animal):
        self.animal_cls = animal

    def factory(self):
        return self.animal_cls()

    def speak(self):
        return f'[ANIMAL]{super().speak()}'


class DoCreateAnimal2(Creator):
    def __init__(self, animal: Animal):
        self.animal_cls = animal

    def factory(self):
        return self.animal_cls()

    def speak(self):
        return f'{super().speak()}'


if __name__ == '__main__':
    animals = [Cat, Dog, Tiger, Human]

    for _ in range(10):
        animal_csl = random.choice(animals)

        animal = DoCreateAnimal(animal=animal_csl)
        print(animal.speak())

    for _ in range(10):
        animal_csl = random.choice(animals)

        animal = DoCreateAnimal2(animal=animal_csl)
        print(animal.speak())
