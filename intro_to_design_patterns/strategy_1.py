#!/usr/bin/env python3
import abc


class Duck(object):
    def __init__(self, name):
        self.name = name
        self._quack_behavior = QuackBehavior()
        self._fly_behavior = FlyBehavior()

    def perform_quack(self):
        """Set a value in the instance."""
        self._quack_behavior.quack()
        return

    def perform_fly(self):
        """Set a value in the instance."""
        self._fly_behavior.fly()
        return

    def set_quack_behavior(self, qb):
        self._quack_behavior = qb

    def set_fly_behavior(self, fb):
        self._fly_behavior = fb

    def swim(self):
        """Get and return a value from the instance."""
        return

    def display(self):
        print(self.name)
        """Get and return a value from the instance."""
        return


class QuackBehavior(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def quack(cls):
        raise NotImplementedError()


class Quack(QuackBehavior):
    @classmethod
    def quack(cls):
        print("Quack")


class Squeak(QuackBehavior):
    @classmethod
    def quack(cls):
        print("Squeak")


class MuteQuack(QuackBehavior):
    @classmethod
    def quack(cls):
        pass


class FlyBehavior(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def fly(cls):
        raise NotImplementedError()


class FlyNoWay(FlyBehavior):
    @classmethod
    def fly(cls):
        print("Going way of the Dodo...")


class FlyWithWings(FlyBehavior):
    @classmethod
    def fly(cls):
        print("Flyin With Wings!!!")


class FlyRocketPowered(FlyBehavior):
    @classmethod
    def fly(cls):
        print("I'm flying with a Rocket!!!")


class RedheadDuck(Duck):
    def __init__(self, name):
        super(RedheadDuck, self).__init__(name)
        self.set_fly_behavior(FlyWithWings())
        self.set_quack_behavior(Quack())


if __name__ == "__main__":
    my_red_duck = RedheadDuck('Bruno')
    my_red_duck.perform_quack()
    my_red_duck.perform_fly()
    my_red_duck.set_fly_behavior(FlyRocketPowered())
    my_red_duck.perform_fly()

    test_duck = RedheadDuck("John")
    test_duck.set_quack_behavior(Squeak())
    test_duck.perform_quack()
    

