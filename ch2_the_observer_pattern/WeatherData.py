from Subject import Subject as Subject


class WeatherData(Subject):
    def __init__(self):
        super(WeatherData, self).__init__()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
