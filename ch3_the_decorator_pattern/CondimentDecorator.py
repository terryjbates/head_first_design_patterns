import abc
from Beverage import Beverage as Beverage


class CondimentDecorator(Beverage):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(CondimentDecorator, self).__init__()
        self._description = str()

    @property
    def description(self):
        raise NotImplementedError()

    @description.setter
    @abc.abstractmethod
    def description(self, value):
        raise NotImplementedError()

