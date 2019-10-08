from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from . import models


class ThermometerBaseAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = models.Thermometer
    show_in_index = True


@admin.register(models.OpenWeatherMap)
class ModelBAdmin(ThermometerBaseAdmin):
    base_model = models.OpenWeatherMap  # Explicitly set here!
    # define custom features here


@admin.register(models.WeatherBit)
class ModelCAdmin(ThermometerBaseAdmin):
    base_model = models.WeatherBit  # Explicitly set here!


@admin.register(models.Thermometer)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    child_models = (models.OpenWeatherMap, models.WeatherBit)
