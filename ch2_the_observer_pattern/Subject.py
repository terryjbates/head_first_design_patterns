<<<<<<< HEAD
import itertools


=======
#!/usr/bin/env python3
import itertools

>>>>>>> 77cd2a230ac6bc8a29d5b9e91df7dd1f7b026636
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
