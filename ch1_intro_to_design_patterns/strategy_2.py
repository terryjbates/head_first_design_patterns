#!/usr/bin/env python3
import abc


class QuackBehavior(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def __call__(cls):
        raise NotImplementedError()

    def __repr__(self):
        return str(self.__call__())

    def __str__(self):
        return str(self.__call__())


class Quack(QuackBehavior):
    @classmethod
    def __call__(cls):
        return "Quack"


class Squeak(QuackBehavior):
    @classmethod
    def __call__(cls):
        return "Squeak"


class MuteQuack(QuackBehavior):
    @classmethod
    def __call__(cls):
        pass


class FlyBehavior(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def __call__(cls):
        raise NotImplementedError()


class FlyNoWay(FlyBehavior):
    @classmethod
    def __call__(cls):
        return "Going way of the Dodo..."


class FlyWithWings(FlyBehavior):
    @classmethod
    def __call__(cls):
        return "Flyin With Wings!!!"


class FlyRocketPowered(FlyBehavior):
    @classmethod
    def __call__(cls):
        return "I'm flying with a Rocket!!!"


class Duck(object):
    def __init__(self, name, quack=QuackBehavior, fly=FlyBehavior):
        self.name = name
        self._quack = quack
        self._fly = fly

    def perform_quack(self):
        """Set a value in the instance."""
        self._quack_behavior.quack()
        return

    def perform_fly(self):
        """Set a value in the instance."""
        self._fly_behavior.fly()
        return

    def set_quack_behavior(self, qb):
        self._quack = qb

    def set_fly_behavior(self, fb):
        self._fly = fb

    def swim(self):
        """Get and return a value from the instance."""
        return

    def display(self):
        print(self.name)
        """Get and return a value from the instance."""
        return

    @property
    def quack(self):
        return self._quack

    @quack.setter
    def quack(self, qb):
        if issubclass(qb, QuackBehavior):
            self.set_quack_behavior(qb)

    @property
    def fly(self):
        return self._quack()


    @fly.setter
    def fly(self, fb):
        if issubclass(fb, FlyBehavior):
            self.set_fly_behavior(fb)


class RedheadDuck(Duck):
    def __init__(self, name):
        super(RedheadDuck, self).__init__(name, quack=Quack, fly=FlyWithWings)


if __name__ == "__main__":
    my_red_duck = RedheadDuck('Bruno')
    #my_red_duck.quack
    print(my_red_duck.quack())
    my_red_duck.set_quack_behavior(Squeak)
    print(my_red_duck.quack())
    #print(result)





