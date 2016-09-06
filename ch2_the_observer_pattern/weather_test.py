<<<<<<< HEAD
#!/usr/bin/env python3
import WeatherData
import CurrentConditions


=======
import WeatherData
import CurrentConditions

>>>>>>> 77cd2a230ac6bc8a29d5b9e91df7dd1f7b026636
def main():
    weather_obj = WeatherData.WeatherData()
    current_cond_obj = CurrentConditions.CurrentConditions()
    print(dir(current_cond_obj))
    weather_obj.set_measurements(78, 89, 199)
    weather_obj.add_observer(current_cond_obj)
    weather_obj.set_measurements(23, 40, 123)
    current_cond_obj.display()

if __name__ == "__main__":
    main()
