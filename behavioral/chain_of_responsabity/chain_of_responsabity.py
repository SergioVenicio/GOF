from abc import ABC, abstractmethod


class Handler(ABC):
    _next = None

    def next(self, handler):
        self._next = handler
        return handler

    def handle(self, request):
        return '>/'


class PersonHandler(Handler):
    def handle(self, request):
        if request == 'PERSON':
            return 'Hello'

        if self._next:
            return self._next.handle(request)

        return super().handle(request)


class DogHandler(Handler):
    def handle(self, request):
        if request == 'DOG':
            return 'Wauuu'
        
        if self._next:
            return self._next.handle(request)

        return super().handle(request)


if __name__ == '__main__':
    personHandler = PersonHandler()
    dogHandler = DogHandler()

    personHandler.next(dogHandler)
    print(personHandler.handle('DOG'))
    print(personHandler.handle('PERSON'))
    print(personHandler.handle(''))