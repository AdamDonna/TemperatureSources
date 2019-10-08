from .models import Thermometer


class OptionReducer:

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def eligible_thermometers(self):
        # cacheable
        return [
            result for result in
            Thermometer.objects.filter(is_enabled=True)
            if result.enabled_for_country(self.city, self.country)
        ]

    def get_temperatures(self):
        # cacheable
        # List of Temperature objects
        return [
            result for result in
            self.eligible_thermometers()
            if result.get_temperature(self.city, self.country)
        ]

    def highest_temp(self):
        return max([temp.get_max_temp() for temp in self.get_temperatures()])

    def lowest_temp(self):
        return max([temp.get_min_temp() for temp in self.get_temperatures()])
