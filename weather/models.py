from django.db import models
# from weather.serializers import WeatherSerializer

class WeatherEntity:

    def __init__(self, temperature, date,
                 city='', atmosphericPressure='',
                 humidity='', weather='', name='Vincenzo') -> None:
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date
        self.name = name

    def __str__(self) -> str:
        return (f"Weather <{self.temperature}>")
    

    # return WeatherEntity()