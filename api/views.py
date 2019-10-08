from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .reducer import OptionReducer


class ReducedTemperatures(APIView):
    def get(self, request, format=None):
        print(OptionReducer("Aspendale", "AU").eligible_thermometers())
        return Response({}, status=status.HTTP_200_OK)
