import abc


class Beverage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._description = "Unknown beverage"
        self._cost = 0

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, input_description):
        if isinstance(input_description, str):
            self._description = input_description

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, input_cost):
        if isinstance(input_cost, float) or  isinstance(input_cost, int):
            self._cost = input_cost
