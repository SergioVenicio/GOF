from abc import ABC


class MediatorInterface(ABC):
    def notify(self, sender, event):
        pass


class Chat(MediatorInterface):
    def __init__(self, name):
        self.name = name
        self.listeners = list()

    def subscribe(self, listener):
        self.listeners.append(listener)

    def notify(self, sender, message, to=None):
        if to is None:
            for listener in self.listeners:
                if listener == sender:
                    continue

                Event(f'[{self.name}][{sender}] {message}', to=listener)
            return
        
        Event(f'[{self.name}][{sender}] {message}', to)


class Event:
    def __init__(self, message, to):
        to.receive(message)


class User:
    def __init__(self, name, mediator: MediatorInterface):
        self.name = name
        self._mediator = mediator

    def __str__(self):
        return self.name

    def receive(self, message):
        print(f'{self} RCV {message}')
    
    def send_message(self, message, to=None):
        self._mediator.notify(self, message, to)


if __name__ == '__main__':
    chat = Chat('MAIN')

    random1 = User('Random', chat)
    random2 = User('Random 2', chat)
    random3 = User('Random 3', chat)

    chat.subscribe(random1)
    chat.subscribe(random2)

    random1.send_message('Hello')
    random2.send_message('Hi')
    random3.send_message('Hi Random', to=random1)

    