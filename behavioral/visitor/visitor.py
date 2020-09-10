class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        return 'running...'


class Cat:
    def meow(self):
        return 'Meowww'


class Dog:
    def meow(self):
        return 'Auauu'


class Visitor:
    def visit(self, element: Animal):
        if isinstance(element, Cat):
            self.visit_cat(element)
        elif isinstance(element, Dog):
            self.visit_cat(element)
        else:
            print(f'Visit {element.name}: {element.run()}')

    def visit_cat(self, element):
        print(f'Visit cat : {element.meow()}.')

    def visit_dog(self, element):
        print(f'Visit dog : {element.bark()}.')


if __name__ == '__main__':
    visitor = Visitor()

    for animal in [Cat(), Dog(), Animal('rat')]:
        visitor.visit(animal)
