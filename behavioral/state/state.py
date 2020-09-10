class BaseState:
    station_id = 0
    def play(self):
        print(f'[{self.station_type}] {self.stations[self.station_id]}')

    def change_radio(self):
        if self.station_id < len(self.stations):
            self.station_id += 1
        else:
            self.station_id = 0


class AmState(BaseState):
    station_type = 'AM'

    def __init__(self):
        self.stations = ('100.0', '200.0', '300.0',)


class FmState(BaseState):
    station_type = 'FM'

    def __init__(self):
        self.stations = ('100.5', '200.5', '300.5',)


class Radio:
    def __init__(self):
        self._am = AmState()
        self._fm = FmState()

        self._state = self._am

    def toggle(self):
        if self._state == self._am:
            self._state = self._fm
        else:
            self._state = self._am

    def change_radio(self):
        self._state.change_radio()
    
    def play(self):
        self._state.play()

if __name__ == '__main__':
    radio = Radio()
    radio.play()
    radio.change_radio()
    radio.play()
    radio.toggle()
    radio.play()
    radio.change_radio()
    radio.play()
    