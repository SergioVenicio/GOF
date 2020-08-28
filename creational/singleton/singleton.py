class Singleton:
    __instances = {}

    def __new__(cls, instance_type=list):
        if cls.__instances.get(instance_type) is not None:
            return cls.__instances[instance_type]

        cls.__instances[instance_type] = instance_type()

        return cls.__instances[instance_type]


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    c = Singleton(dict)

    a.append(10)
    c['test'] = True

    print(id(b) == id(a))
    print(id(c) != id(a))
