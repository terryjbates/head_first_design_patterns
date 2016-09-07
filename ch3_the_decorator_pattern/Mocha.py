from Beverage import Beverage
from CondimentDecorator import CondimentDecorator as condi_deco


class Mocha(condi_deco):
    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self.set_beverage(beverage)

    @property
    def beverage(self):
        return self._beverage

    @beverage.setter
    def beverage(self, input_bev):
        if isinstance(input_bev, Beverage):
            self._beverage = input_bev
            self.set_description()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    
    def set_beverage(self, input_bev):
        if isinstance(input_bev, Beverage):
            self._beverage = input_bev
            self._description = self.beverage.description + " " + "Mocha"
