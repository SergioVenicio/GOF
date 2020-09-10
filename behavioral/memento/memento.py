from abc import ABC, abstractmethod


class MementoInterface(ABC):
    @abstractmethod
    def get_state(self):
        pass


class Memento(MementoInterface):
    def __init__(self, state=''):
        self._state = state

    def get_state(self):
        return self._state


class State:
    def __init__(self, state=''):
        self._state = state

    def show_state(self):
        print(self._state)

    def set_state(self, new_state):
        self._state = new_state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    
class File:
    def __init__(self, state: State):
        self._mementos = []
        self._state_provider = state

    def write(self, text):
        self._state_provider.set_state(text)
        self.backup()

    def read(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print(memento.get_state())

    def read_lines(self):
        for memento in self._mementos:
            print(memento.get_state())

    def backup(self):
        self._mementos.append(self._state_provider.save())

    def undo(self):
        if not self._mementos:
            return
        
        memento = self._mementos.pop()
        self._state_provider.restore(memento)


if __name__ == '__main__':
    file_state = State()
    file = File(file_state)
    file.write('Test')
    file.write('Test 2')
    file.read_lines()

    print('***')

    file_state = State()
    file = File(file_state)
    file.write('Test')
    file.write('Test 2')
    file.read()
    file.read()
    