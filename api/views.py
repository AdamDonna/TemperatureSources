from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .reducer import OptionReducer


class ReducedTemperatures(APIView):
    def get(self, request, format=None):
        reducer = OptionReducer("Aspendale", "AU")
        highest = reducer.highest_temp()
        lowest = reducer.lowest_temp()
        return Response({
            "lowest": lowest.get_min_temp(),
            "lowest_source": lowest.source,
            "highest": highest.get_max_temp(),
            "highest_source": lowest.source
        }, status=status.HTTP_200_OK)
