#!/usr/bin/env python3
import itertools

class Subject(object):
    def __init__(self):
        self.__observers = set()

    def add_observer(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def remove_observer(self, observer):
        self.__observers.discard(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)