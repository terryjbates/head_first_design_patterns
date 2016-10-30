
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