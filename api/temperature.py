class Temperature:
    def __init__(self, current_temp, max_temp, min_temp, humidity, is_celsius=False):
        self.is_celsius = is_celsius
        self.current_temp = current_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.humidity = humidity

    def getter_proxy(self, field):
        if not field:
            return None
        if not self.is_celsius:
            return self.to_celsius(field)
        return field

    def get_max_temp(self):
        return self.getter_proxy(self.max_temp)

    def get_min_temp(self):
        return self.getter_proxy(self.min_temp)

    def get_current_temp(self):
        return self.getter_proxy(self.current_temp)

    @staticmethod
    def to_celsius(temperature):
        # assumes fareignheight
        return 9.0/5.0 * temperature + 32
