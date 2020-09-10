from abc import ABC, abstractmethod


class Analizer(ABC):
    def __init__(self, file_path):
        self._file_path = file_path

    def proccess(self):
        self.open()
        self.read()
        self.analize()
        self.save()

    def open(self):
        print(f'OPEN: {self._file_path}')

    def read(self):
        print(f'READ: {self._file_path}')

    def save(self):
        print(f'SAVE: {self._file_path}')

    @abstractmethod
    def analize(self):
        pass


class CSVAnalizer(Analizer):
    def analize(self):
        print(f'[CSV] ANALIZE: {self._file_path}')


class XLSAnalizer(Analizer):
    def analize(self):
        print(f'[XLS] ANALIZE: {self._file_path}')


if __name__ == '__main__':
    csv = CSVAnalizer('file.csv')
    xls = XLSAnalizer('file.xls')

    csv.proccess()
    print('***')
    xls.proccess()
    