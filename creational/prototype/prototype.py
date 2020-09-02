class Prototype:
    def clone(self, **kwargs):
        instance = self.__class__()
        instance.__dict__.update(kwargs)

        return instance


if __name__ == '__main__':
    person = Prototype().clone(name="Test", age=25)
    user = Prototype().clone(id=1, **person.__dict__)

    print(person.name)
    print(person.age)
    print('***')
    print(user.id)
    print(user.name)
    print(user.age)
