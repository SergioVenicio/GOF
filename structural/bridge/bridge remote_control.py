from abc import ABC


class Device(ABC):
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def get_volume(self):
        pass

    def set_volume(self, volume: int):
        pass

    def get_channel(self):
        pass

    def set_channel(self, channel: int):
        pass


class Tv(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 0
        self.channel = 0

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, volume: int):
        self.volume = volume

    def get_channel(self):
        return self.channel

    def set_channel(self, channel: int):
        self.channel = channel


class Radio(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 0
        self.channel = 0

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, volume: int):
        self.volume = volume

    def get_channel(self):
        return self.channel

    def set_channel(self, channel: int):
        self.channel = channel


class Control:
    def __init__(self, device: Device):
        self._device = device

    def toogle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedControl(Control):
    def mute(self):
        self._device.set_volume(0)


if __name__ == '__main__':
    tv = Tv()
    radio = Radio()

    tv_control = AdvancedControl(tv)
    radio_control = AdvancedControl(radio)

    tv_control.volume_up()
    tv_control.volume_up()
    tv_control.volume_up()
    tv_control.channel_up()

    print(f'TV volume: {tv.get_volume()}')
    print(f'TV channel: {tv.get_channel()}')

    radio_control.volume_up()
    radio_control.channel_up()

    print(f'RADIO volume: {radio.get_volume()}')
    print(f'RADIO channel: {radio.get_channel()}')
