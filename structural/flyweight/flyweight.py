class Flyweight:
    _flyweight_pool = {}

    def get(self, state):
        if self._flyweight_pool.get(state) is None:
            self._flyweight_pool[state] = state

        return self._flyweight_pool[state]

    def list(self):
        return ' '.join([
            str(v)
            for v in self._flyweight_pool.values()
        ])


if __name__ == '__main__':
    pool = Flyweight()

    for i in range(100):
        print(pool.get(i))

    for i in range(100):
        print(pool.get(i))

    print(pool.list())
