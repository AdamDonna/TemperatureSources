from .models import Thermometer


class OptionReducer:

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def eligible_thermometers(self):
        # cacheable
        return [
            result.enabled_for_country(self.city, self.country) for result in
            Thermometer.objects.filter(is_active=True)
        ]

    def get_temperatures(self):
        # cacheable
        # List of Temperature objects
        return [
            result.get_temperature(self.city, self.country) for result in
            self.eligible_thermometers()
        ]

    def highest_temp(self):
        return max([temp.get_max_temp() for temp in self.get_temperatures()])

    def lowest_temp(self):
        return max([temp.get_min_temp() for temp in self.get_temperatures()])
