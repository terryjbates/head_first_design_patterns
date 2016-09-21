import abc


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, execute):
        assert callable(execute)
        self.execute = execute

    def __call__(self):
        self.execute()

    @abc.abstractmethod
    def execute(self):
        return NotImplementedError


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
        super(LightOnCommand, self).__init__(self.light.on)

    def execute(self):
        self.light.on()


class Light(object):
    def __init__(self):
        pass

    def on(self):
        print("Light On")

    def off(self):
        print("Light Off")


class SimpleRemoteControl(object):
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        assert isinstance(command, Command)
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


if __name__ == '__main__':
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)


    remote.set_command(light_on)
    remote.button_was_pressed()