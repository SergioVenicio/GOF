class Cat:
    def meow(self):
        return 'Meaw'


class Dog:
    def bark(self):
        return 'Wauuu'


class Adapter:
    def communicate(self, target):
        if isinstance(target, Cat):
            return f'[{type(target)}] {target.meow()}'
        elif isinstance(target, Dog):
            return f'[{type(target)}] {target.bark()}'


if __name__ == '__main__':
    adapter = Adapter()
    print(adapter.communicate(target=Dog()))
    print(adapter.communicate(target=Cat()))
