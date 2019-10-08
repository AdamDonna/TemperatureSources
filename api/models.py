import requests
from django.db import models
from polymorphic.models import PolymorphicModel
from .temperature import Temperature


class Thermometer(PolymorphicModel):
    # Location specific temperature as measured by different apis
    name = models.TextField(max_length=255)
    base_url = models.TextField(max_length=255)
    is_enabled = models.BooleanField(default=False)
    is_celcius = models.BooleanField(default=True)
    api_key = models.TextField(default="", max_length=255, blank=True)

    def get_temperature(self, location, country) -> Temperature:
        response = requests.get(self.base_url, params=self.get_params(location, country))
        response.raise_for_status()
        temps = self.response_parser(response)
        return Temperature(
            **temps, is_celsius=self.is_celcius
        )

    def response_parser(self, response):
        raise NotImplementedError

    def enabled_for_country(self, city, country):
        # TODO: Workout how to disable per country
        return self.is_enabled

    def get_params(self, location, country):
        params = {
            "location": location
        }
        return params


class OpenWeatherMap(Thermometer):
    # is_celcius = False

    def response_parser(self, response):
        main = response.json().get("main")
        return {
                   "current_temp": main.get("temp"),
                   "max_temp": main.get("temp_max"),
                   "min_temp": main.get("temp_min"),
                   "humidity": main.get("humidity"),
        }

    def get_params(self, location, country):
        params = {
            "location": location,
            "appid": self.api_key,
        }
        return params


class WeatherBit(Thermometer):

    def response_parser(self, response):
        main = response.json().get("data")[0]
        return {
                   "current_temp": main.get("temp"),
                   "max_temp": None,
                   "min_temp": None,
                   "humidity": None,
        }

    def get_params(self, location, country):
        return {
            "city": location,
            "country": country,
            "key": self.api_key,
        }
