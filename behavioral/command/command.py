from abc import ABC, abstractmethod


class Receiver:
    def proccess_int(self, payload):
        return f'[INT] {self.proccess(payload)}'
    
    def proccess(self, payload):
        return f'{payload}'


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self):
        return self._payload


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, payload):
        self._receiver = receiver
        self._payload = payload
    
    def execute(self):
        if isinstance(self._payload, int):
            return self._receiver.proccess_int(self._payload)

        return self._receiver.proccess(self._payload)


if __name__ == '__main__':
    receiver = Receiver()

    print(SimpleCommand('simple').execute())

    for payload in [1, 'payload', {'my': 'dict'}]:
        comand = ComplexCommand(receiver, payload)
        print(comand.execute())

    