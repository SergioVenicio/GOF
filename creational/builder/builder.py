from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build(self):
        raise NotImplementedError('Implements build')


class HouseBuilder(Builder):
    def build(self):
        self.build_walls()
        self.build_window()
        self.build_rooms()
        self.build_bathrooms()

        return f'''\
        House:
            WALLS [{self.walls}]
            WINDOWS [{self.windows}]
            ROOMS [{self.rooms}]
            BATHROOMS [{self.bathrooms}]'''

    def build_walls(self):
        self.walls = 4

    def build_window(self):
        self.windows = 1

    def build_rooms(self):
        self.rooms = 2

    def build_bathrooms(self):
        self.bathrooms = 2


class AppartmentBuilder(Builder):
    def build(self):
        self.build_floor()
        self.build_walls()
        self.build_window()
        self.build_rooms()
        self.build_bathrooms()

        return f'''\
        Appartment:
            FLOOR [{self.floor}]
            WALLS [{self.walls}]
            WINDOWS [{self.windows}]
            ROOMS [{self.rooms}]
            BATHROOMS [{self.bathrooms}]
        '''

    def build_floor(self):
        self.floor = 1

    def build_walls(self):
        self.walls = 4

    def build_window(self):
        self.windows = 1

    def build_rooms(self):
        self.rooms = 1

    def build_bathrooms(self):
        self.bathrooms = 1


if __name__ == '__main__':
    house_builder = HouseBuilder()
    appartment_builder = AppartmentBuilder()

    new_house = house_builder.build()
    new_appartment = appartment_builder.build()

    print(new_house)
    print(new_appartment)
