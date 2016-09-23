import abc


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, do):
        assert callable(do)
        self.do = do

    def __call__(self):
        self.do()


class LightOnCommand(Command):
    def __init__(self, light_obj):
        assert isinstance(light_obj, Light)
        self.light = light_obj
        super(LightOnCommand, self).__init__(self.light.on)


class LightOffCommand(Command):
    def __init__(self, light_obj):
        assert isinstance(light_obj, Light)
        self.light = light_obj
        super(LightOffCommand, self).__init__(self.light.off)


class Stereo(object):
    def __init__(self):
        pass

    def on(self):
        print("Stereo On")

    def off(self):
        print("Stereo Off")

    def set_cd(self, cd_choice="Death Grips"):
        print("Setting CD to {}".format(cd_choice))

    def set_radio(self, radio_station="Hot 97"):
        print("Tuning station to {}".format(radio_station))

    def set_volume(self, volume_level):
        print("Setting volume level to {}".format(str(volume_level)))


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        assert isinstance(stereo, Stereo)
        self.stereo = stereo
        super(StereoOnWithCDCommand, self).__init__(self.__call__)

    def __call__(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door_obj):
        assert isinstance(garage_door_obj, GarageDoor)
        self.garage_door = garage_door_obj
        super(GarageDoorOpenCommand, self).__init__(self.garage_door.up)


class Light(object):
    def __init__(self):
        pass

    def on(self):
        print("Light On")

    def off(self):
        print("Light Off")


class GarageDoor(object):
    def __init__(self):
        pass

    def up(self):
        print("Garage door goes up.")

    def down(self):
        print("Garage door goes down.")

    def stop(self):
        print("Garage door stops moving.")

    def light_on(self):
        print("Garage light goes on.")

    def light_off(self):
        print("Garage light goes off.")


class SimpleRemoteControl(object):
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        assert isinstance(command, Command)
        self.slot = command

    def button_was_pressed(self):
        self.slot()


class RemoteControl(object):
    def __init__(self):
        self.__commands = []

    def add(self, command):
        if not isinstance(command, Command):
            raise TypeError("Expected object of type Command, got {}".format(type(command).__name__))
        self.__commands.append(command)

    def __call__(self):
        for command in self.__commands:
            command()

    do = __call__

    def undo(self):
        for command in reversed(self.__commands):
            command.undo()


if __name__ == '__main__':
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    garage_door = GarageDoor()
    garage_open = GarageDoorOpenCommand(garage_door)
    funky_stereo = Stereo()
    stereo_with_cd = StereoOnWithCDCommand(funky_stereo)

    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_open)
    remote.button_was_pressed()

    power_remote = RemoteControl()
    power_remote.add(light_on)
    power_remote.add(light_off)
    power_remote.add(stereo_with_cd)

    power_remote()