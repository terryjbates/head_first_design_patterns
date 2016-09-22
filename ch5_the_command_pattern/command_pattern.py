import abc


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, execute):
        assert callable(execute)
        self.execute = execute

    def __call__(self):
        self.execute()


class LightOnCommand(Command):
    def __init__(self, light_obj):
        assert isinstance(light_obj, Light)
        self.light = light_obj
        super(LightOnCommand, self).__init__(self.light.on)


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


if __name__ == '__main__':
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)
    garage_door = GarageDoor()
    garage_open = GarageDoorOpenCommand(garage_door)

    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_open)
    remote.button_was_pressed()
