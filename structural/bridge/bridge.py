from abc import ABC, abstractmethod


class ApiInterface(ABC):
    @abstractmethod
    def request(self) -> str:
        raise NotImplementedError()


class Api(ApiInterface):
    def request(self):
        return 'API: body'


class Api2(ApiInterface):
    def request(self):
        return 'API2: body'


class Request:
    def __init__(self, api_imp: ApiInterface):
        self.api = api_imp

    def request(self) -> str:
        return self.api.request()


if __name__ == '__main__':
    api_1 = Api()
    api_2 = Api2()

    request_1 = Request(api_1)
    request_2 = Request(api_2)

    print(request_1.request())
    print(request_2.request())
