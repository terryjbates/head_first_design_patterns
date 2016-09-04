#!/usr/bin/env python3
import abc


class Duck(object):
    def __init__(self, name):
        self.name = name
        self.quack_behavior = QuackBehavior()
        self.fly_behaviour = FlyBehavior()

    def perform_quack(self):
        """Set a value in the instance."""
        QuackBehavior.quack()
        return

    def perform_fly(self):
        """Set a value in the instance."""
        FlyBehavior.fly()
        return


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


class RedheadDuck(Duck):
    def perform_fly(self):
        FlyWithWings.fly()

    def perform_quack(self):
        Quack.quack()

if __name__ == "__main__":
    my_red_duck = RedheadDuck('Bruno')
    my_red_duck.perform_quack()
    my_red_duck.perform_fly()
