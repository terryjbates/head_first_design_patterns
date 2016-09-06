#!/usr/bin/env python3


class CurrentConditions(object):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def update(self, model):
        self.temperature = model.temperature
        self.humidity = model.humidity
        self.pressure = model.pressure
        self.display()

    def display(self,):
        print("Current conditions: {} F degrees and {} % humidity".format(
            self.temperature, self.humidity))
