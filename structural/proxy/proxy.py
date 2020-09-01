from abc import ABC, abstractmethod
from datetime import datetime


class Subject(ABC):
    @abstractmethod
    def request(self):
        raise NotImplementedError()


class RealSubject(Subject):
    def request(self):
        return 'Handling Request'


class SubjectProxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print(f'[LOG][{datetime.now()}] {self._real_subject.request()}...')


if __name__ == '__main__':
    real_subject = RealSubject()
    proxy = SubjectProxy(real_subject)
    proxy.request()
